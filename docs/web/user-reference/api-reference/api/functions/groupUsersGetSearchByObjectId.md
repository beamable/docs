[beamable-sdk](../../modules.md) / [api](../README.md) / groupUsersGetSearchByObjectId

# Function: groupUsersGetSearchByObjectId()

> **groupUsersGetSearchByObjectId**(`requester`, `objectId`, `type`, `enrollmentTypes?`, `hasSlots?`, `limit?`, `name?`, `offset?`, `scoreMax?`, `scoreMin?`, `sortField?`, `sortValue?`, `subGroup?`, `userScore?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GroupSearchResponse`](../../schema/type-aliases/GroupSearchResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/GroupUsersApi.ts:176](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/GroupUsersApi.ts#L176)

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

### enrollmentTypes?

`string`

The `enrollmentTypes` parameter to include in the API request.

### hasSlots?

`boolean`

The `hasSlots` parameter to include in the API request.

### limit?

`number`

The `limit` parameter to include in the API request.

### name?

`string`

The `name` parameter to include in the API request.

### offset?

`number`

The `offset` parameter to include in the API request.

### scoreMax?

The `scoreMax` parameter to include in the API request.

`string` | `bigint`

### scoreMin?

The `scoreMin` parameter to include in the API request.

`string` | `bigint`

### sortField?

`string`

The `sortField` parameter to include in the API request.

### sortValue?

`number`

The `sortValue` parameter to include in the API request.

### subGroup?

`boolean`

The `subGroup` parameter to include in the API request.

### userScore?

The `userScore` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GroupSearchResponse`](../../schema/type-aliases/GroupSearchResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
