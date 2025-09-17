[beamable-sdk](../../modules.md) / [services](../README.md) / PlayerService

# Class: PlayerService

Defined in: [src/services/PlayerService.ts:11](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L11)

A service for managing player-related data and operations.

## Accessors

### account

#### Get Signature

> **get** **account**(): [`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)

Defined in: [src/services/PlayerService.ts:59](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L59)

Retrieves the current player's account information.

##### Returns

[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)

***

### announcements

#### Get Signature

> **get** **announcements**(): [`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]

Defined in: [src/services/PlayerService.ts:77](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L77)

Retrieves the current player's announcements.

##### Returns

[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]

***

### id

#### Get Signature

> **get** **id**(): `string`

Defined in: [src/services/PlayerService.ts:64](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L64)

Retrieves the current player's ID.

##### Returns

`string`

***

### leaderboards

#### Get Signature

> **get** **leaderboards**(): `Record`<`string`, [`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

Defined in: [src/services/PlayerService.ts:90](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L90)

Retrieves the current player's leaderboards.

##### Returns

`Record`<`string`, [`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

***

### stats

#### Get Signature

> **get** **stats**(): `Record`<`string`, `string`\>

Defined in: [src/services/PlayerService.ts:137](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L137)

Retrieves the current player's stats.

##### Returns

`Record`<`string`, `string`\>

## Methods

### hasThirdPartyAssociation()

> **hasThirdPartyAssociation**(`provider`): `boolean`

Defined in: [src/services/PlayerService.ts:44](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/PlayerService.ts#L44)

Checks if the current player has an association with the given third-party provider.

#### Parameters

##### provider

[`ThirdPartyAuthProvider`](../enumerations/ThirdPartyAuthProvider.md)

#### Returns

`boolean`

`true` if the player has an association with the given third-party provider, `false` otherwise.

#### Example

```ts
const hasGoogle = beam.player.hasThirdPartyAssociation(ThirdPartyAuthProvider.Google);
```
