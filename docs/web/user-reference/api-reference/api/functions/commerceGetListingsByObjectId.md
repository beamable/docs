[beamable-sdk](../../modules.md) / [api](../README.md) / commerceGetListingsByObjectId

# Function: commerceGetListingsByObjectId()

> **commerceGetListingsByObjectId**(`requester`, `objectId`, `listing`, `store?`, `time?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ActiveListingResponse`](../../schema/type-aliases/ActiveListingResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/CommerceApi.ts:295](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/CommerceApi.ts#L295)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### listing

`string`

The `listing` parameter to include in the API request.

### store?

`string`

The `store` parameter to include in the API request.

### time?

`string`

The `time` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ActiveListingResponse`](../../schema/type-aliases/ActiveListingResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
