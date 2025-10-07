# Profile & Storage Overview

Beamable offers powerful and flexible solutions for in-game storage and content management.

## Features

| Feature                                                           | Details                                                                |
| :---------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [Cloud Save](doc:cloud-save-feature-overview)                     | Cloud save functionality for player data. Store and sync player progress across devices.     |
| [Content](doc:content-feature-overview)                           | Content management system for game data. Manage game configuration and assets.           |
| [Microservice Storage](doc:microservice-storage-feature-overview) | Microservice-based storage solution. Flexible server-side data storage and management. |
| [Stats](doc:stats-feature-overview)                               | Player statistics tracking. Monitor and analyze player behavior and progress.               |

## Comparison

Game makers can mix and match features to create the custom solution to meet the needs of the game design.

Each feature has read/write access from the game client itself and via [Portal](doc:portal). Some features store information game-specifically and some store information player-specifically.

| Default Benefits     | Client Can (Read/Write) | Portal Can (Read/Write) | Describes "Game" | Describes "Player" |
| :------------------- | :---------------------- | :---------------------- | :--------------- | :----------------- |
| Cloud Save           | ✔️                      | ✔️                      | ❌               | ✔️                 |
| Content              | ✔️                      | ✔️                      | ✔️               | ❌                 |
| Microservice Storage | ✔️                      | ✔️                      | ✔️               | ✔️                 |
| Stats                | ✔️                      | ✔️                      | ❌               | ✔️                 |

## Case Study

_Example: Your game offers 3 'save slots'. On the first game session, the player chooses one empty save slot and all player-specific progress is stored at the end of each level. On subsequent game sessions, the player may continue from an existing save slot or choose an empty one. This is a good fit for the [Cloud Save](doc:cloud-save-feature-overview)._

![Save Slots sample UI](../../../../../media/imgs/FileSelect.png)
