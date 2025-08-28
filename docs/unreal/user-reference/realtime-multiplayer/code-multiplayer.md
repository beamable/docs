# C++ Realtime Multiplayer Systems
In Unreal, there are certain parts of implementing a dedicated server game that MUST be implemented using C++. Namely, **Game Server Authentication**. This means: implementing logic that your Game Server runs to decide whether an incoming connection is allowed in this game server or not.

By default, Beamable's integrates with the Gameplay Framework to give you cross-platform Game Server Authentication (to enable cross-play) WITHOUT going through OnlineSubsystem interfaces. Basically, the `FUniqueNetId` for each player is the user's `GamerTag`. More details about disabling this further down in this document (not recommended).

There are a few components here that you need to know about before you implement this:

- **AGameMode::BeginPlay**: In most Cpp-based implementations, this is your server's "entry point". 
- **AGameMode::PreLoginAsync**: This is what UE calls whenever a client attempts to connect to a game server --- once you invoke a callback it provides, the user is either accepted or rejected. This will be invoked on the server once per-player (if you have multiple players per-client, this is an important distinction).
- **ULocalPlayer::GetGameLoginOptions**: This appends a string of Options to each `ULocalPlayer`'s connection string.
- **FUniqueNetIdRepl**: This is how UE's Gameplay Framework identifies each player in the network and the basis for Beamable's SDK integration with UE Gameplay Framework.

### Setting Up your Gameplay Level's Level Blueprint
This section is the C++ version of [what is done in the Level Blueprint here](realtime-multiplayer-overview.md#setting-up-your-gameplay-levels-level-blueprint).

In C++, this would usually be done in `AGameMode::BeginPlay` and would look something like this.

```c++
virtual void BeginPlay() override
{
    // This will run once the Beamable SDK is initialized (which you can call here OR in a blueprint)
    const auto BeamRuntime = GetGameInstance()->GetSubsystem<UBeamRuntime>();
    BeamRuntime->CPP_RegisterOnStarted(FBeamRuntimeHandlerCode::CreateLambda([this]()
    {
        UE_LOG(LogTemp, Warning, TEXT("Started!"));
        // If we need to set up our orchestrator... 
        if (BeamPIE::Orchestrator::ShouldRegisterOrchestrator(this))
        {            
            UE_LOG(LogTemp, Warning, TEXT("Setting up my orchestrator!!!!"));
	

            // Let's extract the Lobby Id from the CLArgs.
            const auto LobbyId = BeamMultiplayer::Orchestrator::GetLobbyIdFromCLArgs(this);

            // Let's call RegisterLobbyWithServer so that the SDK running here becomes aware of this lobby.             
            BeamMultiplayer::Orchestrator::RegisterLobbyWithServer(this, LobbyId, FBeamOperationEventHandlerCode::CreateLambda([this, LobbyId](FBeamOperationEvent Evt)
            {
                // Failed to get lobby data from Beamable
                // Game-Dependent: Handle error by telling Orchestrator to kill the room maybe? 
                if (Evt.CompletedWithError()) return;
	
                // Got the lobby data from Beamable
                // Game-Dependent: Handle success by doing preloading of data based on the lobby 
                if (Evt.CompletedWithSuccess())
                {
                    const auto Lobbies = GetGameInstance()->GetSubsystem<UBeamLobbySubsystem>();
                    ULobby* Lobby;
                    if (Lobbies->TryGetLobbyById(LobbyId, Lobby))
                    {
                        // Game-Dependent: Use data in the lobby to load things.
                        
                        // Once you are done loading things and preparing the lobby, call this to let clients begin connecting to the server.
                        // Only after this call succeeds does the Federation notify users that the match was found --- this means that PreLoginAsync is guaranteed to have the lobby data at that point.
                        BeamMultiplayer::Orchestrator::NotifyLobbyReady(this, LobbyId, FBeamOperationEventHandlerCode::CreateLambda([](FBeamOperationEvent Evt)
                        {
                            // Users will never receive the notification that a match was found, will timeout and get put back into the queue.
                            // Game-Dependent: Maybe kill the server so it doesn't linger?
                            if (Evt.CompletedWithError()) return;
	
                            // Users will start trying to connect soon (PreLoginAsync flow)
                            if (Evt.CompletedWithSuccess()) return;
                        }));
                    }
                    else
                    {
                        // Something went really wrong inside the Lobby Subsystem (report to Beamable)...
                    }
                }
            }));
        }
    }));
}
```

**The code above still expects you to have the `Easy Enable` node in your level blueprint marked with `Init when Server Build`.**

## Implementing Game Server Authentication
When using the Beamable SDK, in order to validate that the user should be allowed to connect to this game server, we need to know a few things:

- The User's Auth Token and GamerTag... so that the server can verify the user is who they say they are.
- Optionally, the Lobby Id for the lobby the user is in... so we can verify that the user is in a lobby registered with this Game Server.

We expect to receive these via the `Options` parameter. 

In clients builds', passing these options can be achieved using `UBeamLobbySubsystem::TryOpenLevelFromLobby`. You can also use `UBeamLobbySubsystem::PrepareLoginOptions` to append these to a string you'll pass to the regular `Open Level` calls used to connect to game servers.

When implementing `PreLoginAsync`, you need to call two functions:

- `BeamPIE::Authentication::GetExpectedClientPIEOptions` --- this enables our PIE integration to work with Game Server Authentication (it gets around UE limitations --- see further down for more information on this).
- `BeamMultiplayer::Authentication::PreLoginAsync` --- this uses the `Options` to validate the user is in-fact inside a lobby that has been registered with this server. 

A simple implementation of that looks like this:

```c++
virtual void PreLoginAsync(const FString& Options, const FString& Address, const FUniqueNetIdRepl& UniqueId, const FOnPreLoginCompleteDelegate& OnComplete) override
{
    // This enables us to test the Pre-Login in PIE correctly (it adds options in the expected deterministic order the PIE instances create and connect so that we can their users in order) 
    const auto BeamOptions = BeamPIE::Authentication::GetExpectedClientPIEOptions(this, Options, Address, UniqueId);

    // Validate that the user coming in is really one that exists in a lobby that has been BeamMultiplayer::Orchestrator::RegisterLobbyWithServer.
    // BeamPIE guarantee's that happens for the lobbies it creats for PIE use.
    BeamMultiplayer::Authentication::PreLoginAsync(this, BeamOptions, Address, UniqueId, FBeamOperationEventHandlerCode::CreateLambda([this, OnComplete, BeamOptions, Address, UniqueId](FBeamOperationEvent Evt)
    {
        if (Evt.CompletedWithSuccess())
        {            
            Super::PreLoginAsync(BeamOptions, Address, UniqueId, OnComplete);
        }

        // If failed, deny entry into the server by calling OnComplete with a non-Empty string.
        if (Evt.CompletedWithError())
        {
            OnComplete.ExecuteIfBound(Evt.EventCode);
        }
    }));
}
```

The `BeamMultiplayer::Authentication::PreLoginAsync` function runs an operation that, once completed successfully, informs you that we have validated the user is both who they say they are and are in the lobby they say they are. You can do game-specific logic here and combine it with our verification too.

If you have multiple players per-client, you should also implement a subclass of `ULocalPlayer` as such. This will guarantee the correct GamerTag for each `UserSlot` in that client is correctly forwarded when that particular Local Player tries to connect to the Game Server. You can then configure the Local Player class for your game in `Project Settings > Engine > General Settings > Default Classes > Local Player Class`.

```c++
/**
 * If you're game doesn't have multiple local players, this shouldn't be needed --- it doesn't hurt though.
 * It'll ensure each of the local players traveling together to the game server will forward their associated Beamable information as part of the options. 
 */
UCLASS()
class UMyGameLocalPlayer : public ULocalPlayer
{
	GENERATED_BODY()

public:
	virtual FString GetGameLoginOptions() const override
	{
		return BeamMultiplayer::LocalPlayer::GetGameLoginOptions(this, Super::GetGameLoginOptions());
	}
};
```

## Understanding `FUniqueNetId` and Beamable
`FUniqueNetId` is how UE identifies each player in the network. By default, when you sign in with Beamable, we set your `ULocalPlayer`'s preferred `FUniqueNetId` to be the user's `GamerTag`. This is how the Beamable SDK maps each Player in its `ULobby` objects to each **UE Player** objects. The `UBeamLobbySubsystem` has utility functions that help you get a `GamerTag` from a **Player Controller/State** object --- these rely on this mapping to work.

As long as you are using the `Project Settings > Game > Beamable Runtime > Enable Gameplay Framework Integration`, this is all handled automatically for you (in various ways). If, for whatever reason, you want the `FUniqueNetId` to be something other than the Beamable GamerTag, you **_MUST_** also implement Game Server Authentication for these utility functions to work.

This constraint exists because, for now, the logic in our `BeamMultiplayer::Authentication::PreLoginAsync` is the only place where we'll have both the `GamerTag` (from the `Options`) AND the `UniqueId` in order to map each player correctly.

**_Keep in mind that the default SDK behavior does not need you to care about any of this._**

## User Slots in the Game Server SDK
User Slots are a big part of the regular workflow when working with Beamable SDK in game clients. For dedicated servers though they are not used. Any functions containing the `UserSlot` parameter, that parameter can be ignored. 


This means a few things:

- There is no need to `SignUp`/`Login`; just to `InitSDK`.
- Calling APIs that simply read data from users via their `GamerTag` or other Ids will work fine.
- Calling APIs that write to user data is not recommended via regular SDK functions (see below for the alternative).

!!! note "Server Mapping Slots - Experimental"
     By default, if you are implementing the **Game Server Authentication** described here. The server stores the AuthToken for each user inside server mapping slots --- this means the Game Server _can_ make requests "as though they were the user itself" but with the Server's admin permissions. This can be useful due to certain legacy API limitations.

### Writing to a User's Stats/Inventory
When writing your Game Server code, you generally don't want to be making requests for individual players one at a time (batching is generally better). Sometimes that is fine, but there are cases where you'll want to write several things to several players's Stats/Inventory (processing a match's results, for example). In cases like this, you should write `ServerCallable` functions in Microservices and call those from the Microservice. See [Microservices](../microservices/microservices.md) for more information about the various types of `Callable`.

## Making Beam PIE Faster
Iteration time is one of the most important factors when developing a game. Because of that, we wanted you to be able to enter PIE as fast as UE allows us, but still have all the guarantees about Beamable. Unfortunately, that is not possible with Blueprints.

However, it is possible with a custom `GameInstance` implementation.

So, in order to enable you to take advantage of this, you can implement this snippet and configure your custom Game Instance class to be used in your `Project Settings > Project > Maps & Modes > Game Instance Class`.

```c++
/**
 * This is BeamPIE's advanced implementation.
 * It is MUCH faster than the Blueprint node version but... it is a little more complex in what it is doing under the hood.
 * It also does not require you to remove the Blueprint version --- you can leave both on.
 * As long as you are using your custom GameInstance class for your game that has these calls in it --- this version takes precedence over the BP version.
 */
UCLASS()
class UMyGameInstance : public UGameInstance
{
	GENERATED_BODY()

public:

	/**
	    This function is what executes when you are running PIE as separate processes (Standalone Game or running the dedicated server in a separate process). 
	*/    
	virtual void StartGameInstance() override
	{
		// This must be called BEFORE `Super::StartGameInstance()`
		BeamPIE::GameInstance::PreStartGameInstance(this);
		
		// Call the default GameInstance initialization
		Super::StartGameInstance();
		
		// This must be called AFTER `Super::StartGameInstance()`
		BeamPIE::GameInstance::StartGameInstance(this);
	}

#if WITH_EDITOR
	/**
	    This function is what executes when you are running PIE in the editor. 
	*/      
	virtual FGameInstancePIEResult StartPlayInEditorGameInstance(ULocalPlayer* LocalPlayer, const FGameInstancePIEParameters& Params) override
	{
		// This must be called BEFORE Super::StartPlayInEditorGameInstance(...)	
		BeamPIE::GameInstance::StartPlayInEditorGameInstance(this, LocalPlayer, Params);
		
		// Call the default StartPlayInEditorGameInstance implementation 
		return Super::StartPlayInEditorGameInstance(LocalPlayer, Params);
	}
#endif

	/**
	    For as long as you return `true` in this function, PIE Clients will wait before connecting to the game server. 
	    Our utility returns `true` until the Clients are fully initialized and inside BeamPIE's automatically created Lobby.   
	*/      
	virtual bool DelayPendingNetGameTravel() override
	{
		return BeamPIE::GameInstance::DelayPendingNetGameTravel(this);
	}
};
```

!!! note "Why do I have to write this code instead of inheriting from a class you give us?"
     The SDK's philosophy is one that tries **_not_** force you into situations where you cannot combine its utilities and your own project-specific ones. A common mistake in SDK design is to provide a base-class that users _must inherit_; while it does make the simplest case a little easier, it tends to make complex cases _significantly harder_ than they need to be.

    As such, we evaluate this cost is worth the flexibility.

**PLEASE REMEMBER: _In builds, all functions from the `BeamPIE` namespace are no-ops._**

