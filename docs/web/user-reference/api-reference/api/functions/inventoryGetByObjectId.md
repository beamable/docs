[beamable-sdk](../../modules.md) / [api](../README.md) / inventoryGetByObjectId

# Function: inventoryGetByObjectId()

> **inventoryGetByObjectId**(`requester`, `objectId`, `scope?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`InventoryView`](../../schema/type-aliases/InventoryView.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/InventoryApi.ts:154](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/InventoryApi.ts#L154)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### scope?

`string`

The `scope` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`InventoryView`](../../schema/type-aliases/InventoryView.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
