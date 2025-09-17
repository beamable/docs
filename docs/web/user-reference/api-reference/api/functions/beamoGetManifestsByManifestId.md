[beamable-sdk](../../modules.md) / [api](../README.md) / beamoGetManifestsByManifestId

# Function: beamoGetManifestsByManifestId()

> **beamoGetManifestsByManifestId**(`requester`, `manifestId`, `archived?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2Manifest`](../../schema/type-aliases/BeamoV2Manifest.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:135](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/BeamoApi.ts#L135)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### manifestId

`string`

The `manifestId` parameter to include in the API request.

### archived?

`boolean`

The `archived` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2Manifest`](../../schema/type-aliases/BeamoV2Manifest.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
