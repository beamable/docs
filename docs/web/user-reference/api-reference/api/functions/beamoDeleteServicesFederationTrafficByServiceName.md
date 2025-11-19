[beamable-sdk](../../modules.md) / [api](../README.md) / beamoDeleteServicesFederationTrafficByServiceName

# Function: beamoDeleteServicesFederationTrafficByServiceName()

> **beamoDeleteServicesFederationTrafficByServiceName**(`requester`, `serviceName`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2EmptyMessage`](../../schema/type-aliases/BeamoV2EmptyMessage.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:376](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoApi.ts#L376)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### serviceName

`string`

The `serviceName` parameter to include in the API request.

### payload

[`BeamoV2DeleteRegistrationRequest`](../../schema/type-aliases/BeamoV2DeleteRegistrationRequest.md)

The `BeamoV2DeleteRegistrationRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2EmptyMessage`](../../schema/type-aliases/BeamoV2EmptyMessage.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
