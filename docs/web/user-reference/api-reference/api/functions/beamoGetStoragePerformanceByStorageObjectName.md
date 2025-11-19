[beamable-sdk](../../modules.md) / [api](../README.md) / beamoGetStoragePerformanceByStorageObjectName

# Function: beamoGetStoragePerformanceByStorageObjectName()

> **beamoGetStoragePerformanceByStorageObjectName**(`requester`, `storageObjectName`, `EndTime?`, `Granularity?`, `Period?`, `StartTime?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2StoragePerformance`](../../schema/type-aliases/BeamoV2StoragePerformance.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:547](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoApi.ts#L547)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### storageObjectName

`string`

The `storageObjectName` parameter to include in the API request.

### EndTime?

`Date`

The `EndTime` parameter to include in the API request.

### Granularity?

`string`

The `Granularity` parameter to include in the API request.

### Period?

`string`

The `Period` parameter to include in the API request.

### StartTime?

`Date`

The `StartTime` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2StoragePerformance`](../../schema/type-aliases/BeamoV2StoragePerformance.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
