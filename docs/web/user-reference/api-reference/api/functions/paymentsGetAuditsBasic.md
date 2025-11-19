[beamable-sdk](../../modules.md) / [api](../README.md) / paymentsGetAuditsBasic

# Function: paymentsGetAuditsBasic()

> **paymentsGetAuditsBasic**(`requester`, `limit?`, `player?`, `provider?`, `providerid?`, `start?`, `state?`, `txid?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ListAuditResponse`](../../schema/type-aliases/ListAuditResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PaymentsApi.ts:64](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/PaymentsApi.ts#L64)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### player?

The `player` parameter to include in the API request.

`string` | `bigint`

### provider?

`string`

The `provider` parameter to include in the API request.

### providerid?

`string`

The `providerid` parameter to include in the API request.

### start?

`number`

The `start` parameter to include in the API request.

### state?

`string`

The `state` parameter to include in the API request.

### txid?

The `txid` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ListAuditResponse`](../../schema/type-aliases/ListAuditResponse.md)\>\>
