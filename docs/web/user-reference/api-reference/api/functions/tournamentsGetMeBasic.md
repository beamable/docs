[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetMeBasic

# Function: tournamentsGetMeBasic()

> **tournamentsGetMeBasic**(`requester`, `contentId?`, `hasUnclaimedRewards?`, `tournamentId?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetPlayerStatusResponse`](../../schema/type-aliases/GetPlayerStatusResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:355](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/TournamentsApi.ts#L355)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

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

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetPlayerStatusResponse`](../../schema/type-aliases/GetPlayerStatusResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
