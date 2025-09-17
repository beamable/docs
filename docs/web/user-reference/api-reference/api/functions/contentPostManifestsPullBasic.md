[beamable-sdk](../../modules.md) / [api](../README.md) / contentPostManifestsPullBasic

# Function: contentPostManifestsPullBasic()

> **contentPostManifestsPullBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ContentBasicManifestChecksums`](../../schema/type-aliases/ContentBasicManifestChecksums.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:150](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/ContentApi.ts#L150)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`PullAllManifestsRequest`](../../schema/type-aliases/PullAllManifestsRequest.md)

The `PullAllManifestsRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ContentBasicManifestChecksums`](../../schema/type-aliases/ContentBasicManifestChecksums.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
