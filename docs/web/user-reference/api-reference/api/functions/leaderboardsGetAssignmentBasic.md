[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetAssignmentBasic

# Function: leaderboardsGetAssignmentBasic()

> **leaderboardsGetAssignmentBasic**(`requester`, `boardId`, `joinBoard?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardAssignmentInfo`](../../schema/type-aliases/LeaderboardAssignmentInfo.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:100](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/LeaderboardsApi.ts#L100)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### boardId

`string`

The `boardId` parameter to include in the API request.

### joinBoard?

`boolean`

The `joinBoard` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardAssignmentInfo`](../../schema/type-aliases/LeaderboardAssignmentInfo.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
