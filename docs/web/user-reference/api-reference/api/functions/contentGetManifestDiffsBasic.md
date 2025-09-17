[beamable-sdk](../../modules.md) / [api](../README.md) / contentGetManifestDiffsBasic

# Function: contentGetManifestDiffsBasic()

> **contentGetManifestDiffsBasic**(`requester`, `manifestId`, `fromDate?`, `fromUid?`, `limit?`, `offset?`, `toDate?`, `toUid?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetManifestDiffsResponse`](../../schema/type-aliases/GetManifestDiffsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/ContentApi.ts:380](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/ContentApi.ts#L380)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### manifestId

`string`

The `manifestId` parameter to include in the API request.

### fromDate?

The `fromDate` parameter to include in the API request.

`string` | `bigint`

### fromUid?

`string`

The `fromUid` parameter to include in the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### offset?

`number`

The `offset` parameter to include in the API request.

### toDate?

The `toDate` parameter to include in the API request.

`string` | `bigint`

### toUid?

`string`

The `toUid` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetManifestDiffsResponse`](../../schema/type-aliases/GetManifestDiffsResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
