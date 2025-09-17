[beamable-sdk](../../modules.md) / [api](../README.md) / beamoPutOtelViewsByViewId

# Function: beamoPutOtelViewsByViewId()

> **beamoPutOtelViewsByViewId**(`requester`, `viewId`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OtelView`](../../schema/type-aliases/OtelView.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoOtelApi.ts:105](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/BeamoOtelApi.ts#L105)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### viewId

`string`

The `viewId` parameter to include in the API request.

### payload

[`UpdateOtelViewRequest`](../../schema/type-aliases/UpdateOtelViewRequest.md)

The `UpdateOtelViewRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OtelView`](../../schema/type-aliases/OtelView.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
