[beamable-sdk](../../modules.md) / [api](../README.md) / accountsDeleteMeThirdPartyBasic

# Function: accountsDeleteMeThirdPartyBasic()

> **accountsDeleteMeThirdPartyBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AccountsApi.ts:125](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/AccountsApi.ts#L125)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`ThirdPartyAvailableRequest`](../../schema/type-aliases/ThirdPartyAvailableRequest.md)

The `ThirdPartyAvailableRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
