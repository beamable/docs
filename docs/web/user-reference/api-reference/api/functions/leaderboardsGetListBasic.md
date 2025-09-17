[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetListBasic

# Function: leaderboardsGetListBasic()

> **leaderboardsGetListBasic**(`requester`, `includePartitions?`, `limit?`, `prefix?`, `skip?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardListResponse`](../../schema/type-aliases/LeaderboardListResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:44](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/LeaderboardsApi.ts#L44)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### includePartitions?

`boolean`

The `includePartitions` parameter to include in the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### prefix?

`string`

The `prefix` parameter to include in the API request.

### skip?

`number`

The `skip` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardListResponse`](../../schema/type-aliases/LeaderboardListResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
