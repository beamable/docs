# Admin console

The Admin Console is a runtime overlay that lets developers and QA engineers run commands against a live Beamable game session without stopping play mode or redeploying. It renders an window over the scene and accepts typed commands, with autocomplete and history navigation built in.

![The Beamable Admin Console overlay rendered over a running game scene, showing a Console ready prompt above a command input line.](../../../media/imgs/admin-console.gif){width=800px}

As of this version, the Admin Console is a built-in integration managed directly by the Beamable runtime — no manual prefab setup is required. The previous prefab-based Admin Console is deprecated and will be removed in a future release. Migrate to the built-in integration described on this page.

!!! warning "Deprecated: prefab-based Admin Console"
    The old `AdminFlow` prefab approach is deprecated. Remove any existing AdminFlow prefabs from your scenes to start using the built-in integration.

## Activating the console

The console can be opened and closed several ways depending on the target platform and input configuration.

| Method | Details |
|--------|---------|
| Backtick / grave key (`` ` ``) | Default keyboard shortcut on all platforms |
| 3-finger swipe | Touch platforms — drag three fingers while they are all on screen |

## ConsoleConfiguration

`ConsoleConfiguration` is a Beamable module configuration ScriptableObject found alongside the other Beamable config assets in your project (under **Beamable** → **Resources** → **ConsoleConfiguration** in the Project window).

| Field                | Type    | Default | Description                                                                                                    |
|----------------------|---------|---------|----------------------------------------------------------------------------------------------------------------|
| `UI Size`            | `float` | `1.5`   | Configure the size of the UI                                                                                   |
| `EnableAdminConsole` | `bool`  | `true`  | Enables the console overlay in non-editor builds for all players, bypassing the `cli:console` scope requirement |

!!! note "Deprecated fields"
    `ForceEnabled` and `ToggleAction` are still present in the asset but only apply to the old prefab-based Admin Console. They have no effect on the built-in integration and can be ignored.

!!! tip
    Set `EnableAdminConsole` to `false` before shipping a player-facing build to ensure the console cannot be opened without the `cli:console` scope.

## Access control

| Environment | Behavior |
|-------------|---------|
| Unity Editor | Always enabled |
| Runtime build | Requires `ConsoleConfiguration.EnableAdminConsole = true` **or** the logged-in player must have the `cli:console` scope |

Players without the `cli:console` scope will not be able to open the console even if they trigger the correct gesture or key.

## Keyboard shortcuts

Once the console overlay is open, the following shortcuts are active:

| Key | Action                                                                                |
|-----|---------------------------------------------------------------------------------------|
| `Enter` / `Return` | Submit the current input                                                              |
| `Tab` | Accept the current autocomplete suggestion; press again to cycle through matches |
| `↑` / `↓` | Navigate command history                                                              |

## Running commands

Type a command and press `Enter`. The console echoes the command prefixed with `>` and runs it. Status messages appear in the Admin Console output, but a command's detailed result may be written to the Unity Console log instead, depending on how the command logs.

Example:
```text
> account_list
```

## Listing all Commands

Use the `help` command to list every registered command and its usage:

```text
> help
```

## Built-in commands

Beamable registers these commands by default:

| Command                                         | Detail                                                                                                              |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| `help`                                          | Show the list of all admin commands                                                                                 |
| `TRACK_PAYMENT`                                 | Track a test payment audit                                                                                          |
| `ECHO <message>`                                | Repeat a message to the console                                                                                     |
| `WHERE <command>`                               | Find where a console command was registered from, if it was registered with a `BeamableConsoleCommand` attribute    |
| `account_toggle`                                | Emit an account management toggle event                                                                            |
| `account_list`                                  | List user data                                                                                                     |
| `IDFA`                                          | Print the advertising identifier                                                                                   |
| `RESET`                                         | Clear the access token and start with a fresh account                                                              |
| `LOCALNOTE [<delay> [<title> [<body>]]]`        | Send a local notification (default delay is 10 seconds)                                                            |
| `TIMESCALE <value> \| variable`                 | Set the current timescale                                                                                          |
| `SUBSCRIBER_DETAILS`                            | Query subscriber details                                                                                           |
| `DBID`                                          | Show the current player's PlayerId                                                                                 |
| `ENTITLEMENTS <symbol> <state>`                 | Show the current player's entitlements                                                                             |
| `HEARTBEAT <dbid>`                              | Get the heartbeat of a user                                                                                        |
| `LOGIN_ACCOUNT <email> <password>`              | Log in to the PlayerId designated by the given username and password                                               |
| `MAIL_GET <category>`                           | Get mailbox messages                                                                                               |
| `MAIL_UPDATE <id> <state> <acceptAttachments>`  | Update a mail                                                                                                      |
| `REGISTER_ACCOUNT <email> <password>`           | Register this PlayerId with the given username and password                                                        |
| `EXPIRE_TOKEN`                                  | Expire the current access token to trigger the refresh flow                                                        |
| `CORRUPT_TOKEN`                                 | Corrupt the current access token to trigger the refresh flow                                                       |
| `TEST-ANALYTICS`                                | Run 1000 events to test batching and load                                                                          |
| `IAP_BUY <listing> <sku>`                       | Invoke the real-money transaction flow to purchase the given item                                                  |
| `IAP_PENDING`                                   | Display pending transactions                                                                                       |

## Custom commands

You can register your own commands to extend the console. Annotate a class with `[BeamableConsoleCommandProvider]` and each command method with `[BeamableConsoleCommand]`:

CustomConsoleCommandExample.cs
```csharp
using Beamable.ConsoleCommands;
using UnityEngine;

namespace Beamable.Examples.AdminConsole
{
    [BeamableConsoleCommandProvider]
    public class CustomConsoleCommandProvider
    {
        [BeamableConsoleCommand("Add", "A sample addition command", "Add <int> <int>")]
        public string Add(string[] args)
        {
            var a = int.Parse(args[0]);
            var b = int.Parse(args[1]);
            return "Result: " + (a + b);
        }
    }

    /// <summary>
    /// Demonstrates a custom <see cref="BeamableAdminConsole"/> command.
    /// </summary>
    public class CustomConsoleCommandExample : MonoBehaviour
    {
        //  Unity Methods  --------------------------------
        protected void Start()
        {
            Debug.Log($"Start() Instructions...\n" +
                      " * Run the scene\n" +
                      " * Type '~' in the Unity Game window to open the Admin Console\n" +
                      " * Type 'Add 5 10'\n" +
                      " * See 'Result: 15' in the Unity Console window\n");
        }
    }
}
```

## Logging to the console

Any script can write lines to the console output by calling `Log` on the singleton instance:

```csharp
BeamableAdminConsole.Instance.Log("Inventory refreshed.");
```

## API reference

### Instance

```csharp
public static BeamableAdminConsole Instance { get; private set; }
```

Singleton reference set during `InitializeConsole`. Use this to call `Log`, check state, or subscribe to events from anywhere in your code without holding a direct reference to the component.

### IsActive

```csharp
public bool IsActive { get; }
```

`true` while the console overlay is visible on screen. Use this to pause game input or suppress UI interactions that should not fire while the console is open.

### IsInitialized

```csharp
public bool IsInitialized { get; }
```

`true` after `InitializeConsole` has completed successfully. Calls to `Log` or `Instance` before initialization are safe but will have no visible effect until the console is ready.

### OnLogLine

```csharp
public event Action<string> OnLogLine;
```

Fired each time a line is appended to the console output, whether from a command result, a `Log` call, or internal console messages. Subscribe to forward output to an external logger or display it in a custom UI:

```csharp
BeamableAdminConsole.Instance.OnLogLine += line => MyLogger.Write(line);
```