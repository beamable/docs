[beamable-sdk](../../modules.md) / [api](../README.md) / beamoGetManifestsBasic

# Function: beamoGetManifestsBasic()

> **beamoGetManifestsBasic**(`requester`, `archived?`, `limit?`, `offset?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoBasicGetManifestsResponse`](../../schema/type-aliases/BeamoBasicGetManifestsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:778](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoApi.ts#L778)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### archived?

`boolean`

The `archived` parameter to include in the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### offset?

`number`

The `offset` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoBasicGetManifestsResponse`](../../schema/type-aliases/BeamoBasicGetManifestsResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
