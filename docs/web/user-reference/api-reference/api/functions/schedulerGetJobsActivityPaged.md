[beamable-sdk](../../modules.md) / [api](../README.md) / schedulerGetJobsActivityPaged

# Function: schedulerGetJobsActivityPaged()

> **schedulerGetJobsActivityPaged**(`requester`, `cursor?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobActivityViewCursorPagedResult`](../../schema/type-aliases/JobActivityViewCursorPagedResult.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SchedulerApi.ts:305](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SchedulerApi.ts#L305)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### cursor?

`string`

The `cursor` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobActivityViewCursorPagedResult`](../../schema/type-aliases/JobActivityViewCursorPagedResult.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
