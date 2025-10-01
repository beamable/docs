# Google Sign-In

The purpose of this guide is for game makers to use Google Sign-In with the Beamable Accounts feature.

Beamable integrates with Google's Sign-In service to provide seamless authentication for your game. Google's [Sign-In](https://developers.google.com/identity/sign-in/web/sign-in) manages the OAuth 2.0 flow and token lifecycle, simplifying your integration with Google APIs. A user always has the option to revoke access to an application at any time.

When set up properly, the user experience in the game project will be as follows:
![google-experience.png](../../../../media/imgs/google-experience.png)

!!! info "Prerequisites"
    Before Google Sign-In will work properly, the Unity project must be configured to support Google as a third-party authentication provider.

    - [Prerequisites](google-sign-in-guide#prerequisites)
    - [Configure Unity Project](google-sign-in-guide#configure-unity-project)
    - [Configure iOS Settings](google-sign-in-guide#additional-ios-setup) (if applicable)

## Google Sign-In Integration

The Beamable SDK contains a wrapper for native Google Sign-In behavior on Android and iOS. The provided class is called GoogleSignIn, which can be initialized with the correct Web Client ID, iOS Client ID, as well as a "target" (a context for the sign in callback to attach to), and a callback method name.

```csharp
private GoogleSignIn _google;

private string webClientId;
private string iosClientId; //can be left blank if iOS is unsupported

/// <summary>
/// Starts Google Login process, then calls GoogleAuthResponse with a message.
/// </summary>
public void StartGoogleLogin()
{
    _google = new GoogleSignIn(gameObject, "GoogleAuthResponse", webClientId, iosClientId);
    _google.Login();
}
```

After the Login process is started, the callback function (GoogleAuthResponse) will be invoked with a message:

```csharp
/// <summary>
/// Callback to be invoked via UnitySendMessage when the plugin either
/// receives a valid ID token or indicates an error.
/// </summary>
/// <param name="message">Response message from the Google Sign-In plugin</param>
private void GoogleAuthResponse(string message)
{
    GoogleSignIn.HandleResponse(message, token =>
        {
            if (token == null)
            {
                //Login failed or was cancelled
            }
            else
            {
                //Login successful, see additional functions below
            }
        },
        errback => { Debug.LogError(errback); });
}
```

## Handle Various Flow Scenarios

Now that we have the Google credential (token), we need to account for 3 different scenarios:

- New Player
- Returning Player already linked to Google
- Returning Player linking their account with Google

We can account for this by determining if we need to:

Switch Player - Player wants to switch credentials to a new Player  
Create New Player - Player wants to Create a new Player account  
Attach To Current Player - Player wants to Attach this 3rd Party Login to an already authenticated Player.

!!! info "Beamable SDK Initialization"
    The following assumes that you have initialized the Beamable SDK and it is stored in _beamContext variable.

    ```csharp
    _beamContext = BeamContext.Default;
    await _beamContext.OnReady;
    ```

The following code will establish conditions for various flow scenarios.

```csharp
//Specify the third party auth provider
var thirdParty = AuthThirdParty.Google;
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

### Switch Users

In this example, the AuthService is used to authenticate a user with a third-party auth provider.

```csharp
if(shouldSwitchUsers)
{
	  await _beamContext.Api.AuthService.LoginThirdParty(thirdParty, token, false);
}
```

### Create New User

If we want to create a new user then apply the third party credentials, we can use the following calls from AuthService.

```csharp
if(shouldCreateUser)
{
	  var tokenResponse = await _beamContext.AuthService.CreateUser();
	  _beamContext.ApplyToken(tokenResponse);
    var user = await _beamContext.Api.AuthService.RegisterThirdPartyCredentials(thirdParty, token);
    _beamContext.Api.UpdateUserData(user);
}
```

### Link To Existing User

If the user already exists and is now trying to link their Google credentials to it, the flow is very similar to new user creation.

```csharp
if(shouldAttachToCurrentUser)
{
 	  var user = await _beamContext.Api.AuthService.RegisterThirdPartyCredentials(thirdParty, token);
    _beamContext.Api.UpdateUserData(user);
}
```

## Remarks

A complete example demonstrating the functionality for Google Sign-In can be found in GoogleSignInBehavior.cs, which is used by the Account Management Flow prefab packaged with Beamable.
