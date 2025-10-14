# Global Price War 2 - Chat & MicroStorage Sample

A sample project demonstrating Beamable's Chat and MicroStorage features through an advanced trading game called "Global Price Wars 2".

In "Global Price War" (GPW), the winners say **Buy low, sell high! Finish rich and be top on the Leaderboard.**. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/2yVdP53Gw64?si=6f3VCYe6z6tWcxAa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Features

!!! info "Beamable Features Used"

    This sample demonstrates integration with multiple Beamable services:

    - [Chat](../user-reference/beamable-services/social-networking/chat.md) - Real-time messaging between players
    - **[Connectivity](../user-reference/beamable-services/social-networking/connectivity.md)** - Player connection and presence management
    - **[Content Management](../user-reference/beamable-services/profile-storage/content/content-overview.md)** - Game configuration and data storage
    - **[Inventory System](../user-reference/beamable-services/game-economy/inventory-overview.md)** - Player item and resource management
    - **[Leaderboards](../user-reference/beamable-services/social-networking/leaderboards.md)** - Player rankings and competitive scoring
    - **[Microservices](../user-reference/cloud-services/microservices/microservice-framework.md)** - Custom server-side business logic
    - **[MicroStorage](../user-reference/cloud-services/microstorages.md)** - MongoDB database integration for persistent data


### Architecture

The GPW2 project uses a more sophisticated architecture compared to GPW1:

- **Client-Server Model**: Game logic runs on Beamable Microservices
- **Database Storage**: Market data and game state stored in MicroStorage
- **Real-time Updates**: Chat and market data synchronized across clients
- **Scalable Design**: Supports multiple concurrent games and players


## Project Repository

The code for Global Price War 2 is available at [Chat GPW 2 With MicroStorage Sample Project](https://github.com/beamable/Chat_GPW_2_With_MicroStorage_Sample_Project). Please check the [Guide](chat-gpw2-guide.md) for guidance on using the project.

## Screenshots

| Scene01Intro | Scene02Game | Scene03Chat | Scene04Settings | Scene05Leaderboard |
| :--- | :--- | :--- | :--- | :--- |
| <img src="https://files.readme.io/8f9ffe2-8.jpg" height="230"/> | <img src="https://files.readme.io/d1209ae-4.jpg" height="230"/> | <img src="https://files.readme.io/5d113e8-3.jpg" height="230"/> | <img src="https://files.readme.io/d894514-settings.png" height="230"/> | <img src="https://files.readme.io/fd4b0d4-5.jpg" height="230"/> |

!!! info "Project Comparison"

    There are two repos for the "Global Price Wars" game each with distinct learning goals.

    1. [Chat GPW Sample Project](../chat-gpw/chat-gpw-overview.md) - Simpler project, the `GPWBasicDataFactory` uses random, local data values.
    2. [Chat GPW2 Sample Project With MicroStorage](chat-gpw2-overview.md) - **Complex project, the `GPWMicroStorageDataFactory` uses Beamable Microservices and MicroStorage with data values stored in shared database. You are currently viewing the documentation for this project.**

## Download

| Source | Detail |
| :--- | :--- |
| **Beamable** | 1. **Download** the [Chat GPW2 Sample Project](https://github.com/beamable/Chat_GPW_2_With_MicroStorage_Sample_Project)<br/>2. Open in Unity Editor (Version 2021.3 or later)<br/>3. Open the Beamable [Toolbox](../../user-reference/editor-systems/unity-editor-login.md)<br/>4. Sign-In / Register To Beamable. See [Getting Started](../../getting-started/installing-beamable.md) for more info<br/>5. Set up Docker and Microservices following the [Microservices Guide](../../user-reference/cloud-services/microservices/microservice-framework.md)<br/>6. Deploy the MicroStorage and Microservices<br/>7. Open the `Scene01Intro` Scene<br/>8. Play The Scene: Unity → Edit → Play<br/>9. Click the "Start" Button<br/>10. Enjoy!<br/><br/>_Note: This sample project requires Docker setup for Microservices and is compatible with Unity 2021.3 and later versions._ |

### Rules of the Game

- 1 player starts the game with limited turns
- After the final turn, the game is over
- The player's final score is calculated as `Cash + Bank - Debt`
- Each turn, the player makes decision to increase the total cash
  - Use money in `Cash`. Buy items at a low price, Sell items at a high price
  - Move money into the `Bank`. The bank pays interest to the player after each turn
  - Move money out of `Debt.` The debtors charge interest to the player after each turn
  - Chat with other players to better understand the market price of items

_Pro Tip: Sell all owned items before the final turn to increase the final score._

## Key Differences from GPW1

This advanced version (GPW2) includes several enhancements over the basic Chat GPW project:

### MicroStorage Integration
- **Persistent Data**: Uses Beamable MicroStorage for persistent, server-side data storage
- **Shared Market Data**: All players see the same market prices stored in the database
- **Real-time Synchronization**: Market data updates are synchronized across all connected players

### Microservices Architecture
- **Server-side Logic**: Game logic runs on Beamable Microservices for better security and consistency
- **Data Validation**: Server validates all transactions and market operations
- **Scalable Design**: Architecture supports multiple concurrent players and games

### Advanced Features
- **Database Persistence**: Game state persists between sessions
- **Enhanced Chat**: More sophisticated chat integration with game events
- **Market Dynamics**: More realistic market behavior with server-controlled pricing
