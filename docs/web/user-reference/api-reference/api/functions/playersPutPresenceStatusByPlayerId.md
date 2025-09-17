[beamable-sdk](../../modules.md) / [api](../README.md) / playersPutPresenceStatusByPlayerId

# Function: playersPutPresenceStatusByPlayerId()

> **playersPutPresenceStatusByPlayerId**(`requester`, `playerId`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OnlineStatus`](../../schema/type-aliases/OnlineStatus.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PlayerApi.ts:74](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PlayerApi.ts#L74)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### playerId

`string`

The `playerId` parameter to include in the API request.

### payload

[`SetPresenceStatusRequest`](../../schema/type-aliases/SetPresenceStatusRequest.md)

The `SetPresenceStatusRequest` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`OnlineStatus`](../../schema/type-aliases/OnlineStatus.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
