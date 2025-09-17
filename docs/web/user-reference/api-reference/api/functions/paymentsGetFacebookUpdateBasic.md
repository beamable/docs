[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsGetFacebookUpdateBasic

# Function: paymentsGetFacebookUpdateBasic()

> **paymentsGetFacebookUpdateBasic**(`requester`, `hubChallenge`, `hubMode`, `hubVerifyToken`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SubscriptionVerificationResponse`](../../schema/type-aliases/SubscriptionVerificationResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:136](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PaymentsApi.ts#L136)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### hubChallenge

`string`

The `hubChallenge` parameter to include in the API request.

### hubMode

`string`

The `hubMode` parameter to include in the API request.

### hubVerifyToken

`string`

The `hubVerifyToken` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SubscriptionVerificationResponse`](../../schema/type-aliases/SubscriptionVerificationResponse.md)\>\>
