[beamable-sdk](../../modules.md) / [api](../README.md) / announcementsGetListBasic

# Function: announcementsGetListBasic()

> **announcementsGetListBasic**(`requester`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AnnouncementContentResponse`](../../schema/type-aliases/AnnouncementContentResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AnnouncementsApi.ts:61](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/AnnouncementsApi.ts#L61)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AnnouncementContentResponse`](../../schema/type-aliases/AnnouncementContentResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
