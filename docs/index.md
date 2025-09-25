# Introduction to Unreal SDK

Welcome to the Beamable!

The Beamable Unreal SDK provides all the functionality to integrate The Beamable Systems in your Project. It include many features such as Authentication, Content, Events, Inventory, Microservices and more.

Here's a bit of our philosophy when desing the SDK so you know a bit what to expect:

| **<center>The SDK's source code is entirely available and modifiable inside your project by you</center>**                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| <center>In case you modify the SDK's source code, we cannot guarantee that its features will work. We trust you to know when doing so might be worth it for you (VCS are your friend here). |

| **<center>The SDK keeps itself as simple as possible, providing extension points and documentation.**                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| <center>We believe that tools should helpful or at least not get in your way. If you find yourself working around parts of the SDK instead of using them even with MicroServices/Storages, reach out to us. |

| **<center>The SDK is careful about assumptions it makes.** |
| ----------- | 
|<center>Whenever we ***have to*** make an assumption, we try to be explicit about what it means. MicroServices/Storages are great ways to "just write what you want instead" when using our default services is not a good fit.|

| **<center>Blueprint and C++ Code Parity** |
| ----------- | 
|<center>Most of our docs contains examples using Blueprints. Unless described otherwise there is option to achieve same results in C++ while following Blueprint sample. In C++, the subsystems and function names are the same except that, for lambda-binding, you'll need to use the `CPP_` versions of functions.|

## Platform Support Roadmap
The Beamable Unreal SDK is designed to work across multiple platforms. Below is a table outlining the current support status and estimated time of arrival (ETA) for each platform.

| Platform | Client Support | Dedicated Server Support | ETA        |
|----------|----------------|--------------------------|------------|
| Windows  | ✅ | — | Released   |
| Android  | ✅ | — | Released          |
| Linux    | — | ✅ | Released         |
| iOS      | 🚧 Planned | — | Q4 2025    |
| Consoles | 🚧 Planned | 🚧 Planned | Q1/Q2 2026 |

## Beamable CLI
Most of the Beamable workflows are enabled through the Beamable CLI; our editor integrations making use of it to create Engine-specific workflows.

The SDK is tightly integrated with the CLI in some ways more than others. For example:

- [Content](unreal/user-reference/beamable-services/content.md), being designer-focused, has its own UE-familiar content editing UI so you can edit the various JSON blobs that defines your game's content.
- [Microservices](unreal/user-reference/microservices/microservices.md), however, being more engineer focused, leans more directly on the CLI.

In other words: **The Beamable CLI is invisible to the user where it needs to be and explicit to users that need to work with them.**

## Where to start? 
Regardless of who you are, we recommend run through:

- [Your First Request](unreal/getting-started/first-request.md)
- [Blueprints Integration](unreal/user-reference/runtime-systems/blueprints.md)
- [Runtime Systems Overview](unreal/user-reference/overview.md)
- [Identity](unreal/user-reference/beamable-services/identity.md)

After this, it depends on what you're game is or what you are looking to do.

- If you are a game maker looking to implement simple and common back-end features, take a look at the docs for [Inventory](unreal/user-reference/beamable-services/inventory.md), for currency and items, and [Stats](unreal/user-reference/beamable-services/stats.md), for player-scoped key-value stores.
- If you are a game maker looking to implement unique features, browse the documentation for [Content](unreal/user-reference/beamable-services/content.md) and [Microservices](unreal/user-reference/microservices/microservices.md) to think about how to structure your game's data and how to write custom code with Beamable.

If you have any questions, feel free to contact us through one of our Customer Success channels.