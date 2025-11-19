[beamable-sdk](../../modules.md) / [api](../README.md) / accountsPostPasswordUpdateInitBasic

# Function: accountsPostPasswordUpdateInitBasic()

> **accountsPostPasswordUpdateInitBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`EmptyResponse`](../../schema/type-aliases/EmptyResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AccountsApi.ts:362](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/AccountsApi.ts#L362)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`PasswordUpdateRequest`](../../schema/type-aliases/PasswordUpdateRequest.md)

The `PasswordUpdateRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`EmptyResponse`](../../schema/type-aliases/EmptyResponse.md)\>\>
