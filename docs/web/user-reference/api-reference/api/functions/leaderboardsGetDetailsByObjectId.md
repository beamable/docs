[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetDetailsByObjectId

# Function: leaderboardsGetDetailsByObjectId()

> **leaderboardsGetDetailsByObjectId**(`requester`, `objectId`, `from?`, `max?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardDetails`](../../schema/type-aliases/LeaderboardDetails.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:478](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/LeaderboardsApi.ts#L478)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

`string`

Gamertag of the player.

### from?

`number`

The `from` parameter to include in the API request.

### max?

`number`

The `max` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardDetails`](../../schema/type-aliases/LeaderboardDetails.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
