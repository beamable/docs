[beamable-sdk](../../modules.md) / [api](../README.md) / lobbiesPost

# Function: lobbiesPost()

> **lobbiesPost**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Lobby`](../../schema/type-aliases/Lobby.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LobbyApi.ts:68](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/LobbyApi.ts#L68)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`CreateLobby`](../../schema/type-aliases/CreateLobby.md)

The `CreateLobby` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Lobby`](../../schema/type-aliases/Lobby.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
