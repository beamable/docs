[beamable-sdk](../../modules.md) / [api](../README.md) / beamoPostOtelViews

# Function: beamoPostOtelViews()

> **beamoPostOtelViews**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OtelView`](../../schema/type-aliases/OtelView.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/BeamoOtelApi.ts:57](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/BeamoOtelApi.ts#L57)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`OtelView`](../../schema/type-aliases/OtelView.md)

The `OtelView` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OtelView`](../../schema/type-aliases/OtelView.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
