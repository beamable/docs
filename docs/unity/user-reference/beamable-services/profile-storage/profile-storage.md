# Profile & Storage Overview

Beamable offers powerful and flexible solutions for in-game storage and content management.


| Feature                                                           | Details                                                                |
|:------------------------------------------------------------------| :--------------------------------------------------------------------- |
| [Cloud Save](cloud-save.md)                                       | Cloud save functionality for player data. Store and sync player progress across devices.     |
| [Content](content/content-overview.md)                            | Content management system for game data. Manage game configuration and assets.           |
| [Microservice Storage](../../cloud-services/microstorages.md) | Microservice-based storage solution. Flexible server-side data storage and management. |
| [Stats](stats.md)                                                 | Player statistics tracking. Monitor and analyze player behavior and progress.               |


Game makers can mix and match features to create the custom solution to meet the needs of the game design.

Each feature has read/write access from the game client itself and via Portal. Some features store information game-specifically and some store information player-specifically.

| Default Benefits     | Client Can (Read/Write) | Portal Can (Read/Write) | Describes "Game" | Describes "Player" |
| :------------------- | :---------------------- | :---------------------- | :--------------- | :----------------- |
| Cloud Save           | ✔️                      | ✔️                      | ❌               | ✔️                 |
| Content              | ✔️                      | ✔️                      | ✔️               | ❌                 |
| Microservice Storage | ✔️                      | ✔️                      | ✔️               | ✔️                 |
| Stats                | ✔️                      | ✔️                      | ❌               | ✔️                 |
