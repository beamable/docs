[beamable-sdk](../../modules.md) / [api](../README.md) / beamoDeleteOtelViewsByViewId

# Function: beamoDeleteOtelViewsByViewId()

> **beamoDeleteOtelViewsByViewId**(`requester`, `viewId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiBeamoOtelViewsDeleteBeamoOtelResponse`](../../schema/type-aliases/ApiBeamoOtelViewsDeleteBeamoOtelResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoOtelApi.ts:81](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoOtelApi.ts#L81)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### viewId

`string`

The `viewId` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiBeamoOtelViewsDeleteBeamoOtelResponse`](../../schema/type-aliases/ApiBeamoOtelViewsDeleteBeamoOtelResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
