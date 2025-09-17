[beamable-sdk](../../modules.md) / [api](../README.md) / beamoGetStoragePerformanceBasic

# Function: beamoGetStoragePerformanceBasic()

> **beamoGetStoragePerformanceBasic**(`requester`, `granularity`, `storageObjectName`, `endDate?`, `period?`, `startDate?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PerformanceResponse`](../../schema/type-aliases/PerformanceResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:746](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/BeamoApi.ts#L746)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### granularity

`string`

The `granularity` parameter to include in the API request.

### storageObjectName

`string`

The `storageObjectName` parameter to include in the API request.

### endDate?

`string`

The `endDate` parameter to include in the API request.

### period?

`string`

The `period` parameter to include in the API request.

### startDate?

`string`

The `startDate` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PerformanceResponse`](../../schema/type-aliases/PerformanceResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
