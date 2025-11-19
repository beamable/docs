[beamable-sdk](../../modules.md) / [api](../README.md) / schedulerPostJobExecuteInternal

# Function: schedulerPostJobExecuteInternal()

> **schedulerPostJobExecuteInternal**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobExecutionResult`](../../schema/type-aliases/JobExecutionResult.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SchedulerApi.ts:37](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SchedulerApi.ts#L37)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`JobExecutionEvent`](../../schema/type-aliases/JobExecutionEvent.md)

The `JobExecutionEvent` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobExecutionResult`](../../schema/type-aliases/JobExecutionResult.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
