[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsPostItunesPurchaseCompleteBasic

# Function: paymentsPostItunesPurchaseCompleteBasic()

> **paymentsPostItunesPurchaseCompleteBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:664](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L664)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`CompletePurchaseRequest`](../../schema/type-aliases/CompletePurchaseRequest.md)

The `CompletePurchaseRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>
