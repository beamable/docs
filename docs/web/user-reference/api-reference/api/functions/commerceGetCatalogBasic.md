[beamable-sdk](../../modules.md) / [api](../README.md) / commerceGetCatalogBasic

# Function: commerceGetCatalogBasic()

> **commerceGetCatalogBasic**(`requester`, `version?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetCatalogResponse`](../../schema/type-aliases/GetCatalogResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/CommerceApi.ts:65](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/CommerceApi.ts#L65)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### version?

The `version` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetCatalogResponse`](../../schema/type-aliases/GetCatalogResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
