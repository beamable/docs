[beamable-sdk](../../modules.md) / [api](../README.md) / leaderboardsGetMembershipByObjectId

# Function: leaderboardsGetMembershipByObjectId()

> **leaderboardsGetMembershipByObjectId**(`requester`, `objectId`, `playerId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardMembershipResponse`](../../schema/type-aliases/LeaderboardMembershipResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LeaderboardsApi.ts:173](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/LeaderboardsApi.ts#L173)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

`string`

Gamertag of the player.

### playerId

The `playerId` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LeaderboardMembershipResponse`](../../schema/type-aliases/LeaderboardMembershipResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
