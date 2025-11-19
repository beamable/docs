[beamable-sdk](../../modules.md) / [api](../README.md) / realmsGetCustomerActivateBasic

# Function: realmsGetCustomerActivateBasic()

> **realmsGetCustomerActivateBasic**(`requester`, `cid`, `token`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`HtmlResponse`](../../schema/type-aliases/HtmlResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/RealmsApi.ts:52](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/RealmsApi.ts#L52)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### cid

The `cid` parameter to include in the API request.

`string` | `bigint`

### token

`string`

The `token` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`HtmlResponse`](../../schema/type-aliases/HtmlResponse.md)\>\>
