# Google Sign-In

The purpose of this guide is for game makers to use Google Sign-In with the Beamable Accounts feature.

Beamable integrates with Google's Sign-In service to provide seamless authentication for your game. Google's [Sign-In](https://developers.google.com/identity/sign-in/web/sign-in) manages the OAuth 2.0 flow and token lifecycle, simplifying your integration with Google APIs. A user always has the option to revoke access to an application at any time.

!!! info "Prerequisites"
    Before Google Sign-In will work properly, the Unity project must be configured to support Google as a third-party authentication provider.

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

## Getting Started

This guide provides step-by-step instructions to set up Google Sign-In with Beamable's Accounts feature in a Unity project.

### Prerequisites

This guide assumes the following prerequisites have been completed:

| Steps | Details |
| --- | --- |
| **1. Unity: Set up the Beamable SDK for Unity** | • See Beamable's [Getting Started](../../../../getting-started/installing-beamable.md) for more info |
| **2. Unity: Switch platform to Android** | • Unity → File → Build Settings<br>• Select Android then press Switch Platform |
| **3. Unity: Establish Keystore for Signing** | • Unity → File → Build Settings<br>• Press Player Settings...<br>• In Inspector, go to Publishing Settings and create the keystore (or unlock an existing one). |
| **4. Android: Set up the corresponding Google Cloud Platform application with OAuth 2.0 credentials** | • See Google's [start-integrating#configure_a_project](https://developers.google.com/identity/sign-in/android/start-integrating#configure_a_project) for more info<br>**Note:** You will need both Web application credentials AND platform specific credentials for Android or iOS or both. |

---

### Configure Unity Project

In orther to setup the Unity Project you need to edit gradle file.

- Open the `.gradle` file located in your project at `Plugins/Android/mainTemplate.gradle`. Look for the `dependencies` block and add `play-services-auth`.

See the code sample below.


```gradle
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.google.android.gms:play-services-auth:18.1.0'
    **DEPS**
}

```

---

### Additional iOS Setup

When using Google Sign-In on Apple, the Login Flow depends on version 5 of Google's Sign-In SDK framework for iOS. Enabling sign-in on iOS also requires first-time setup regarding a custom URL scheme specific to your Google Cloud App, including overriding the `openURL` method on `UnityAppController`.

| Step | Detail |
| --- | --- |
| **1. Install the Google Sign-In SDK** | • Download Google Sign-In SDK version 5.0.0 or newer from [https://developers.google.com/identity/sign-in/ios/sdk](https://developers.google.com/identity/sign-in/ios/sdk)<br>• Create the `Assets/Plugins/iOS` folder in your Unity project if it does not already exist<br>• Extract the SDK archive, then copy `GoogleSignIn.framework` and `GoogleSignInDependencies.framework` to your `Assets/Plugins/iOS` folder |
| **2. Add the URL scheme to your project** | • Your custom URL scheme is a reversed version of your iOS Client ID: `com.googleusercontent.apps.<your-app-id>`<br>• Unity -> File -> Build Settings -> Player Settings... -> Other Settings<br>• Supported URL schemes: set size to 1 and enter your reversed ID as Element 0 |
| **3. Ensure app delegate handles `openURL`** | • The app delegate for your app should handle `application:openURL:options:` and invoke the `handleURL` method of `GIDSignIn`. |

#### Method Swizzling for iOS URL Handling

The response from the Google Sign-In flow on Apple uses the custom **Supported URL Scheme**. This requires that the app delegate (`UnityAppController`) implement the `openURL` method. Using **swizzling**, we can define a new method and exchange implementations at runtime.

Place both `GoogleSignInAppController.h` and `GoogleSignInAppController.mm` within a `Plugins/iOS` folder in your Unity project.

**GoogleSignInAppController.h**

```objectivec
#import <GoogleSignIn/GIDSignIn.h>
#import <UnityAppController.h>

@interface UnityAppController (GoogleSignInAppController)

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
            options:(NSDictionary<NSString *, id> *)options;

@end

```

**GoogleSignInAppController.m**

```objectivec
#import "GoogleSignInAppController.h"
#import <objc/runtime.h>

@implementation UnityAppController (GoogleSignInController)

+ (void)load {
    method_exchangeImplementations(
        class_getInstanceMethod(self, @selector(application:openURL:options:)),
        class_getInstanceMethod(self, @selector(GoogleSignInAppController:openURL:options:))
    );
}

- (BOOL)GoogleSignInAppController:(UIApplication *)app
                           openURL:(NSURL *)url
                           options:(NSDictionary *)options {
    BOOL handled = [self GoogleSignInAppController:app openURL:url options:options];
    return [[GIDSignIn sharedInstance] handleURL:url] || handled;
}

@end

```

### Next Steps

* Players can edit account details (name, avatar).
* Players can switch accounts or sign in with various methods. See the [Identity](../identity.md) feature page for more info.