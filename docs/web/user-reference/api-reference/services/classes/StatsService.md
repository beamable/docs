[beamable-sdk](../../modules.md) / [services](../README.md) / StatsService

# Class: StatsService

Defined in: [src/services/StatsService.ts:49](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L49)

## Extends

- [`ApiService`](ApiService.md)

## Constructors

### Constructor

> **new StatsService**(`props`): `StatsService`

Defined in: [src/services/StatsService.ts:50](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L50)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`StatsService`

#### Overrides

`ApiService.constructor`

## Methods

### get()

> **get**(`params`): `Promise`<`Record`<`string`, `string`\>\>

Defined in: [src/services/StatsService.ts:78](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L78)

Fetches stats for the current player.

#### Parameters

##### params

[`GetStatsParams`](../interfaces/GetStatsParams.md)

#### Returns

`Promise`<`Record`<`string`, `string`\>\>

#### Remarks

Game domain stats can only be fetched by the game server.

#### Example

```ts
// client-side: fetch private or public stats for a client domain
const stats = await beam.stats.get({
  accessType: 'private', // or 'public'
  stats: ['CURRENT_LEVEL', 'SCORE'], // optional, fetches all stats if not provided
});
// server-side: fetch private or public stats for a game domain
const gameStats = await beamServer.stats(playerId).get({
  domainType: 'game',
  accessType: 'private', // or 'public'
  stats: ['CURRENT_LEVEL', 'SCORE'], // optional, fetches all stats if not provided
});
```

#### Throws

If the request fails or the stats do not exist.

***

### set()

> **set**(`params`): `Promise`<`void`\>

Defined in: [src/services/StatsService.ts:134](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L134)

Sets a stats for the current player.

#### Parameters

##### params

[`SetStatsParams`](../interfaces/SetStatsParams.md)

#### Returns

`Promise`<`void`\>

#### Remarks

Game domain stats can only be set by the game server.

#### Example

```ts
const stats = {
  CURRENT_LEVEL: '10',
  SCORE: '1000',
};
// client-side: set stats for a client domain
await beam.stats.set({
  accessType: 'private', // or 'public'
  stats,
});
// server-side: set stats for a game domain
await beamServer.stats(playerId).set({
  domainType: 'game',
  accessType: 'private', // or 'public'
  stats,
});
```

#### Throws

If the request fails or the stats cannot be set.
