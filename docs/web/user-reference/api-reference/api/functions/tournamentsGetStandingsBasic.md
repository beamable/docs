[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetStandingsBasic

# Function: tournamentsGetStandingsBasic()

> **tournamentsGetStandingsBasic**(`requester`, `tournamentId`, `contentId?`, `cycle?`, `focus?`, `from?`, `max?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetStandingsResponse`](../../schema/type-aliases/GetStandingsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:266](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/TournamentsApi.ts#L266)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### tournamentId

`string`

The `tournamentId` parameter to include in the API request.

### contentId?

`string`

The `contentId` parameter to include in the API request.

### cycle?

`number`

The `cycle` parameter to include in the API request.

### focus?

The `focus` parameter to include in the API request.

`string` | `bigint`

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

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetStandingsResponse`](../../schema/type-aliases/GetStandingsResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
