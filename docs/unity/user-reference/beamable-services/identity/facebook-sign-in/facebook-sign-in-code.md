# Facebook Sign-In - Code

You can use Facebook Sign-In without the prefab Account Management Flow as well. Below are the integration steps that will allow you to implement Facebook Sign-In & Beamable via Code.

!!! info "Prerequisites"
    You will still need to follow some Prerequisites, Configure Unity Project & Configure Beamable steps from the [Facebook Sign-In - Guide](facebook-sign-in-guide.md).
    - [Prerequisites](facebook-sign-in-guide.md#prerequisites)
    - [Configure Unity Project](facebook-sign-in-guide.md#configure-unity-project)
    - [Configure Beamable](facebook-sign-in-guide.md#configure-beamable)

While the guide describes a solid implementation of using the Facebook Sign-In feature, this section will describe several API pieces for you to implement your own wrapper. 

## Facebook Login & Callbacks

Ultimately you will have to implement the Facebook SDK and listen for the callback with the Login Result. The callback is triggered by the _FB.LogInWithReadPermissions()_ API call.

```csharp
var perms = new List<string>(){"public_profile", "email"};
FB.LogInWithReadPermissions(perms, result => FB_AuthCallback(result));
```

In this example, we are forwarding the result into our own method. In this method you should check for errors from Facebook. In addition, you would check to ensure that login was successful.

```csharp
private void FB_AuthCallback (ILoginResult result) 
{
	if(!string.IsNullOrEmpty(result.Error)){
  	 //There was an error to handle
     return;
	}
  
  if(FB.IsLoggedIn){
		//User is logged into facebook successfully.
    
    // AccessToken class will have session details
    var aToken = Facebook.Unity.AccessToken.CurrentAccessToken;
    
    return;
	}
}
```

## Beamable Login with AccessToken

!!! info "Beamable SDK Initialization"
    The following assumes that you have initialized the Beamable SDK and it is stored in _beamContext variable.
    _beamContext = BeamContext.Default;
    await _beamContext.OnReady;

In the [Facebook Sign-In - Guide](facebook-sign-in-guide.md), we've passed in an additional helper object that will automate the Beamable login flow process. However, in this document we will expose what is "under the hood" of that helper.

### Getting the access token string

```csharp
// AccessToken class will have session details
var aToken = Facebook.Unity.AccessToken.CurrentAccessToken;
var tokenString = aToken.TokenString;
```

You will want a reference to the actual TokenString to pass to the Beamable 3rd Party Login Service. 

### IsThirdPartyAvailable

With the access token, we need to check if this third party provider is available to the logged in user. It will return a boolean.

```csharp
var thirdParty = AuthThirdParty.Facebook;
var available = _beamContext.Api.AuthService.IsThirdPartyAvailable(thirdParty, tokenString);
```

## Handle Various Flow Scenarios

Now that we have the Facebook token, we need to account for 3 different scenarios:

- Switch Player - Player wants to switch credentials to a new Player 
- Create New Player - Player wants to Create a new Player account
- Attach To Current Player - Player wants to Attach this 3rd Party Login to an already authenticated Player.

```csharp
//Specify the third party auth provider
var thirdParty = AuthThirdParty.Facebook;
//Get information about the user's third party credential
var available = await _beamContext.Api.AuthService.IsThirdPartyAvailable(thirdParty, token);
var userHasCredentials = _beamContext.Api.User.HasThirdPartyAssociation(thirdParty);

//Should we switch to a user that's not currently logged in?
var shouldSwitchUsers = !available;
//Should we create a brand new user with these credentials?
var shouldCreateUser = available && userHasCredentials;
//Should we attach the credentials to an existing user?
var shouldAttachToCurrentUser = available && !userHasCredentials;
```

