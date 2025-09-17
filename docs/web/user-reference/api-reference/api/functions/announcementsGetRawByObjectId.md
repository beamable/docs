[beamable-sdk](../../modules.md) / [api](../README.md) / announcementsGetRawByObjectId

# Function: announcementsGetRawByObjectId()

> **announcementsGetRawByObjectId**(`requester`, `objectId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AnnouncementRawResponse`](../../schema/type-aliases/AnnouncementRawResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AnnouncementsApi.ts:252](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/AnnouncementsApi.ts#L252)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

Gamertag of the player.Underlying objectId type is integer in format int64.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AnnouncementRawResponse`](../../schema/type-aliases/AnnouncementRawResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
