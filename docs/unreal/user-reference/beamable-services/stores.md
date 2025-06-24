# Stores

Beamable's Store feature enables game-makers to create and manage dynamic in-game storefronts where players can purchase items using virtual currencies. Stores support various features including:

- Per Store Settings
- Purchase limitations and player requirements
- Items and Virtual currency basic implementation
- Customizable store layouts and content

# Content Types
In Unreal, Stores are represented by `UBeamStoreContent` class, which includes a store title and a list of links to `UBeamListingContent` types. The `UBeamListingContent` class contains all the details about the offer, such as player requirements, costs, and benefits. Make sure you understand the [Content System](content.md) as both `UBeamStoreContent` and `UBeamListingContent` are subclasses of `UBeamContentObject`.

## Store Content
The store content has the following properties:

- **Show Innactive Listing**: Shows things that the user already bought and their outside of availability window or outside cohort settings.
- **ActiveListingLimit**: Defaults to 20. The Store will only show the first N listings that are valid. When asking for all active listings for a particular user, the API will return a maximum of whatever is here.

## Listing Content
You can think of a listing as an "entry in a catalog of purchasable products".

- **Price**: Is the definition of `currency` a player must have to acquire this listing.
- **Offer**: Describes what will be added to the player's inventory once the purchase is completed.
- **Client Data**: Use this to store information specific to your game's UI in a way that you can parse and display.
- **DateTime**: Is an active period is an ISO-8601 string.
- **Purchase Limit**: Number of times the listing is purchasable by the same user. Since its optional, absent means infinite purchases allowed while the listing's other filters say you can buy it.

We don't support subtypes of `UBeamListingContent`; use `ClientData` instead.

# Beam Store Subsystem
Purchases are handled through the `UBeamStoreSubsystem`. This subsystem allows you to request the purchase of any available `Listing` on any `Store`. It also provides helper functions to retrieve detailed data from listings, making it easier to interact with store content.

You can fetch a particular player's view of a particular store, via the `RefreshStoresOperation` or `RefreshStoreOperation`. After the view is refreshed, you can access the view for that particular player through `TryGetStoreView`. To make purchases, you can use the `PerformPurchaseOperation`.

## Purchases IAP support
Beamable supports purchasing listings using in-game IAPs, but for the Unreal SDK, this feature is not yet available. It will be added in future releases.