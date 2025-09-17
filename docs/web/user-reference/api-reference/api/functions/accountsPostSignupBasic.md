[beamable-sdk](../../modules.md) / [api](../README.md) / accountsPostSignupBasic

# Function: accountsPostSignupBasic()

> **accountsPostSignupBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CreateAccountWithCredsApiResponse`](../../schema/type-aliases/CreateAccountWithCredsApiResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AccountsApi.ts:429](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/AccountsApi.ts#L429)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`CreateAccountWithCredsRequest`](../../schema/type-aliases/CreateAccountWithCredsRequest.md)

The `CreateAccountWithCredsRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CreateAccountWithCredsApiResponse`](../../schema/type-aliases/CreateAccountWithCredsApiResponse.md)\>\>
