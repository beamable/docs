[beamable-sdk](../../modules.md) / [api](../README.md) / accountsGetGetPersonallyIdentifiableInformationBasic

# Function: accountsGetGetPersonallyIdentifiableInformationBasic()

> **accountsGetGetPersonallyIdentifiableInformationBasic**(`requester`, `query`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountPersonallyIdentifiableInformationResponse`](../../schema/type-aliases/AccountPersonallyIdentifiableInformationResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/AccountsApi.ts:145](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/AccountsApi.ts#L145)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### query

`string`

The `query` parameter to include in the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`AccountPersonallyIdentifiableInformationResponse`](../../schema/type-aliases/AccountPersonallyIdentifiableInformationResponse.md)\>\>
