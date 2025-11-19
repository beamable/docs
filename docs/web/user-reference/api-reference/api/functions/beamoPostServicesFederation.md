[beamable-sdk](../../modules.md) / [api](../README.md) / beamoPostServicesFederation

# Function: beamoPostServicesFederation()

> **beamoPostServicesFederation**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2FederationRegistrationResponse`](../../schema/type-aliases/BeamoV2FederationRegistrationResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:326](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoApi.ts#L326)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`BeamoV2ServiceRegistrationQuery`](../../schema/type-aliases/BeamoV2ServiceRegistrationQuery.md)

The `BeamoV2ServiceRegistrationQuery` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2FederationRegistrationResponse`](../../schema/type-aliases/BeamoV2FederationRegistrationResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
