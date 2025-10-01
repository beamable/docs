# Frictionless Authentication

Beamable’s SDK provides frictionless authentication by default when the SDK is initialized. This is completely done for you under the hood. It is quite simple, and thus the Code Sample for it is short. However, this is an opportunity for you to learn more about the Beamable SDK and what it does for you when it is initialized from any “prefab”, service or API.

## Frictionless Flow Diagram

![Frictionless Flow](../../../../../media/imgs/frictionless_auth_lifecycle.png)

Whenever you use Beamable, you should initialize the SDK, this can be done more than once as it uses the Singleton pattern under the hood. That means it will only ever create one instance the Beamable API and it returns a reference to that instance.

Upon Initialization it passes necessary data about your device, such as Device ID, to the Beamable service to determine if a user has been created for this device yet. If it has not been created, it will create one for you and return an authorization token. If it has been created it will just return the authorization token.

## Error Handling

Because initialization must communicate with the Beamable service, it is possible for an error to be thrown. It is up to you to determine the best course of action for when these errors occur. 

If your game is an **Online** game, then you may want to return an error message to the player. If your game has offline play, you may want to hide these errors but take another course of action to enable the offline mode functionality of the game.


## Initializing the Beamable SDK

Put this at the top of your class or any MonoBehaviour as a way to access the Beamable APIs.

```csharp
private BeamContext _beamContext;
```

At face value, the following creates a player instance with access to Beamable APIs. But, under the hood, it is creating an anonymous user for you, if one doesn’t exist. It also assigns a User Id, also known as the PlayerId. The PlayerId can be used to look up the player in [Portal](https://docs.beamable.com/docs/portal).

```csharp
private async void Start()
{
    _beamContext = BeamContext.Default;
    await beamContext.OnReady;
}
```

In this example we output the PlayerId to the console, which you can use to look up the Player in [Portal](https://docs.beamable.com/docs/portal).

```csharp
Debug.Log($"User Id: {_beamContext.PlayerId}");
```

By default, Beamable’s SDK always ensures there is a player token loaded, which means you will always have a unique user account that is anonymous. From here you can then use other forms of account linking/account creation such as Username & Password or Social Logins like Facebook (aka LoginThirdParty).

Not all games require authentication to be visible to get into the game. As such it is common practice to have frictionless login and the above shows you just how to do that.

Observe the classic flow of frictionless authentication.

![Frictionless Guide](../../../../../media/imgs/3e1d303-583b4d1-frictionless_auth.png)

You can _always_ prompt the user to authenticate another way once the above step has been established. In fact just using the Login Prefab does the above process and then allows you to set a Display Name (alias) for the anonymous user.

![Beamable Auth Show Login](../../../../../media/imgs/faeb11a-2039d7c-beamable_auth_showlogin.png)

# Sample Code

Below is the easiest and quickest way to provide authentication with Beamable. However, the following does not provide any cross-platform support. It will create a user and log them in with Beamable specifically for the current device.

The `PlayerAccount` contains the player's gamer tag, their alias, and any other third party credentials that may be associated with the player.

```csharp
using Beamable;
using Beamable.Player;

public class SilentLogin 
{
    private BeamContext _beamContext;
    public PlayerAccount account;

    private async void Start()
    {
        _beamContext = BeamContext.Default;
        await _beamContext.OnReady;
        await _beamContext.Accounts.OnReady;
        account = _beamContext.Accounts.Current;
    }
}
```