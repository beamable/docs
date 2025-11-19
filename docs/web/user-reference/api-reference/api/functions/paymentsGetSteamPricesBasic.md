[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsGetSteamPricesBasic

# Function: paymentsGetSteamPricesBasic()

> **paymentsGetSteamPricesBasic**(`requester`, `steamId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LocalizedPriceMap`](../../schema/type-aliases/LocalizedPriceMap.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:557](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/PaymentsApi.ts#L557)

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

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LocalizedPriceMap`](../../schema/type-aliases/LocalizedPriceMap.md)\>\>
