[beamable-sdk](../../modules.md) / [api](../README.md) / contentPostBinaryBasic

# Function: contentPostBinaryBasic()

> **contentPostBinaryBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SaveBinaryResponse`](../../schema/type-aliases/SaveBinaryResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:126](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/ContentApi.ts#L126)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`SaveBinaryRequest`](../../schema/type-aliases/SaveBinaryRequest.md)

The `SaveBinaryRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SaveBinaryResponse`](../../schema/type-aliases/SaveBinaryResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
