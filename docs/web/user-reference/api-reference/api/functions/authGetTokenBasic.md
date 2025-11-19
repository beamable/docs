[beamable-sdk](../../modules.md) / [api](../README.md) / authGetTokenBasic

# Function: authGetTokenBasic()

> **authGetTokenBasic**(`requester`, `token`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Token`](../../schema/type-aliases/Token.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AuthApi.ts:188](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/AuthApi.ts#L188)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### token

`string`

The `token` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Token`](../../schema/type-aliases/Token.md)\>\>
