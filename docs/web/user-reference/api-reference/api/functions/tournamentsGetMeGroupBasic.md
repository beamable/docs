[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsGetMeGroupBasic

# Function: tournamentsGetMeGroupBasic()

> **tournamentsGetMeGroupBasic**(`requester`, `contentId?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetGroupStatusResponse`](../../schema/type-aliases/GetGroupStatusResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:111](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/TournamentsApi.ts#L111)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### contentId?

`string`

The `contentId` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetGroupStatusResponse`](../../schema/type-aliases/GetGroupStatusResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
