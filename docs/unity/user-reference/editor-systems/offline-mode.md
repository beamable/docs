# Offline Mode

## Overview

Beamable requires internet connectivity to offer its full suite of benefits. However, even offline, it has an appropriate subset of functionality.

The Connectivity feature drives the heartbeat sent back to the Beamable backend platform. If the game client loses connectivity, the heartbeat will stop and the Beamable API will gracefully wait for reconnection before resuming the full online feature-set.

## Feature Support

You can find below a table that summarizes the offline support for each Beamable feature.


| Feature | Support | Detail |
|---------|---------|--------|
| A/B Testing | ⚠️ | Read-only support. Uses cached data |
| Identity | ⚠️ | Read-only support. Uses cached data |
| Admin | ⚠️ | Read-only support. Uses cached data |
| Analytics | ❌ | No offline support |
| Announcements | ❌ | No offline support |
| Calendars | | |
| Chat | ❌ | No offline support |
| Cloud Save | ❌ | No offline support |
| Connectivity | ✅ | Full offline support |
| Content | ⚠️ | Read-only support. Uses cached data |
| Currency | ⚠️ | Read-only support. Uses cached data |
| Events | ❌ | No offline support |
| Game Shards | | |
| Groups | ❌ | No offline support |
| Inventory | ⚠️ | Read-only support. Uses cached data |
| Leaderboards | ⚠️ | Read-only support. Uses cached data |
| Mail | ❌ | No offline support |
| Microservices | ❌ | No offline support |
| Multiplayer | ❌ | No offline support |
| Notifications | ❌ | No offline support |
| Payments | ❌ | No offline support |
| Player History | | |
| Promotions | | |
| Realm Administration | | |
| Skinning | ✅ | Full offline support |
| Stats | ⚠️ | Read-only support. Uses cached data |
| Store | ⚠️ | Read-only support. Uses cached data |
| Tournaments | ⚠️ | Read-only support. Uses cached data |


- ✅ - Feature offers **full** support while the game client is offline
- ⚠️ - Feature offers **partial** support while the game client is offline
- ❌ - Feature offers **no** support while the game client is offline

## Prefab Support

Generally speaking, Beamable feature prefabs will render properly when offline. Beamable uses a local data cache.

Additionally, _some_ feature prefabs are compatible with the Beamable prefab "OfflineObjects". Attach it to a GameObject for enhancements.

**OfflineObjects Support**

- Account Management Flow

## REST API Support

While online, Beamable will cache the game project, game content, the user, and stats for offline use. As long as the only thing performed while "offline" are read operations, those can function without connectivity.

The other part of this is the local cache. If a request has the "useCache: true" then it can operate to some limited capacity "offline".

**Local Cache Support**

- `/basic/realms/project`
- `/basic/accounts/me`
- `/basic/content/manifest?id={manifestID}`
- `/basic/content/manifest/checksum`
- `/basic/realms/customer`
- `/basic/realms/games`
- `/basic/stats/client/batch?format=stringlist&objectIds={queryString}`

The Beamable [ConnectivityService](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Connectivity_1_1ConnectivityService.html#details) hits a `/health` route on the Beamable gateway service to ensure that your game can reach the Beamable backend platform.
