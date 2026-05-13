# Lower-level SDK

This section talks about lower-level details of how requests to Beamable get made. ***You don't need to read this***, but... you might want to if you plan on implementing your own `UBeamRuntimeSubsystem`.

Here's why you'd want to do this:

- You want to replace one of the SDK's implementations with something custom and want to provide guarantees about your system's lifecycle that are similar to those the SDK provides.
- You wish to guarantee that when any `Login / Signup` Operation's success is triggered, you'll already have access to custom data fetched via Microservices and MicroStorages.

Unless you are solving one of the two problems above, you will not need to write your own `UBeamRuntimeSubsystem`. If you do, the following concepts are essential.

!!! warning "Low Level Usage"
    The systems described here are used by various environments the Beamable SDK runs in: PIE, Editor, Dedicated Server Builds and regular game builds. Their code is pretty heavily commented, so feel free to read it and figure things out that way.

The lowest layer of systems is shared between the SDK's UE Editor integration and the SDK's Runtime integration:

- `UBeamUserSlots`: [User Slots](user-slots.md) tracks multiple local signed-in users (for local co-op cases).
    - This is basically a local user cache that is aware of the peculiarities of PIE.<br><br>

- `UBeamRequestTracker`: provides BP-compatible async operations that emit various events as they go along.
    - You can think of these as "BP-Compatible Promises".
    - These are integrated with the `UBeam____Api` subsystems.
    - `BeginOperation` is effectively the same a creating a new promise.
    - `TriggerOperationSuccess`, `TriggerOperationError` and `TriggerOperationCancelled` should be called when you want to complete the Operation.
    - This is a somewhat complex subsystem so read [Operations and Waits](operations-and-waits.md) for more details.<br><br>

- `UBeam_____Api`: Code-Generated Subsystems from the Beamable Backend OpenAPI spec.
    - These are stateless `UEngineSubsystem` implementations.
    - These provide you low-level access to every end-point of the Beamable backend even if the SDK does not include utilities that do exactly what you want.
    - As UE doesn't allow for namespaces AND BP-compatibility, this is _very_ verbose. Prefer more liberal use of `auto` when dealing with Code-Gen API Types.
    - At runtime, don't forget to pass in the `UObject* CallingContext` parameter: any `UWorld`, `UGameInstanceSubsystem`, `UActorComponent` or `AActor` will do (this ensures proper behavior in all cases of PIE).<br><br>

- `UBeamBackend`, `UBeamNotifications` and `UBeam_____Notifications` are discussed in the sections below.

## `UBeamBackend`
`UBeamBackend` is the most important `UEngineSubsystem` in the SDK. It uses Unreal's `HTTP` module to make requests to the configured Beamable backend. It contains the implementations used by the `UBeam____Api` classes to make the actual requests.

These implementations handle:

- Request/Response serialization and deserialization.
- Configurable Retry Logic with per-request-type, per-user-slot and per-call-site granularity.
- Request's response caching, though this is disabled by default as caching is a very context dependent endeavor.
- Transparent and Automatic Re-Auth in case of expired `AccessToken` through a user's `RefreshToken`.

The SDK provides a few different request types with 4 implementations:

- **CPP and BP Authenticated Requests**: require an `FUserSlot` with a logged-in user whose access token is used to make the request.
- **CPP and BP Non-Authenticated Requests**: does not require an `FUserSlot` with a logged-in user.
- **`UBeamBackend::CreateGenericBeamRequest`**: for making requests to non-Beamable servers by `UBeamGenericApi`.

In addition to these implementations, the SDK also provides a hierarchy of retry configurations. You can configure these in `UBeamCoreSettings` (`Project Settings -> Beamable Core`). Retries happen automatically on timeouts and a few other known cases.

By default, these are if:

- The `FBeamErrorResponse` structure received is a `408` status.
    - The Unreal HTTP Requests returning a `EHttpFailureReason::ConnectionError` or `EHttpFailureReason::TimedOut` are parsed into `FBeamErrorResponse` with a `408`.<br><br>

- Received any error defined in `UBeamBackend::AUTH_ERROR_CODE_RETRY_ALLOWED`.
    - These errors trigger the SDK's authentication token refresh flow. It will refresh the token and then retry the request.

If you ever encounter issues with this system, `log LogBeamBackend Verbose` is a useful Unreal command that can be used as a diagnostic tool. It will print out the entire process of building the request, sending it out, and receiving its response.

!!! note "Connectivity"
    The Beamable SDK does not handle the concept of "player connectivity to the internet" via request/response heuristics. See `UBeamNotifications` below and [Connectivity](connectivity.md) for more information.

## `UBeamNotifications`

Every connected Beamable player maintains a WebSocket connection to Beamable while they are logged-in. This system uses UE's `WebSocket` module to open web-socket connections for each logged-in user (using `FUserSlot`).

This WebSocket connection semantically represents the connectivity status for that particular user. This means the SDK (and the Beamable Servers) think that a user is online/offline based on whether this connection is alive and well. Which in turn means that, if you want to use any of the SDK's real-time services ([Matchmaking](../beamable-services/matchmaking.md), [Lobbies](../beamable-services/lobbies.md), etc.) this connection needs to be properly working. At runtime, `UBeamRuntime`, and `UBeamConnectivityManager` handle per-`FUserSlot` [Connectivity](connectivity.md) statuses.

Aside from defining [Connectivity](connectivity.md) semantics, this connection is also how the Beamable servers (or your own custom Microservices) send notifications to clients about certain events.

For example:

- Implementations of `UEngineSubsystem` called `UBeam_____Notifications` exist for each of the Beamable Services that emit notifications.
    - These expose two UE function versions, one BP-Compatible and the other Lambda-Compatible, that register a handler to process a specific type of notification.<br><br>

- These are used by that service's `UBeamRuntimeSubsystem` based on their semantic needs.
    - For example, `UBeamMatchmakingNotifications` subscribes to notifications for the matchmaking ticket while a `FUserSlot` is on a given queue.<br><br>

- You can use Microservices to send out custom notifications — those can be received in clients by creating your own subsystem modeled after these.
    - Use `UBeamRuntime::SubscribeToCustomNotification` to subscribe to these easily at runtime.

