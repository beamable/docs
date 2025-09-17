[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsGetSteamProductsBasic

# Function: paymentsGetSteamProductsBasic()

> **paymentsGetSteamProductsBasic**(`requester`, `steamId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetProductsResponse`](../../schema/type-aliases/GetProductsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:997](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L997)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### steamId

The `steamId` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetProductsResponse`](../../schema/type-aliases/GetProductsResponse.md)\>\>
