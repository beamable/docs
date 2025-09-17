[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsGetTestProductBasic

# Function: paymentsGetTestProductBasic()

> **paymentsGetTestProductBasic**(`requester`, `sku`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetProductResponse`](../../schema/type-aliases/GetProductResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:1194](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L1194)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### sku

`string`

The `sku` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetProductResponse`](../../schema/type-aliases/GetProductResponse.md)\>\>
