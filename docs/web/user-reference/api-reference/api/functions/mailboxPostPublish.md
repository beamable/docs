[beamable-sdk](../../modules.md) / [api](../README.md) / mailboxPostPublish

# Function: mailboxPostPublish()

> **mailboxPostPublish**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiMailboxPublishPostMailboxResponse`](../../schema/type-aliases/ApiMailboxPublishPostMailboxResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MailboxApi.ts:23](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/MailboxApi.ts#L23)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`MessageRequest`](../../schema/type-aliases/MessageRequest.md)

The `MessageRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiMailboxPublishPostMailboxResponse`](../../schema/type-aliases/ApiMailboxPublishPostMailboxResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
