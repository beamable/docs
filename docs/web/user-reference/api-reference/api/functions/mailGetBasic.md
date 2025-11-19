[beamable-sdk](../../modules.md) / [api](../README.md) / mailGetBasic

# Function: mailGetBasic()

> **mailGetBasic**(`requester`, `mid`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailResponse`](../../schema/type-aliases/MailResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MailApi.ts:81](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/MailApi.ts#L81)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### mid

The `mid` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailResponse`](../../schema/type-aliases/MailResponse.md)\>\>
