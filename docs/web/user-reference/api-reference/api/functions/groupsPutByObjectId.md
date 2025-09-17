[beamable-sdk](../../modules.md) / [api](../README.md) / groupsPutByObjectId

# Function: groupsPutByObjectId()

> **groupsPutByObjectId**(`requester`, `objectId`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CommonResponse`](../../schema/type-aliases/CommonResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/GroupsApi.ts:212](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/GroupsApi.ts#L212)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### payload

[`GroupUpdate`](../../schema/type-aliases/GroupUpdate.md)

The `GroupUpdate` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CommonResponse`](../../schema/type-aliases/CommonResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
