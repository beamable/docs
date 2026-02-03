# Federated Identity

Beamable supports custom authentication federation using managed [microservices](https://docs.beamable.com/docs/microservices-feature-overview). You can use this feature to implement an OAuth2, OpenID Connect, or a custom external authentication provider and use it with Beamable. We also support two-way challenge-based flows for PKI-based authentication for Web3/blockchain scenarios. Some use cases:

- Blockchain wallet authentication - Attach a wallet to a player's account and use it for authentication.
- External authentication provider integration - Already using something like Auth0? Use it for your game to achieve a Single Sign-On experience.

Here we will go through the steps to create a custom authentication federation.

## Creating a Custom Federation

### Creating a microservice

You should first create a microservice or use an existing one. You can bundle multiple authentication federations in a single microservice using the `UniqueName` value of cloud identity classes to establish namespaces. This is illustrated by the difference between "tuna" and "haddock" below.

### Implementing an IFederationId interface

Create an implementation of IThirdPartyCloudIdentity in Beamable/Common (or any shared assembly).
This will create a "tuna" namespace for your new authentication scheme. Namespace will be a part of the authentication endpoint path. In the following example, TunaCloudIdentity will correspond to `/your_microservice/tuna/authenticate` and HaddockCloudIdentity will correspond to `/your_microservice/haddock/authenticate`.

```csharp
[FederationId("tuna")]
public class TunaCloudIdentity : IFederationId
{
}

[FederationId("haddock")]
public class HaddockCloudIdentity : IFederationId
{
}
```

### Implementing IFederatedLogin in your microservice

Let's say you already have a TunaService that holds all your user's data. We will use it to validate a "token" received by the client and respond with a "user_id".

```csharp
[Microservice("AuthenticationMicroservice")]
public class AuthenticationMicroservice : IFederatedLogin<TunaCloudIdentity>, IFederatedLogin<HaddockCloudIdentity>
{
  public async Promise<FederatedAuthenticationResponse> IFederatedLogin<TunaCloudIdentity>.Authenticate(string token, string challenge, string solution)
  {
    // Token can be something like an authorization_code, depending on your client and service implementations
    var tunaUserResponse = await TunaService.GetUserByAuthorizationCode(token);
    if (tunaUserResponse == null)
    {
        throw new UnauthorizedException();
    }
    return new FederatedAuthenticationResponse { user_id = tunaUserResponse.userId };
  }
  
  public async Promise<FederatedAuthenticationResponse> IFederatedLogin<HaddockCloudIdentity>.Authenticate(string token, string challenge, string solution)
  {
  	throw new NotImplementedException("Haddock identity is not implemented. Please use Tuna identity instead.");
  }
}
```

In this example, we didn't use the "challenge" and "solution" arguments. The standard use case for challenges is wallet authentication. If a client sends us a wallet address as a token, the only way to verify the ownership of that wallet is to issue a challenge, and require a user to sign that challenge using their private key. [Solana/Phantom wallet authentication](https://github.com/beamable/solana-example) is an example that uses a challenge.

### Attaching an external identity to a player (CLIENT)

```csharp
var ctx = BeamContext.Default;
var response = await ctx.Accounts
  .AddExternalIdentity<TunaCloudIdentity, AuthenticationMicroserviceClient>(_authorizationCode);
```

### Login-in using an external identity (CLIENT)

```csharp
var ctx = BeamContext.Default;
var accountRecoveryResponse = await ctx.Accounts
  .RecoverAccountWithExternalIdentity<TunaCloudIdentity, AuthenticationMicroserviceClient>(_authorizationCode);
await accountRecoveryResponse.SwitchToAccount();
```

### Running or Publish your microservice

Previous to the Beamable Mercury release (Unity 2.0, CLI 3.0, and UE 1.0), you would need to publish the service in order to test federation. However, now you can test federations with a locally running service.

## More Samples
Here are some more examples of federated identity implementations:
- [Solana/Phantom authentication and inventory federation](https://github.com/beamable/solana-example)
