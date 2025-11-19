[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetGlobalBasic

# Function: tournamentsGetGlobalBasic()

> **tournamentsGetGlobalBasic**(`requester`, `tournamentId`, `contentId?`, `cycle?`, `focus?`, `from?`, `max?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetStandingsResponse`](../../schema/type-aliases/GetStandingsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:194](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/TournamentsApi.ts#L194)

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
