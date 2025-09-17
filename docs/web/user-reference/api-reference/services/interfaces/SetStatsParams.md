[beamable-sdk](../../modules.md) / [services](../README.md) / SetStatsParams

# Interface: SetStatsParams

Defined in: [src/services/StatsService.ts:28](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L28)

## Properties

### accessType

> **accessType**: `"public"` \| `"private"`

Defined in: [src/services/StatsService.ts:39](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L39)

The type of access for the stats.

#### Remarks

'public' for public stats, 'private' for private stats.

***

### domainType?

> `optional` **domainType**: `"client"` \| `"game"`

Defined in: [src/services/StatsService.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L34)

The type of domain for the stats.

#### Remarks

'client' for client-side stats, 'game' for game server stats.

#### Default

```ts
'client'
```

***

### emitAnalytics?

> `optional` **emitAnalytics**: `boolean`

Defined in: [src/services/StatsService.ts:46](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L46)

Whether to emit analytics for the stats change.

***

### stats

> **stats**: `Record`<`string`, `string`\>

Defined in: [src/services/StatsService.ts:44](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/StatsService.ts#L44)

The stats to set for the current player.

#### Remarks

The keys are stat names and the values are their corresponding values as strings.
