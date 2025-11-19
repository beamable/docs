[beamable-sdk](../../modules.md) / [api](../README.md) / groupsDeleteMemberByObjectId

# Function: groupsDeleteMemberByObjectId()

> **groupsDeleteMemberByObjectId**(`requester`, `objectId`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GroupMembershipResponse`](../../schema/type-aliases/GroupMembershipResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/GroupsApi.ts:164](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/GroupsApi.ts#L164)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### payload

[`KickRequest`](../../schema/type-aliases/KickRequest.md)

The `KickRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GroupMembershipResponse`](../../schema/type-aliases/GroupMembershipResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
