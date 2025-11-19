[beamable-sdk](../../modules.md) / [api](../README.md) / socialGetBasic

# Function: socialGetBasic()

> **socialGetBasic**(`requester`, `playerIds`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetSocialStatusesResponse`](../../schema/type-aliases/GetSocialStatusesResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SocialApi.ts:174](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SocialApi.ts#L174)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### playerIds

`string`[]

The `playerIds` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`GetSocialStatusesResponse`](../../schema/type-aliases/GetSocialStatusesResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
