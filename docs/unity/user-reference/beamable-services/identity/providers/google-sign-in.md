# Google Sign-In

The purpose of this guide is to help game makers use Google Sign-In with the Beamable Accounts feature.

Beamable integrates with Google's Sign-In service to provide seamless authentication for your game. Google's [Sign-In](https://developers.google.com/identity/sign-in/web/sign-in) manages the OAuth 2.0 flow and token lifecycle, simplifying your integration with Google APIs. A user always has the option to revoke access to an application at any time.

## Getting Started

This guide provides step-by-step instructions to set up Google Sign-In with Beamable's Accounts feature in a Unity project.

!!! note "Google Play Game Services"
    This guide covers Google Sign-In using OAuth. It does not apply to Google Play Game Services (GPGS), which uses a different authentication flow.

### Create a Unity Project

**Set up the Beamable SDK for Unity**

   - See Beamable's [Getting Started](../../../../getting-started/installing-beamable.md) for more info

**Switch platform to Android**

   - Unity → File → Build Settings
   - Select Android, then press Switch Platform

**Set Package Name**

   - Unity → File → Build Settings → Player Settings
   - Set your package name (e.g., `com.yourcompany.yourgame`)
   - You will need this exact package name for the Google Cloud Console setup

### Create KeyStore for Signing

**Create a KeyStore**

   - Go to Unity → File → Build Settings → Player Settings
   - In Inspector, go to **Publishing Settings** and create the keystore (or unlock an existing one)
   - **Important:** Save the password securely

**Record the KeyStore SHA-1 Fingerprint**

   - Open a terminal where you created the keystore and run:
   ```bash
   keytool -list -v -keystore <your.keystore>
   ```
   - Look for the SHA-1 fingerprint in the output and save it
   - If you don't have `keytool` installed, follow the instructions after installing Java on your machine: [Here](https://stackoverflow.com/questions/5488339/how-can-i-find-and-run-the-keytool)

### Create Google Cloud Console - OAuth 2.0 Credentials

**Create a Project & Enable APIs:**

   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create OR select an existing project
   - Go to **APIs & Services** → **Enable APIs and Services**
   - Enable the following API: **Google+ API**

**Create Credentials:**

Go to **API & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**

You need to create **TWO** credentials:

**Web Application Credentials:**

   - Select "Web application" as the application type
   - Give it a name
   - **Important:** Save the **Client ID** and **Client Secret** - you will need these later

**Android Credentials:**

   - Select "Android" as the application type
   - Enter your exact package name (from Step 1.3)
   - Enter the SHA-1 fingerprint (from Step 2.2)
   - Save the Client ID just in case it is necessary later

!!! warning "Important"
    You will need both Web application credentials AND platform-specific credentials for Android or iOS or both.

---

### Configure Unity Project

Beamable's Google Sign-In integration requires `play-services-auth` in your Android build.

#### Enable Custom Android Gradle Template

- Change platform to Android (if not already done)
- Enable Custom Gradle Template: **Project Settings** → **Player** → **Other Settings** → **Custom Gradle Template**
- This will generate a file at `Plugins/Android/mainTemplate.gradle`

#### Add play-services-auth Dependency

- Open the `.gradle` file located in your project at `Plugins/Android/mainTemplate.gradle`
- Look for the `dependencies` block
- Add `play-services-auth` as shown below:

```gradle
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'com.google.android.gms:play-services-auth:21.5.0'
    **DEPS**
}

```

---

### Additional iOS Setup

When using Google Sign-In on Apple, the Login Flow depends on version 5 of Google's Sign-In SDK framework for iOS. Enabling sign-in on iOS also requires first-time setup regarding a custom URL scheme specific to your Google Cloud App, including overriding the `openURL` method on `UnityAppController`.

| Step | Detail |
| --- | --- |
| **1. Install the Google Sign-In SDK** | Download Google Sign-In SDK version 5.0.0 or newer from [https://developers.google.com/identity/sign-in/ios/sdk](https://developers.google.com/identity/sign-in/ios/sdk)<br><br>Create the `Assets/Plugins/iOS` folder in your Unity project if it does not already exist<br><br>Extract the SDK archive, then copy `GoogleSignIn.framework` and `GoogleSignInDependencies.framework` to your `Assets/Plugins/iOS` folder |
| **2. Add the URL scheme to your project** | Your custom URL scheme is a reversed version of your iOS Client ID: `com.googleusercontent.apps.<your-app-id>`<br><br>Unity → File → Build Settings → Player Settings → Other Settings<br><br>Supported URL schemes: set size to 1 and enter your reversed ID as Element 0 |
| **3. Ensure app delegate handles `openURL`** | The app delegate for your app should handle `application:openURL:options:` and invoke the `handleURL` method of `GIDSignIn`. |

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

- **Switch Player** - Player wants to switch credentials to a new Player
- **Create New Player** - Player wants to create a new Player account
- **Attach To Current Player** - Player wants to Attach this 3rd Party Login to an already authenticated Player

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

If we want to create a new user and apply the third-party credentials, we can use the following calls from AuthService.

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


## Next Steps

- Players can edit account details (name, avatar).
- Players can switch accounts or sign in with various methods. See the [Identity](../identity.md) feature page for more info.
