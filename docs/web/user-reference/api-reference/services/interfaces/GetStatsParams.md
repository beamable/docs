[beamable-sdk](../../modules.md) / [services](../README.md) / GetStatsParams

# Interface: GetStatsParams

Defined in: [src/services/StatsService.ts:9](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L9)

## Properties

### accessType

> **accessType**: `"public"` \| `"private"`

Defined in: [src/services/StatsService.ts:20](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L20)

The type of access for the stats.

#### Remarks

'public' for public stats, 'private' for private stats.

***

### domainType?

> `optional` **domainType**: `"client"` \| `"game"`

Defined in: [src/services/StatsService.ts:15](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L15)

The type of domain for the stats.

#### Remarks

'client' for client-side stats, 'game' for game server stats.

#### Default

```ts
'client'
```

***

### stats?

> `optional` **stats**: `string`[]

Defined in: [src/services/StatsService.ts:25](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L25)

The specific stats to fetch.

#### Remarks

If not provided, all stats for the specified domain and access will be fetched.
