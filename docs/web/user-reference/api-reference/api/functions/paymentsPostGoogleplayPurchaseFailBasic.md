[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsPostGoogleplayPurchaseFailBasic

# Function: paymentsPostGoogleplayPurchaseFailBasic()

> **paymentsPostGoogleplayPurchaseFailBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:863](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L863)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`FailPurchaseRequest`](../../schema/type-aliases/FailPurchaseRequest.md)

The `FailPurchaseRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PaymentResultResponse`](../../schema/type-aliases/PaymentResultResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
