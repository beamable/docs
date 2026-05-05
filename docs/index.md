# Introduction to Unreal SDK

**Welcome to the Beamable Unreal SDK Documentation!**

The Beamable Unreal SDK provides all of the functionality to integrate Beamable's systems into your Project. It includes features like Authentication, Content, Events, Inventory, Microservices and much more.

## SDK Design Principles

- Source-available and modifiable inside your project
- Simple by default, with clear extension points
- Explicit about assumptions when they exist
- Full parity between Blueprint and C++ APIs (except when otherwise notated in docs)

## Platform Support Roadmap
The Beamable Unreal SDK is designed to work across multiple platforms. Below is a table outlining the current support status and estimated time of arrival (ETA) for each platform.

| Platform | Client Support | Dedicated Server Support | ETA        |
|----------|----------------|--------------------------|------------|
| Windows  | ✅ | — | Released   |
| Android  | ✅ | — | Released          |
| Linux    | — | ✅ | Released         |
| iOS      | 🚧 Planned | — | Q4 2025    |
| Consoles | 🚧 Planned | — | Q1/Q2 2026 |

## Beamable CLI
Most Beamable workflows run through the Beamable CLI. Editor integrations use the CLI to create Engine-specific workflows.

The SDK is tightly integrated with the CLI, in some ways more than others. For example:

- [Content](unreal/user-reference/beamable-services/content.md), being designer-focused, has its own UE-familiar content editing UI so you can edit the various JSON blobs that define your game's content
- [Microservices](unreal/user-reference/microservices/microservices.md), more engineer focused, leans more directly on the CLI

**The Beamable CLI is invisible where it needs to be and explicit where needed.**

## Where to start?
New users should start with:

- [Your First Request](unreal/getting-started/first-request.md)
- [Blueprints Integration](unreal/user-reference/runtime-systems/blueprints.md)
- [Runtime Systems Overview](unreal/user-reference/overview.md)
- [Identity](unreal/user-reference/beamable-services/identity.md)

After this, it depends on what your game is and what you are looking to do.

- The most-used backend systems include: <!-- TODO(@drewbleam): This should lean further into showing off what the SDK can do (maybe Microservice cards like docs.beamable lander) -->
    - [Inventory](unreal/user-reference/beamable-services/inventory.md) for items and currency management
    - [Stats](unreal/user-reference/beamable-services/stats.md) for player-scoped key-value stores
- Custom features are explored in the [Content](unreal/user-reference/beamable-services/content.md) and [Microservices](unreal/user-reference/microservices/microservices.md) documentation with consideration to data structuring and writing custom code with Beamable

---
*For support, email [support@beamable.com](mailto:support@beamable.com) or visit the [Beamable support page](https://beamable.com/support).*
