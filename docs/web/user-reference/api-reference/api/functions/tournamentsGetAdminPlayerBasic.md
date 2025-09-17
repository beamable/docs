[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetAdminPlayerBasic

# Function: tournamentsGetAdminPlayerBasic()

> **tournamentsGetAdminPlayerBasic**(`requester`, `playerId`, `contentId?`, `hasUnclaimedRewards?`, `tournamentId?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AdminGetPlayerStatusResponse`](../../schema/type-aliases/AdminGetPlayerStatusResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:300](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/TournamentsApi.ts#L300)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### playerId

The `playerId` parameter to include in the API request.

`string` | `bigint`

### contentId?

`string`

The `contentId` parameter to include in the API request.

### hasUnclaimedRewards?

`boolean`

The `hasUnclaimedRewards` parameter to include in the API request.

### tournamentId?

`string`

The `tournamentId` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AdminGetPlayerStatusResponse`](../../schema/type-aliases/AdminGetPlayerStatusResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
