[beamable-sdk](../../modules.md) / [api](../README.md) / realmsGetPromotionBasic

# Function: realmsGetPromotionBasic()

> **realmsGetPromotionBasic**(`requester`, `sourcePid`, `contentManifestIds?`, `promotions?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PromoteRealmResponse`](../../schema/type-aliases/PromoteRealmResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/RealmsApi.ts:759](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/RealmsApi.ts#L759)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### sourcePid

`string`

The `sourcePid` parameter to include in the API request.

### contentManifestIds?

`string`[]

The `contentManifestIds` parameter to include in the API request.

### promotions?

`string`[]

The `promotions` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PromoteRealmResponse`](../../schema/type-aliases/PromoteRealmResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
