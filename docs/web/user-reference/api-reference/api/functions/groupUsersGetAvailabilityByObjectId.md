[beamable-sdk](../../modules.md) / [api](../README.md) / groupUsersGetAvailabilityByObjectId

# Function: groupUsersGetAvailabilityByObjectId()

> **groupUsersGetAvailabilityByObjectId**(`requester`, `objectId`, `type`, `name?`, `subGroup?`, `tag?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AvailabilityResponse`](../../schema/type-aliases/AvailabilityResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/GroupUsersApi.ts:37](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/GroupUsersApi.ts#L37)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### type

[`GroupType`](../../schema/enumerations/GroupType.md)

The `type` parameter to include in the API request.

### name?

`string`

The `name` parameter to include in the API request.

### subGroup?

`boolean`

The `subGroup` parameter to include in the API request.

### tag?

`string`

The `tag` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AvailabilityResponse`](../../schema/type-aliases/AvailabilityResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
