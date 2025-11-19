[beamable-sdk](../../modules.md) / [api](../README.md) / realmsGetClientDefaultsBasic

# Function: realmsGetClientDefaultsBasic()

> **realmsGetClientDefaultsBasic**(`requester`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`RealmConfiguration`](../../schema/type-aliases/RealmConfiguration.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/RealmsApi.ts:388](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/RealmsApi.ts#L388)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`RealmConfiguration`](../../schema/type-aliases/RealmConfiguration.md)\>\>
