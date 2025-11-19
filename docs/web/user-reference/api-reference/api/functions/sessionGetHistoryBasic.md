[beamable-sdk](../../modules.md) / [api](../README.md) / sessionGetHistoryBasic

# Function: sessionGetHistoryBasic()

> **sessionGetHistoryBasic**(`requester`, `dbid`, `month?`, `year?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SessionHistoryResponse`](../../schema/type-aliases/SessionHistoryResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SessionApi.ts:52](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SessionApi.ts#L52)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### dbid

The `dbid` parameter to include in the API request.

`string` | `bigint`

### month?

`number`

The `month` parameter to include in the API request.

### year?

`number`

The `year` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SessionHistoryResponse`](../../schema/type-aliases/SessionHistoryResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
