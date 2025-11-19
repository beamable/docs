[beamable-sdk](../../modules.md) / [api](../README.md) / authPostTokensRefreshToken

# Function: authPostTokensRefreshToken()

> **authPostTokensRefreshToken**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AuthResponse`](../../schema/type-aliases/AuthResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AuthApi.ts:62](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/AuthApi.ts#L62)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`RefreshTokenAuthRequest`](../../schema/type-aliases/RefreshTokenAuthRequest.md)

The `RefreshTokenAuthRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AuthResponse`](../../schema/type-aliases/AuthResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
