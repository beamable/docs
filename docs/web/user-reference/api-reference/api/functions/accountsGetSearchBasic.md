[beamable-sdk](../../modules.md) / [api](../README.md) / accountsGetSearchBasic

# Function: accountsGetSearchBasic()

> **accountsGetSearchBasic**(`requester`, `page`, `pagesize`, `query`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountSearchResponse`](../../schema/type-aliases/AccountSearchResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AccountsApi.ts:172](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/AccountsApi.ts#L172)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### page

`number`

The `page` parameter to include in the API request.

### pagesize

`number`

The `pagesize` parameter to include in the API request.

### query

`string`

The `query` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountSearchResponse`](../../schema/type-aliases/AccountSearchResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
