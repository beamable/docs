[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetViewByObjectId

# Function: leaderboardsGetViewByObjectId()

> **leaderboardsGetViewByObjectId**(`requester`, `objectId`, `focus?`, `friends?`, `from?`, `guild?`, `max?`, `outlier?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderBoardViewResponse`](../../schema/type-aliases/LeaderBoardViewResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:511](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/LeaderboardsApi.ts#L511)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

`string`

Gamertag of the player.

### focus?

The `focus` parameter to include in the API request.

`string` | `bigint`

### friends?

`boolean`

The `friends` parameter to include in the API request.

### from?

`number`

The `from` parameter to include in the API request.

### guild?

`boolean`

The `guild` parameter to include in the API request.

### max?

`number`

The `max` parameter to include in the API request.

### outlier?

The `outlier` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderBoardViewResponse`](../../schema/type-aliases/LeaderBoardViewResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
