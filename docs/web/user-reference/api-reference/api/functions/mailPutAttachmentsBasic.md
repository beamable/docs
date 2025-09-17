[beamable-sdk](../../modules.md) / [api](../README.md) / mailPutAttachmentsBasic

# Function: mailPutAttachmentsBasic()

> **mailPutAttachmentsBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailSuccessResponse`](../../schema/type-aliases/MailSuccessResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MailApi.ts:38](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/MailApi.ts#L38)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`AcceptMultipleAttachments`](../../schema/type-aliases/AcceptMultipleAttachments.md)

The `AcceptMultipleAttachments` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`MailSuccessResponse`](../../schema/type-aliases/MailSuccessResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
