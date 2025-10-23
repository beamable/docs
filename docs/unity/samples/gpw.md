# Global Price War - Chat Sample

A sample project demonstrating Beamable's Chat feature through a trading game called "Global Price Wars".

In "Global Price War" (GPW), the winners say **Buy low, sell high! Finish rich and be top on the Leaderboard.**. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/2yVdP53Gw64?si=Y7t2Z5EvIduv5bmc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


!!! info "Beamable Features Used"

    This sample demonstrates integration with multiple Beamable services:
    
    - [Chat](../user-reference/beamable-services/social-networking/chat.md) - Real-time messaging between players
    - [Connectivity](../user-reference/beamable-services/social-networking/connectivity.md) - Player connection and presence
    - [Content](../user-reference/beamable-services/profile-storage/content/content-overview.md) - Game configuration and data management
    - [Inventory](../user-reference/beamable-services/game-economy/inventory-overview.md) - Player item management
    - [Leaderboards](../user-reference/beamable-services/social-networking/leaderboards.md) - Player rankings and scores


## Screenshots

| Scene01Intro | Scene02Game | Scene03Chat | Scene04Settings | Scene05Leaderboard |
| :--- | :--- | :--- | :--- | :--- |
| <img src="https://files.readme.io/8f9ffe2-8.jpg" height="230"/> | <img src="https://files.readme.io/d1209ae-4.jpg" height="230"/> | <img src="https://files.readme.io/5d113e8-3.jpg" height="230"/> | <img src="https://files.readme.io/d894514-settings.png" height="230"/> | <img src="https://files.readme.io/fd4b0d4-5.jpg" height="230"/> |

!!! info "Variations On A Theme"

    There are two repos for the "Global Price Wars" game each with distinct learning goals.

    1. **Chat GPW Sample Project** - Simpler project, the `GPWBasicDataFactory` uses random, local data values. **You are currently viewing the documentation for this project.**
    2. [Chat GPW2 Sample Project With MicroStorage](gpw2.md) - Complex project, the `GPWMicroStorageDataFactory` uses Beamable Microservices and MicroStorage with data values stored in shared database

## Download

| Source | Detail |
| :--- | :--- |
| **Beamable** | 1. **Download** the [Chat GPW Sample Project](https://github.com/beamable/Chat_GPW_Sample_Project)<br/>2. Open in Unity Editor (Version 2021.3 or later)<br/>3. Open the Beamable [Toolbox](../user-reference/editor-systems/unity-editor-login.md)<br/>4. Sign-In / Register To Beamable. See [Getting Started](../getting-started/installing-beamable.md) for more info<br/>5. Rebuild the Unity [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@1.3/manual/AddressableAssetsDevelopmentCycle.html) : Unity → Window → Asset Management → Groups, then Build → Update a Previous Build<br/>6. Open the `Scene01Intro` Scene<br/>7. Play The Scene: Unity → Edit → Play<br/>8. Click the "Start" Button<br/>9. Enjoy!<br/><br/>_Note: This sample project is compatible with Unity 2021.3 and later versions._ |

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

## Design Overview

Many Beamable features are used to implement the game design and game rules.

### Content

Using the Beamable [Content](../user-reference/beamable-services/profile-storage/content/content-overview.md) feature, this game stores core data with ease and flexibility.

| Remote Configuration | Location | Product |
| :--- | :--- | :--- |
| <img src="https://files.readme.io/300a32f-remo.jpg" width="300"/> | <img src="https://files.readme.io/c1c1b17-locatino.jpg" width="300"/> | <img src="https://files.readme.io/da1d00f-coffee.jpg" width="300"/> |

### Class Organization

Each scene uses the `GPWController` class to interact with the local data model and the remote services.

Here is a high-level chart showing the _partial_ structure.

<!-- Class organization diagram would go here -->

### Design of Data

The data within the `RuntimeDataStorage` is vital for the core game loop. 

The game design requires that all users in the same game (e.g. same chat session) to see a shared world of consistent pricing. This is accomplished using the data structure and data factory below.

**Data Structure**  
The structure contains all the locations of the game. Within each location is information about each product; including its price and quantity.

- List < LocationContentView >
  - LocationData (e.g. "Africa")
  - List < ProductContentViews >
    - ProductData (e.g. "Chocolate")
    - MarketGoods
      - Price (e.g. "10")
      - Quantity (e.g. "3")

**Data Factory**  
The `IDataFactory` gets data as shown in the diagram below.

- A. The `RuntimeDataStorage` calls to `GetLocationContentViews()` at the start of each game session
- B. Here in the GPW game the `GPWBasicDataFactory` creates pseudorandom price/quantity for all products. A random-seed value is shared across all game clients for consistent pricing. This solution is easier to understand, but likely not robust enough for a production game.

<!-- Data factory diagram would go here -->


