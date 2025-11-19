[beamable-sdk](../../modules.md) / [api](../README.md) / contentGetManifestPublicJsonBasic

# Function: contentGetManifestPublicJsonBasic()

> **contentGetManifestPublicJsonBasic**(`requester`, `id?`, `uid?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ClientManifestJsonResponse`](../../schema/type-aliases/ClientManifestJsonResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:480](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/ContentApi.ts#L480)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id?

`string`

Content ID of the content manifest

### uid?

`string`

UID of the content manifest

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ClientManifestJsonResponse`](../../schema/type-aliases/ClientManifestJsonResponse.md)\>\>
