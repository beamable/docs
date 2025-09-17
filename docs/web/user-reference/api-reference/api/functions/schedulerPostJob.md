[beamable-sdk](../../modules.md) / [api](../README.md) / schedulerPostJob

# Function: schedulerPostJob()

> **schedulerPostJob**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobDefinitionView`](../../schema/type-aliases/JobDefinitionView.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SchedulerApi.ts:61](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/SchedulerApi.ts#L61)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`JobDefinitionSaveRequest`](../../schema/type-aliases/JobDefinitionSaveRequest.md)

The `JobDefinitionSaveRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobDefinitionView`](../../schema/type-aliases/JobDefinitionView.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
