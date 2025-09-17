[beamable-sdk](../../modules.md) / [api](../README.md) / schedulerPutJobCancelByJobId

# Function: schedulerPutJobCancelByJobId()

> **schedulerPutJobCancelByJobId**(`requester`, `jobId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiSchedulerJobCancelPutSchedulerResponse`](../../schema/type-aliases/ApiSchedulerJobCancelPutSchedulerResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SchedulerApi.ts:360](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/SchedulerApi.ts#L360)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### jobId

`string`

The `jobId` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiSchedulerJobCancelPutSchedulerResponse`](../../schema/type-aliases/ApiSchedulerJobCancelPutSchedulerResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
