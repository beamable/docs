[beamable-sdk](../../modules.md) / [api](../README.md) / sessionPostBasic

# Function: sessionPostBasic()

> **sessionPostBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`StartSessionResponse`](../../schema/type-aliases/StartSessionResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SessionApi.ts:136](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SessionApi.ts#L136)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`StartSessionRequest`](../../schema/type-aliases/StartSessionRequest.md)

The `StartSessionRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`StartSessionResponse`](../../schema/type-aliases/StartSessionResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
