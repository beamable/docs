[beamable-sdk](../../modules.md) / [services](../README.md) / LeaderboardsService

# Class: LeaderboardsService

Defined in: [src/services/LeaderboardsService.ts:72](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L72)

## Extends

- [`ApiService`](ApiService.md)

## Constructors

### Constructor

> **new LeaderboardsService**(`props`): `LeaderboardsService`

Defined in: [src/services/LeaderboardsService.ts:73](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L73)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`LeaderboardsService`

#### Overrides

`ApiService.constructor`

## Methods

### freeze()

> **freeze**(`params`): `Promise`<`void`\>

Defined in: [src/services/LeaderboardsService.ts:270](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L270)

Freezes a leaderboard, preventing further score updates.

#### Parameters

##### params

[`FreezeLeaderboardParams`](../interfaces/FreezeLeaderboardParams.md)

#### Returns

`Promise`<`void`\>

#### Remarks

This method can only be called by a game server using an admin account.

#### Example

```ts
await beamServer.leaderboards(adminId).freeze({ id: 'leaderboard-id' });
```

#### Throws

If the request fails, the leaderboard does not exist,
  or this method is called on the client side.

***

### get()

> **get**(`params`): `Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

Defined in: [src/services/LeaderboardsService.ts:103](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L103)

Fetches a leaderboard view for the current player.

#### Parameters

##### params

[`GetLeaderboardParams`](../interfaces/GetLeaderboardParams.md)

#### Returns

`Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

#### Example

```ts
// client-side:
const leaderboards = beam.leaderboards;
// server-side:
const leaderboards = beamServer.leaderboards(playerId);
// fetch a leaderboard view
const leaderboardView = await leaderboards.get({
  id: 'leaderboard-id',
  from: 1, // optional, to start from a specific rank
  max: 10, // optional, to limit the number of ranks returned
  focus: 'playerGamertagOrId', // optional, to center the view on a specific player
  outlier: 'anotherPlayerGamertagOrId', // optional, to include another player as an outlier
  includeFriends: true, // optional, to include friends in the view
  includeGuilds: true, // optional, to include group members in the view
});
```

#### Throws

If the request fails or the leaderboard does not exist.

***

### getAssignedBoard()

> **getAssignedBoard**(`params`): `Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

Defined in: [src/services/LeaderboardsService.ts:143](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L143)

Fetches the partitioned or cohorted leaderboard view for the current player.

#### Parameters

##### params

[`GetLeaderboardParams`](../interfaces/GetLeaderboardParams.md)

#### Returns

`Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

#### Remarks

This method is used to fetch a leaderboard that has been assigned to the current player.

#### Example

```ts
// client-side:
const leaderboards = beam.leaderboards;
// server-side:
const leaderboards = beamServer.leaderboards(playerId);
// fetch the assigned leaderboard view
const assignedBoard = await leaderboards.getAssignedBoard({ id: 'leaderboard-id' });
```

#### Throws

If the assignment does not exist or the leaderboard cannot be fetched.

***

### getFriendRanks()

> **getFriendRanks**(`params`): `Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

Defined in: [src/services/LeaderboardsService.ts:174](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L174)

Fetches the ranks of friends in a leaderboard for the current player.

#### Parameters

##### params

[`GetLeaderboardFriendsParams`](../interfaces/GetLeaderboardFriendsParams.md)

#### Returns

`Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

#### Example

```ts
// client-side:
const leaderboards = beam.leaderboards;
// server-side:
const leaderboards = beamServer.leaderboards(playerId);
// fetch the ranks of friends in a leaderboard
const friendRanks = await leaderboards.getFriendRanks({
  id: 'leaderboard-id',
});
```

#### Throws

If the request fails or the leaderboard does not exist.

***

### getRanks()

> **getRanks**(`params`): `Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

Defined in: [src/services/LeaderboardsService.ts:202](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L202)

Fetches the ranks of specific players in a leaderboard for the current player.

#### Parameters

##### params

[`GetLeaderboardRanksParams`](../interfaces/GetLeaderboardRanksParams.md)

#### Returns

`Promise`<[`LeaderBoardView`](../../schema/type-aliases/LeaderBoardView.md)\>

#### Example

```ts
// client-side:
const leaderboards = beam.leaderboards;
// server-side:
const leaderboards = beamServer.leaderboards(playerId);
// fetch the ranks of specific players in a leaderboard
const ranks = await leaderboards.getRanks({
  id: 'leaderboard-id',
  playerIds: ['player1GamertagOrId', 'player2GamertagOrId'],
});
```

#### Throws

If the request fails or the leaderboard does not exist.

***

### setScore()

> **setScore**(`params`): `Promise`<`void`\>

Defined in: [src/services/LeaderboardsService.ts:231](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/LeaderboardsService.ts#L231)

Sets the score for the current player in a leaderboard.

#### Parameters

##### params

[`SetLeaderboardScoreParams`](../interfaces/SetLeaderboardScoreParams.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const leaderboards = beam.leaderboards;
// server-side:
const leaderboards = beamServer.leaderboards(playerId);
// set the score for the current player in a leaderboard
await leaderboards.setScore({
  id: 'leaderboard-id',
  score: 1000,
  increment: true, // optional, to increment the existing score
  stats: { key: 'value' }, // optional, additional stats to set
});
```

#### Throws

If the request fails or the leaderboard does not exist.
