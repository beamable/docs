[beamable-sdk](../../modules.md) / [api](../README.md) / tournamentsPostBasic

# Function: tournamentsPostBasic()

> **tournamentsPostBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PlayerStatus`](../../schema/type-aliases/PlayerStatus.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TournamentsApi.ts:87](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/TournamentsApi.ts#L87)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`JoinRequest`](../../schema/type-aliases/JoinRequest.md)

The `JoinRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PlayerStatus`](../../schema/type-aliases/PlayerStatus.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
