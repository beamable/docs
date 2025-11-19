[beamable-sdk](../../modules.md) / [api](../README.md) / commercePostSkusBasic

# Function: commercePostSkusBasic()

> **commercePostSkusBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ResultResponse`](../../schema/type-aliases/ResultResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/CommerceApi.ts:112](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/CommerceApi.ts#L112)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`SaveSKUsRequest`](../../schema/type-aliases/SaveSKUsRequest.md)

The `SaveSKUsRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ResultResponse`](../../schema/type-aliases/ResultResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
