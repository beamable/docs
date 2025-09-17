[beamable-sdk](../../modules.md) / [api](../README.md) / socialGetMyBasic

# Function: socialGetMyBasic()

> **socialGetMyBasic**(`requester`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Social`](../../schema/type-aliases/Social.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SocialApi.ts:31](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/SocialApi.ts#L31)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Social`](../../schema/type-aliases/Social.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
