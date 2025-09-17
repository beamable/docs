[beamable-sdk](../../modules.md) / [api](../README.md) / authGetTokenListBasic

# Function: authGetTokenListBasic()

> **authGetTokenListBasic**(`requester`, `gamerTagOrAccountId`, `page`, `pageSize`, `cid?`, `pid?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ListTokenResponse`](../../schema/type-aliases/ListTokenResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AuthApi.ts:162](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/AuthApi.ts#L162)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamerTagOrAccountId

The `gamerTagOrAccountId` parameter to include in the API request.

`string` | `bigint`

### page

`number`

The `page` parameter to include in the API request.

### pageSize

`number`

The `pageSize` parameter to include in the API request.

### cid?

The `cid` parameter to include in the API request.

`string` | `bigint`

### pid?

`string`

The `pid` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ListTokenResponse`](../../schema/type-aliases/ListTokenResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
