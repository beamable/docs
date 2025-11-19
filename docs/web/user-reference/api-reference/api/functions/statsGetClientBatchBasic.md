[beamable-sdk](../../modules.md) / [api](../README.md) / statsGetClientBatchBasic

# Function: statsGetClientBatchBasic()

> **statsGetClientBatchBasic**(`requester`, `objectIds`, `format?`, `stats?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BatchReadStatsResponse`](../../schema/type-aliases/BatchReadStatsResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/StatsApi.ts:86](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/StatsApi.ts#L86)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectIds

`string`

The `objectIds` parameter to include in the API request.

### format?

`string`

The `format` parameter to include in the API request.

### stats?

`string`

The `stats` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`BatchReadStatsResponse`](../../schema/type-aliases/BatchReadStatsResponse.md)\>\>
