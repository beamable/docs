# Lobby
Beamable's Lobby system can be used primarily for 2 cases:

- **Open/Closed Custom Lobbies/Rooms**: Player-created custom rooms for room-based games
- **Resulting Matchmaking Matches**: Matchmaking queues output lobbies with players in them at each matchmaking queue. See more in [Matchmaking](../features/matchmaking.md).

Conceptually, Lobbies are room containing only online players and a set of arbitrary room properties and player properties. There are a few rules you should be aware off:

- Each Non-Matchmaking Lobby has a **Host** and other Players.
- Becoming offline will remove you from the lobby (after a small delay).
- The host player becoming offline will disband a lobby (after a small delay).
- The host player can edit global properties and any other player's properties.
- The host player can kick other players whereas regular players can only leave themselves.
- Players can **read** the entire lobby data but only **write** to their own state.
- Matchmaking Result Lobbies have no host; instead they disband once every player is offline.

