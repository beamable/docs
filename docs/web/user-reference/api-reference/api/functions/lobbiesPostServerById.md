[beamable-sdk](../../modules.md) / [api](../README.md) / lobbiesPostServerById

# Function: lobbiesPostServerById()

> **lobbiesPostServerById**(`requester`, `id`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiLobbiesServerPostLobbyResponse`](../../schema/type-aliases/ApiLobbiesServerPostLobbyResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/LobbyApi.ts:289](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/LobbyApi.ts#L289)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id

`string`

Id of the lobby

### payload

[`CreateFederatedGameServer`](../../schema/type-aliases/CreateFederatedGameServer.md)

The `CreateFederatedGameServer` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`ApiLobbiesServerPostLobbyResponse`](../../schema/type-aliases/ApiLobbiesServerPostLobbyResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
