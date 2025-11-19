[beamable-sdk](../../modules.md) / [services](../README.md) / GetLeaderboardParams

# Interface: GetLeaderboardParams

Defined in: [src/services/LeaderboardsService.ts:16](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L16)

## Properties

### focus?

> `optional` **focus**: `string` \| `bigint`

Defined in: [src/services/LeaderboardsService.ts:29](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L29)

Player (gamertag) to center the leaderboard view on.

***

### from?

> `optional` **from**: `number`

Defined in: [src/services/LeaderboardsService.ts:22](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L22)

Start rank of the leaderboard view.

#### Remarks

This is ignored when focus is set

***

### id

> **id**: `string`

Defined in: [src/services/LeaderboardsService.ts:18](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L18)

The ID of the leaderboard to fetch.

***

### includeFriends?

> `optional` **includeFriends**: `boolean`

Defined in: [src/services/LeaderboardsService.ts:36](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L36)

Whether to include friends in the leaderboard.

***

### includeGuilds?

> `optional` **includeGuilds**: `boolean`

Defined in: [src/services/LeaderboardsService.ts:38](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L38)

Whether to include group members in the leaderboard.

***

### max?

> `optional` **max**: `number`

Defined in: [src/services/LeaderboardsService.ts:27](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L27)

Maximum number of ranks to return in the leaderboard view.

#### Remarks

When `focus` is set, includes the focused player plus up to `max/2` entries before and after. If one side has fewer entries, it’s truncated.

***

### outlier?

> `optional` **outlier**: `string` \| `bigint`

Defined in: [src/services/LeaderboardsService.ts:34](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/LeaderboardsService.ts#L34)

Player (gamertag) to use as an outlier in the leaderboard view.

#### Remarks

This is used to include a specific player in the leaderboard view.
