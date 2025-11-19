[beamable-sdk](../../modules.md) / [services](../README.md) / SetLeaderboardScoreParams

# Interface: SetLeaderboardScoreParams

Defined in: [src/services/LeaderboardsService.ts:53](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L53)

## Properties

### id

> **id**: `string`

Defined in: [src/services/LeaderboardsService.ts:55](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L55)

The ID of the leaderboard to set the score for.

***

### increment?

> `optional` **increment**: `boolean`

Defined in: [src/services/LeaderboardsService.ts:62](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L62)

Whether to increment the existing score instead of overwriting it.

#### Default

```ts
false
```

***

### score

> **score**: `number`

Defined in: [src/services/LeaderboardsService.ts:57](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L57)

The score to set.

***

### stats?

> `optional` **stats**: `Record`<`string`, `string`\>

Defined in: [src/services/LeaderboardsService.ts:64](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L64)

Additional stats to set for the leaderboard entry.
