[beamable-sdk](../../modules.md) / [api](../README.md) / contentGetManifestPrivateBasic

# Function: contentGetManifestPrivateBasic()

> **contentGetManifestPrivateBasic**(`requester`, `id?`, `uid?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ClientManifestResponse`](../../schema/type-aliases/ClientManifestResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:559](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/ContentApi.ts#L559)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id?

`string`

ID of the content manifest

### uid?

`string`

UID of the content manifest

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ClientManifestResponse`](../../schema/type-aliases/ClientManifestResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
