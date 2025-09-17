[beamable-sdk](../../modules.md) / [api](../README.md) / contentGetManifestHistoryBasic

# Function: contentGetManifestHistoryBasic()

> **contentGetManifestHistoryBasic**(`requester`, `id?`, `limit?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetManifestHistoryResponse`](../../schema/type-aliases/GetManifestHistoryResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:99](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/ContentApi.ts#L99)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id?

`string`

The `id` parameter to include in the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetManifestHistoryResponse`](../../schema/type-aliases/GetManifestHistoryResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
