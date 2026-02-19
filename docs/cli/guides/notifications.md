# Notifications

## Listening for Notifications

Beamable provides several player facing and game facing callbacks via WebSockets. The Unity SDK relies on these WebSockets events to manage state and run C# callbacks within the SDK. The CLI provides two useful commands to monitor these WebSockets events, one for [player events](../commands/cli-command-reference/listen/player.md) and a second for [game events](../commands/cli-command-reference/listen/server.md).

**IMPORTANT**: these commands are meant as diagnostic tools, and should not be used as critical components in a game's architecture. Neither command has robust reconnection logic, and if the socket is closed due to ephemeral network failure, it will not re-open automatically.
