# Authenticating the API

Most of the Beamable API requires authentication. To be authenticated, each request needs to carry user identification, project identification, and a privileged credential. There are multiple methods to achieve those requirements. Which method you select depends on your use case.


### Player Scoped Authentication

The most common way to authenticate requests is to use player scoped authentication. Each request should include headers that will specify the user identification, project identification, and credential. 

Notably, developer accounts are also player accounts, but with higher privileges. Anyone can make a guest account for your game, which means they are a _player_. However, through Portal, you can grant specific accounts higher levels of access, such as _tester_, _developer_, or _admin_. 

Different APIs require different levels of privilege. 

To authenticate a request using player scoped authentication, you need to include a few headers on the request. 

#### `X-BEAM-SCOPE`

The `X-BEAM-SCOPE` header carries project identification in the format, `<cid>.<pid>`. For example, if your `cid` was `123`, and your `pid` was `456`, the header value would be `123.456`.

Remember, you can find your `cid` and `pid` on Portal by using the `/games` page. 

!!! tip 
    You can use your `alias` in place of the `cid`.

#### `Authorization`

The `Authorization` header carries the user credential in the format, `Bearer <token>`. For example, if your token was `123`, the header value would be `Bearer 123`. 

There are two types of tokens, 
1. GUID tokens,
2. JWTs

You can find these tokens in a variety of ways, or generate a new one for a guest account. Here are _some_ methods to find a token for using the API directly.

##### Create a new guest account

If you want a brand new player account to experiment with, you can create one by issuing a request to one of the few _public_ APIs in Beamable that does not require any authentication at all. 

```sh
curl -X POST "https://api.beamable.com/basic/auth/token" \
    -H 'accept: application/json'\
    -H 'content-type: application/json'\
    -H 'x-beam-scope: <cid>.<pid>' \
    -d '{"grant_type":"guest"}' 
```

!!! note
    Make sure to fill in your own custom `X-BEAM-SCOPE` header.

##### Log in with email & password

If you have a player that has an email & password associated with it (such as a developer account), you can retrieve an access token for that account by using the credentials. 

```sh
curl -X POST "https://api.beamable.com/basic/auth/token" \
    -H 'accept: application/json'\
    -H 'content-type: application/json'\
    -H 'x-beam-scope: <cid>.<pid>' \
    -d '{"username":"<email>","grant_type":"password","password":"<password>"}' 

```

!!! note
    Make sure to fill in your own custom `X-BEAM-SCOPE` header, as well as pass the `<email>` and `<password>` values in the `"username"` and `"password"` fields respectively. 


##### Use the CLI

If you have initialized a `.beamable` workspace on your computer, you can use the following command to find your local developer token:

!!! tip
    This examples assumes you have `jq` available. If you do not, just look at the output and find the `accessToken` field.

```sh
beam me | jq .data.accessToken
```

Remember, both the Beamable Unity and Unreal SDKs create `.beamable` workspaces automatically. For example, you could run the `beam me` command within your Unity project folder. 

##### Grab it from the Portal

A common debug technique for acquiring a token is to snoop the token from your browser. Go to Portal and sign in. Open the developer tools in your browser, go to the _network_ tab, and find any request going to `api.beamable.com`. Observe the request headers, and look for the `Authorization` header value. You can copy/paste the header value for your own debugging purposes. 

#### `X-BEAM-GAMERTAG`

The `X-BEAM-GAMERTAG` header carries the user identification in the format, `<gamertag>`. For example, if the player's gamertag was `123`, the header value would be `123`. 

Normally, the `Authorizaton` header carries enough information to imply the user identification, but if you needed to _override_ the user, use this header. 

!!! tip 
    **This header is optional** for player scoped requests. 



### Signed Requests

Beamable supports server-to-server privileged API requests in addition to token based access. In contrast to token based requests which must act as a particular Beamable user (who may or may not have administrative privileges), signed requests act as a server entity with universal privileges in its realm. This allows for server-authoritative action such as setting "game.private" stats, submitting scores to leaderboards whose "writeSelf" access is false, and so on.

In technical terms, signed requests differ from token based requests in several ways:

- Signed requests never have an `Authorization:` header; instead, they rely on the signature to prove their authorization
- Signed requests must include a signature in the `X-BEAM-SIGNATURE:` header. The procedure for calculating the signature value is described below.
- Signed requests may include a player ID in the `X-BEAM-GAMERTAG:` header; this is useful when using an API route that is normally player-oriented and usually gets the player ID implicitly from the access token.

Both token based requests and signed requests require the `X-BEAM-SCOPE:` header to indicate which realm they are operating in. The format for the scope header is a dotted pair of CID (numeric organization ID) and PID (project ID, identifying the realm within the organization). Example: `X-BEAM-SCOPE: 1434605640884224.DE_1434605640884225`

#### Calculating Signatures

The signature for any given request is a one-way hash of five pieces of information:

1. Realm Secret (a UUID)
2. The PID of the realm
3. API version string; at present the version is always "1"
4. The path part of the URL including its leading slash (for example: `/basic/tournaments/rewards`)
5. The exact body of the request, if it has one

To calculate the signature, concatenate these five strings, take the digest of the MD5 hash of the concatenated plaintext, and Base64-encode it. This should result in a Base64 string a couple dozen characters long.

```csharp
public class BeamableSignedRequester
{
	private HttpClient _client;
	private string _cid, _pid, _secret;

	public BeamableSignedRequester(string cid, string pid, string secret, HttpClient client = null)
	{
		_cid = cid;
		_pid = pid;
		_secret = secret;
		_client = client ?? new HttpClient();
	}

	/// <summary>
	/// Calculate the Beamable signature for a given request. This signature
	/// can be used in the X-BEAM-SIGNATURE header of a HTTP request to make
	/// a privileged request to the Beamable API.
	/// </summary>
	/// <param name="pid">Project ID of the realm ("DE_...")</param>
	/// <param name="secret">The realm secret, which is a UUID</param>
	/// <param name="uriPathAndQuery">Path and query parts of the URI</param>
	/// <param name="body">Request body, if any</param>
	/// <returns>Signature as a short Base64 string</returns>
	public static string CalculateSignature(string pid, string secret, string uriPathAndQuery, string body = null)
	{
		const string version = "1";
		var md5 = System.Security.Cryptography.MD5.Create();
		var dataToSign = $"{secret}{pid}{version}{uriPathAndQuery}";
		if (body != null) dataToSign += body;

		byte[] data = Encoding.UTF8.GetBytes(dataToSign);
		byte[] hash = md5.ComputeHash(data);
		return Convert.ToBase64String(hash);
	}

	public string CalculateRequestSignature(string uriPathAndQuery, string body = null) =>
		CalculateSignature(_pid, _secret, uriPathAndQuery, body);

	public async Task<HttpResponseMessage> Request(HttpMethod method, Uri uri, string body = null)
	{
		var signature = CalculateRequestSignature(uri.PathAndQuery, body);
		var request = new HttpRequestMessage(method, uri);
		request.Headers.Add("X-BEAM-SCOPE", $"{_cid}.{_pid}");
		request.Headers.Add("X-BEAM-SIGNATURE", signature);
		if (body != null)
			request.Content = new StringContent(body, Encoding.UTF8, "application/json");

		var response = await _client.SendAsync(request);
		return response;
	}
}

```
