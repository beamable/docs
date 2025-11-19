[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsPostFacebookPurchaseBeginBasic

# Function: paymentsPostFacebookPurchaseBeginBasic()

> **paymentsPostFacebookPurchaseBeginBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeginPurchaseResponse`](../../schema/type-aliases/BeginPurchaseResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:749](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/PaymentsApi.ts#L749)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`BeginPurchaseRequest`](../../schema/type-aliases/BeginPurchaseRequest.md)

The `BeginPurchaseRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeginPurchaseResponse`](../../schema/type-aliases/BeginPurchaseResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
