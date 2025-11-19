[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetRanksByObjectId

# Function: leaderboardsGetRanksByObjectId()

> **leaderboardsGetRanksByObjectId**(`requester`, `objectId`, `ids`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderBoardViewResponse`](../../schema/type-aliases/LeaderBoardViewResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:200](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/LeaderboardsApi.ts#L200)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

`string`

Gamertag of the player.

### ids

`string`

The `ids` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderBoardViewResponse`](../../schema/type-aliases/LeaderBoardViewResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
