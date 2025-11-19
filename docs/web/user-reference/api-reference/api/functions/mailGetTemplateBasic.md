[beamable-sdk](../../modules.md) / [api](../README.md) / mailGetTemplateBasic

# Function: mailGetTemplateBasic()

> **mailGetTemplateBasic**(`requester`, `gamerTag`, `templateName`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailTemplate`](../../schema/type-aliases/MailTemplate.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MailApi.ts:59](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/MailApi.ts#L59)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamerTag

The `gamerTag` parameter to include in the API request.

`string` | `bigint`

### templateName

`string`

The `templateName` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailTemplate`](../../schema/type-aliases/MailTemplate.md)\>\>
