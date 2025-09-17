[beamable-sdk](../../modules.md) / [api](../README.md) / lobbiesGet

# Function: lobbiesGet()

> **lobbiesGet**(`requester`, `Limit?`, `MatchType?`, `Skip?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LobbyQueryResponse`](../../schema/type-aliases/LobbyQueryResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LobbyApi.ts:40](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/LobbyApi.ts#L40)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### Limit?

`number`

The `Limit` parameter to include in the API request.

### MatchType?

`string`

The `MatchType` parameter to include in the API request.

### Skip?

`number`

The `Skip` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`LobbyQueryResponse`](../../schema/type-aliases/LobbyQueryResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
