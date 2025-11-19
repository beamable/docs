[beamable-sdk](../../modules.md) / [api](../README.md) / commerceGetOffersAdminByObjectId

# Function: commerceGetOffersAdminByObjectId()

> **commerceGetOffersAdminByObjectId**(`requester`, `objectId`, `language?`, `stores?`, `time?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetActiveOffersResponse`](../../schema/type-aliases/GetActiveOffersResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/CommerceApi.ts:214](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/CommerceApi.ts#L214)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### language?

`string`

The `language` parameter to include in the API request.

### stores?

`string`

The `stores` parameter to include in the API request.

### time?

`string`

The `time` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetActiveOffersResponse`](../../schema/type-aliases/GetActiveOffersResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
