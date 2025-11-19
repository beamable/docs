[beamable-sdk](../../modules.md) / [api](../README.md) / mailGetDetailByObjectId

# Function: mailGetDetailByObjectId()

> **mailGetDetailByObjectId**(`requester`, `objectId`, `mid`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailResponse`](../../schema/type-aliases/MailResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MailApi.ts:155](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/MailApi.ts#L155)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### mid

The `mid` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailResponse`](../../schema/type-aliases/MailResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
