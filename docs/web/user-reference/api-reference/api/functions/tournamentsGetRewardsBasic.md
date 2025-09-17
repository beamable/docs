[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetRewardsBasic

# Function: tournamentsGetRewardsBasic()

> **tournamentsGetRewardsBasic**(`requester`, `contentId?`, `tournamentId?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`RewardsResponse`](../../schema/type-aliases/RewardsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:138](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/TournamentsApi.ts#L138)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### contentId?

`string`

The `contentId` parameter to include in the API request.

### tournamentId?

`string`

The `tournamentId` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`RewardsResponse`](../../schema/type-aliases/RewardsResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
