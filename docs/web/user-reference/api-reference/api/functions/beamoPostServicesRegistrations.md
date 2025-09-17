[beamable-sdk](../../modules.md) / [api](../README.md) / beamoPostServicesRegistrations

# Function: beamoPostServicesRegistrations()

> **beamoPostServicesRegistrations**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2ServiceRegistrationResponse`](../../schema/type-aliases/BeamoV2ServiceRegistrationResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoApi.ts:302](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/BeamoApi.ts#L302)

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

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BeamoV2ServiceRegistrationResponse`](../../schema/type-aliases/BeamoV2ServiceRegistrationResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
