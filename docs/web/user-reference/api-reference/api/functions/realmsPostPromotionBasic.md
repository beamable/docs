[beamable-sdk](../../modules.md) / [api](../README.md) / realmsPostPromotionBasic

# Function: realmsPostPromotionBasic()

> **realmsPostPromotionBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PromoteRealmResponse`](../../schema/type-aliases/PromoteRealmResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/RealmsApi.ts:787](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/RealmsApi.ts#L787)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`PromoteRealmRequest`](../../schema/type-aliases/PromoteRealmRequest.md)

The `PromoteRealmRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PromoteRealmResponse`](../../schema/type-aliases/PromoteRealmResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
