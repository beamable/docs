# Stores
Beamable's Store feature enables game-makers to create an in-game storefront where users can purchase items using virtual currency.

!!! note "Purchases IAP support"
    Beamable supports purchasing listings using in-game IAPs, but for the Unreal SDK, this feature is not yet available. It will be added in future releases.

### Content Types
In Unreal, Stores are represented by `UBeamStoreContent` class, which includes a store title and a list of links to `UBeamListingContent` types. The `UBeamListingContent` class contains all the details about the offer, such as player requirements, costs, and benefits. Make sure you understand the [Content System](content.md) as both `UBeamStoreContent` and `UBeamListingContent` are subclasses of `UBeamContentObject`.
