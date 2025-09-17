[beamable-sdk](../../modules.md) / [api](../README.md) / cloudsavingGetBasic

# Function: cloudsavingGetBasic()

> **cloudsavingGetBasic**(`requester`, `playerId?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CloudsavingBasicManifest`](../../schema/type-aliases/CloudsavingBasicManifest.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/CloudsavingApi.ts:244](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/CloudsavingApi.ts#L244)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### playerId?

The `playerId` parameter to include in the API request.

`string` | `bigint`

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`CloudsavingBasicManifest`](../../schema/type-aliases/CloudsavingBasicManifest.md)\>\>
