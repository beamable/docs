[beamable-sdk](../../modules.md) / [api](../README.md) / trialsGetAdminDataBasic

# Function: trialsGetAdminDataBasic()

> **trialsGetAdminDataBasic**(`requester`, `id`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetS3DataResponse`](../../schema/type-aliases/GetS3DataResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/TrialsApi.ts:36](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/TrialsApi.ts#L36)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id

The `id` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetS3DataResponse`](../../schema/type-aliases/GetS3DataResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
