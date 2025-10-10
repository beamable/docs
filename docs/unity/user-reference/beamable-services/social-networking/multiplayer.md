# Multiplayer

The Beamable Multiplayer feature allows game makers to create real-time and turn-based multi-user game experiences. 

**What is a game server?** A game **server** is the source of event coordination in a multiplayer video game. The server transmits enough events about its internal state to allow each connected **client** to maintain their own accurate version of the game. Events may contain various types of information including; properties about the game world, the players, and player input. See [Wikipedia](https://en.wikipedia.org/wiki/Game_server) for more info.

## Game Servers

Here are the leading options;

**Dedicated Server** 

- The server processes game-specific logic. The server **is** the game.
- Ideal For: Persistent world games, MMOs, and first-person shooters.

**Peer-To-Peer Server** 

- The server introduces client to client. Key communication passes directly from client to client. 
- Ideal For: First-person shooters and games that can tolerate cheating.

**Relay Server** 

- The server sends and receives events _between_ all clients in a match. The match is the "Room" in which all the game players interact. Each client **is** the game.
- Ideal For: Real-time strategy, tower defense, MOBAs, card battlers, auto chess, and more...

_Here is a comparison of various game servers;_ 

| Default Benefits                              | Relay Server     | Dedicated Server          | Peer-To-Peer Server    |
| :-------------------------------------------- | :--------------- | :------------------------ | :--------------------- |
| Lower Bandwidth                               | ✔️               | ❌    | ❌ |
| Simpler Server Infrastructure & Simpler Setup | ✔️               | ❌    | ❌ |
| Client-Authoritative                          | ✔️               | ❌    | ✔️                     |
| Lower Cost                                    | ✔️               | ❌    | ❌ |
| Higher Security                               | ✔️ (Determinism) | ✔️ (Server-Authoritative) | ❌ |
| Lower Latency                                 | ✔️               | ✔️                        | ✔️                     |

## Beamable Multiplayer

The Beamable Multiplayer API is lean and straightforward to setup. The pipeline and workflow for development are ready out-of-the-box on day 1 of development, allowing game makers to focus on game-specific client logic.

> Beamable Multiplayer uses relay server technology for rapid game development.

Beamable's Multiplayer is a **relay server**. This means that Beamable keeps a list of all events sent from all clients in a given match. Then, via push or pull, each client can ask "for all events since last time I asked". The clients then MUST advance the game play deterministically, replaying each player's input, so each client is in sync.

Plus, with Beamable Multiplayer, the game logic can access the full suite of Beamable functionality including [Inventory](../game-economy/inventory-overview.md), [Cloud Save](../profile-storage/cloud-save.md), and more!

here is a high-level diagram of the Beamable Multiplayer terms

| Name | Detail |
|------|--------|
| Client | This refers to the instance of the game code that is running on each player's local device (e.g. Mobile Phone) |
| Event | The data packet that represents a player's turn in the game. This may be any serializable C# structure. |
| Latency | This measurement indicates the average total time needed for the game **client** to send an event to the Multiplayer **server** and receive the reply. Latency is measured in milliseconds (e.g. 200ms) |
| Matchmaking | This is the process of choosing a `MatchId` based on criteria. E.g. "Give me a match to play in with 3 total players with beginner skill level". Beamable includes an optional, light-weight Matchmaking service.<br><br>_Note: See [Matchmaking](matchmaking.md) for more info_ |
| SimClient | This class is the main entry point for Beamable's Multiplayer feature. |
| SimClient's TargetNetworkLead | This is network buffer. It represents how long the Multiplayer **server** holds game **events** before sending them back to clients. E.g. With a value of 5, the Multiplayer **server** will hold 5 events before sending those 5 to the game client's. A higher value provides more consistency to the **clients'** rendering experience, but at the cost of higher latency. |
| SimClient's Match | This represents a set of players playing a specific instance of the game together. Only players in the **same** match may collaborate, compete, and communicate. |
| SimClient's FramesPerSecond | This is the rate (in times per second) at which the **client** receives event updates from the Multiplayer **server**. As a data optimization, typically this is set lower than the rendering frame rate of Unity. |
| Server | This refers to the instance of the server code that sits between the game's **clients** and manages distribution of the game events. |

### Game Security

To be more secure against any malicious hackers in your multiplayer game's community, consider never sending any game object state (player's heath, power of weapon, etc) as part of the messages to be synchronized over the network. 

Any enterprising hacker can "easily" hack a game client to send inflated values which will only make the game worse for everyone. If all a player can do is send an "action". i.e. "What I did" ("I fired my equipped gun" rather than "I hit player 2 for 100 damage"), it becomes quite a bit harder for someone to cheat. 

A hacker may also attempt to replay actions AGAIN for a particular turn or to send malformed game event object messages that can lead to a worst experience for other players.

### Matchmaking

In multiplayer gaming, matchmaking is the process of choosing a `MatchId` based on criteria (e.g. "Give me a match to play in with 2 total players of any skill level"). Beamable supports matchmaking through its matchmaking service.

See [Matchmaking](matchmaking.md) for more info.

### Playing "Against Yourself"

One of the challenges of developing a multiplayer game is testing it frequently as an individual developer. Finding a friend to play against you **every** time you run the game in development is prohibitive. 

Here are 2 strategies to help the development process.

#### Adding a Bot

The sample game includes an optional bot opponent. This is an AI that plays against you. Simply click "Start Game: Human vs Bot" from the Menu Scene to activate it. Architecturally this is similar to the full game and it fully uses the Beamable Multiplayer event objects for each player move. However, it requires only one human player. 

#### Playing Against Yourself

The sample game allows a workflow to test the full 2 player experience with relative ease. Build the Unity sample project as a standalone game for either Mac or PC. Then run the game in the Unity Editor **also**. Simply click "Start Game: Human vs Human" from the Menu Scene in **both** game clients to activate it. 

Doing a build takes a few minutes. Depending on the specifics of your game, it may not be required to rebuild the standalone after **every** code change.

This is the process of choosing a `MatchId` based on criteria. E.g. "Give me a match to play in with 3 total players with beginner skill level". Beamable includes an optional, light-weight Matchmaking service.

### Randomization and Determinism

In single-player game design, game makers may freely use randomization libraries to add variety to game play. The environment may be randomized, the enemy amount and variety can change every game session. This adds richness and replayability to the game.

In a multiplayer game its important that all players in a given game session have the SAME "random" experience. But how?

Randomization is supported by Beamable's Multiplayer with the following advice. During initialization the Beamable `SimClient` will pass along the same seed value to feed the random operations on each client. By using the same seed, each game client will be in-sync.

## Multiplayer API

Here is the **High-level Sequence for Beamable Multiplayer**.

!!! danger "Experimental API"

    This API is experimental and may change in future versions.

### Creating Multiplayer Session
Each game client connects this way. No one client has special status of 'host'. Depending on the needs of the game, the `SimClient` session may stay from the moment any one player joins until the moment the last player leaves.

```csharp
_simClient = new SimClient(new SimNetworkEventStream(MatchId, BeamContext.Default.ServiceProvider), FramesPerSecond, TargetNetworkLead);
```

**Create Custom Event **  
Depending on the complexity of the game play, there may be dozens of custom events.

```csharp
public class MyPlayerMoveEvent
{
     public Vector3 Position;
     public MyPlayerMoveEvent(Vector3 position)
     {
          Position = position;
     }
}
```

### Subscribing To Events
The client must repeat this for **each** PlayerId of interest.

```csharp
_simClient.On<MyPlayerMoveEvent>(MyPlayerMoveEvent.Name, _localPlayerDbid.ToString(),
     SimClient_OnMyPlayerMoveEvent);
```

### Sending Events  
Typically each player's input is converted into an event.

```csharp
_simClient.SendEvent(MyPlayerMoveEvent.Name,
     new MyPlayerMoveEvent(_localPlayerDbid, new Vector3(0, 0, 0)));
```

### Handling Event 
Typically for a fair and consistent game play experience, best practices dictate that all events, even the local clients own player's events are sent to the server, later received, and then converted to rendered graphics and sounds. This way the requisite latency is the same for the local client as it is for all other clients in the same match.

```csharp
private void SimClient_OnMyPlayerMoveEvent(MyPlayerMoveEvent myPlayerMoveEvent)
{
     Debug.Log($"The player moved to the position of {myPlayerMoveEvent.Position}.");
}
```

### Handling Network Faults

It is possible that temporary network outages may occur. While these errors are occurring, player communication with the Beamable Game Relay is blocked, and no messages will be sent or received. When network connectivity resumes, the session will resume sending and receiving events.

Errors can be caught using callbacks available on the `SimClient` instance. When a network outage event occurs, the `OnErrorStarted` event will always trigger first. Later, when the outage has recovered, the `OnErrorRecovered` event will trigger. However, if the outage is too long, or if there is a different unrecoverable error, the `OnErrorFailed` event will trigger.

```csharp
// client is a SimClient instance

client.OnErrorStarted += (e) =>
{
    // TODO: show "connecting to server error message"
    Debug.Log($"Sim Client Errors Starting... {r.ErrorMessage}");
};
client.OnErrorRecovered += (r) =>
{
    // TODO: remove any error UI and resume the game
    Debug.Log($"Sim Client disaster averted... ");
};
client.OnErrorFailed += r =>
{
    // TODO: force exit the match, because the network is too unstable to continue or recover.
    Debug.Log($"Sim Client wasn't able to recover. {r.ErrorMessage}" );
};
```

The effect of `OnErrorFailed` event can also be captured by using a `try/catch` around the `SimClient.Update` function, like so...

```csharp
try
{
    client.Update();
}
catch (SimNetworkErrorException ex)
{
    // TODO: destroy the client- start over.
    Debug.LogException(ex);
}
```

In the event that a network outage is unrecoverable, the entire `SimNetworkEventStream` instance needs to be reconstructed. Any further calls to `SimClient.Update` will re-throw the `SimNetworkErrorException`.

#### Custom Fault Tolerance

It is possible to inject custom network outage fault tolerance logic. Use [Custom Dependency Injection](../../runtime-systems/dependency-injection/di-custom-services.md) to inject a new instance of `ISimFaultHandler`, or pass in a custom instance of `ISimFaultHandler` as an optional parameter to the `SimNetworkEventStream`.

The default implementation of the `ISimFaultHandler` is the `DefaultSimFaultHandler`.

!!! info "Change Default Fault Tolerance Duration"

    By default, the `DefaultSimFaultHandler` instance will allow for 15 seconds of network outage before reporting an unrecoverable error. This duration can be adjusted by passing in a custom instance of the `DefaultSimFaultHandler` to the `SimNetworkEventStream`.

    ```csharp
    var stream = new SimNetworkEventStream(roomId, ctx.ServiceProvider, new DefaultSimFaultHandler
    {
        // use a 4 second duration instead of 15.
        MaxFaultyDurationInSeconds = 4
    });
    ```

### Sample Code
Here is a complete Beamable Multiplayer example which creates a game session and sends/receives game events.

MultiplayerExample.cs
```csharp
using System.Collections.Generic;
using Beamable.Experimental.Api.Sim;
using UnityEngine;
using UnityEngine.Events;

namespace Beamable.Examples.Services.Multiplayer
{
   [System.Serializable]
   public class MultiplayerExampleDataEvent : UnityEvent<MultiplayerExampleData> { }

   public enum SessionState
   {
      None,
      Initializing,
      Initialized,
      Connected,
      Disconnected
   }
   
   /// <summary>
   /// Holds data for use in the <see cref="MultiplayerExample"/>.
   /// </summary>
   [System.Serializable]
   public class MultiplayerExampleData
   {
      public string MatchId = null;
      public string SessionSeed;
      public long CurrentFrame;
      public long LocalPlayerDbid;
      public bool IsSessionConnected { get { return SessionState == SessionState.Connected; }}
      public SessionState SessionState = SessionState.None;
      public List<string> PlayerMoveLogs = new List<string>();
      public List<string> PlayerDbids = new List<string>();
   }
   
   /// <summary>
   /// Defines a simple type of in-game "move" sent by a player
   /// </summary>
   public class MyPlayerMoveEvent
   {
      public static string Name = "MyPlayerMoveEvent";
      public long PlayerDbid;
      public Vector3 Position;

      public MyPlayerMoveEvent(long playerDbid, Vector3 position)
      {
         PlayerDbid = playerDbid;
         Position = position;
      }

      public override string ToString()
      {
         return $"[MyPlayerMoveEvent({Position})]";
      }
   }
   
    /// <summary>
    /// Demonstrates <see cref="SimClient"/>.
    /// </summary>
    public class MultiplayerExample : MonoBehaviour
    {
       //  Events  ---------------------------------------
       [HideInInspector]
       public MultiplayerExampleDataEvent OnRefreshed = new MultiplayerExampleDataEvent();
       
        //  Fields  ---------------------------------------
       
        private MultiplayerExampleData _multiplayerExampleData = new MultiplayerExampleData();
        private const long FramesPerSecond = 20;
        private const long TargetNetworkLead = 4;
        private SimClient _simClient;
        private BeamContext _beamContext;
        
        //  Unity Methods  --------------------------------
        protected void Start()
        {
           Debug.Log($"Start() Instructions...\n\n" + 
                     " * Run The Scene\n" + 
                     " * Press 'Start Multiplayer'\n" + 
                     " * Press 'Send Player Move'\n" + 
                     " * See results in the in-game UI\n");

            SetupBeamable();
        }
        
        
        protected void Update()
        {
           if (_simClient != null) 
           { 
              _simClient.Update(); 
           }

           string refreshString = "";
           refreshString += $"MatchId: {_multiplayerExampleData.MatchId}\n";
           refreshString += $"Seed: {_multiplayerExampleData.SessionSeed}\n";
           refreshString += $"Frame: {_multiplayerExampleData.CurrentFrame}\n";
           refreshString += $"Dbids:";
           foreach (var dbid in _multiplayerExampleData.PlayerDbids)
           {
              refreshString += $"{dbid},";
           }

           //Debug.Log($"message:{refreshString}");
        }

        
        protected void OnDestroy()
        {
           if (_simClient != null)
           {
              StopMultiplayer();
           }
        }
        
        
        //  Methods  --------------------------------------
        private async void SetupBeamable()
        {
           _beamContext = BeamContext.Default;
           await _beamContext.OnReady;

            Debug.Log($"_beamContext.PlayerId = {_beamContext.PlayerId}");
            
            // Access Local Player Information
            _multiplayerExampleData.LocalPlayerDbid = _beamContext.PlayerId;

        }
        
        public void StartMultiplayer()
        {
           if (_simClient != null)
           {
              StopMultiplayer();
           }
           
           _multiplayerExampleData.SessionState = SessionState.Initializing;
           Refresh();
           
           // Generates a specific MatchId
           // (Otherwise use Beamable's MatchmakingService)
           _multiplayerExampleData.MatchId = "MyCustomMatchId_" + UnityEngine.Random.Range(0,99999);
           
           // Create Multiplayer Session
           _simClient = new SimClient(
              new SimNetworkEventStream(_multiplayerExampleData.MatchId, _beamContext.ServiceProvider), 
              FramesPerSecond, TargetNetworkLead);
        
           // Handle Common Events
           _simClient.OnInit(SimClient_OnInit);
           _simClient.OnConnect(SimClient_OnConnect);
           _simClient.OnDisconnect(SimClient_OnDisconnect);
           _simClient.OnTick(SimClient_OnTick);
        }

        public void StopMultiplayer()
        {
           if (_simClient != null)
           {
              // TODO: Manually Disconnect/close?
              _simClient = null;
           }

           _multiplayerExampleData.SessionState = SessionState.Disconnected;
           Refresh();
        }

        public void SendPlayerMoveButton()
        {
           if (_simClient == null)
           {
              return;
           }
           
           // Create a mock  player position
           Vector3 position = new Vector3(
              Random.Range(1, 10),
              Random.Range(1, 10),
              Random.Range(1, 10)
              );
           
           _simClient.SendEvent(MyPlayerMoveEvent.Name,
              new MyPlayerMoveEvent(_multiplayerExampleData.LocalPlayerDbid, position));
        }
        
        public void Refresh()
        {
           string refreshLog = $"Refresh() ...\n" +
                               $"\n * LocalPlayerDbid = {_multiplayerExampleData.LocalPlayerDbid}\n\n" +
                               $"\n * PlayerDbids.Count = {_multiplayerExampleData.PlayerDbids.Count}\n\n" +
                               $"\n * PlayerMoveLogs.Count = {_multiplayerExampleData.PlayerMoveLogs.Count}\n\n";
            
           //Debug.Log(refreshLog);

           OnRefreshed?.Invoke(_multiplayerExampleData);
        }

        
        //  Event Handlers  -------------------------------
        private void SimClient_OnInit(string sessionSeed)
        {
           _multiplayerExampleData.SessionState = SessionState.Initialized;
           _multiplayerExampleData.SessionSeed = sessionSeed;
           Refresh();
           
           Debug.Log($"SimClient_OnInit()...\n" + 
                     $"MatchId = {_multiplayerExampleData.MatchId}, " +
                     $"sessionSeed = {sessionSeed}");
        }

        
        private void SimClient_OnConnect(string dbid)
        {
           _multiplayerExampleData.SessionState = SessionState.Connected;
           _multiplayerExampleData.PlayerDbids.Add(dbid);
           Refresh();
        
           // Handle Custom Events for EACH dbid
           _simClient.On<MyPlayerMoveEvent>(MyPlayerMoveEvent.Name, dbid,
              SimClient_OnMyPlayerMoveEvent);
        
           Debug.Log($"SimClient_OnConnect() dbid = {dbid}");
        }

        
        private void SimClient_OnDisconnect(string dbid)
        {
           if (long.Parse(dbid) == _multiplayerExampleData.LocalPlayerDbid)
           {
              StopMultiplayer();
           }
           
           _multiplayerExampleData.PlayerDbids.Remove(dbid);
           Refresh();
           
           Debug.Log($"SimClient_OnDisconnect() dbid = {dbid}");
        }

        
        private void SimClient_OnTick(long currentFrame)
        {
           _multiplayerExampleData.CurrentFrame = currentFrame;
           Refresh();
        }

        
        private void SimClient_OnMyPlayerMoveEvent(MyPlayerMoveEvent myPlayerMoveEvent)
        {
           string playerMoveLog = $"{myPlayerMoveEvent}";
           _multiplayerExampleData.PlayerMoveLogs.Add(playerMoveLog);
           Refresh();
        }
    }
}
```