[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsPostSteamPurchaseCancelBasic

# Function: paymentsPostSteamPurchaseCancelBasic()

> **paymentsPostSteamPurchaseCancelBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:1022](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L1022)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`CancelPurchaseRequest`](../../schema/type-aliases/CancelPurchaseRequest.md)

The `CancelPurchaseRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
