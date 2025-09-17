[beamable-sdk](../../modules.md) / [api](../README.md) / schedulerGetJobsPaged

# Function: schedulerGetJobsPaged()

> **schedulerGetJobsPaged**(`requester`, `cursor?`, `name?`, `onlyUnique?`, `source?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobDefinitionViewCursorPagedResult`](../../schema/type-aliases/JobDefinitionViewCursorPagedResult.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SchedulerApi.ts:145](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/SchedulerApi.ts#L145)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### cursor?

`string`

The `cursor` parameter to include in the API request.

### name?

`string`

The `name` parameter to include in the API request.

### onlyUnique?

`boolean`

The `onlyUnique` parameter to include in the API request.

### source?

`string`

The `source` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`JobDefinitionViewCursorPagedResult`](../../schema/type-aliases/JobDefinitionViewCursorPagedResult.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
