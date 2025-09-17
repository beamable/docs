[beamable-sdk](../../modules.md) / [api](../README.md) / statsPostSearchExtendedBasic

# Function: statsPostSearchExtendedBasic()

> **statsPostSearchExtendedBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SearchExtendedResponse`](../../schema/type-aliases/SearchExtendedResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/StatsApi.ts:161](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/StatsApi.ts#L161)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`SearchExtendedRequest`](../../schema/type-aliases/SearchExtendedRequest.md)

The `SearchExtendedRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SearchExtendedResponse`](../../schema/type-aliases/SearchExtendedResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
