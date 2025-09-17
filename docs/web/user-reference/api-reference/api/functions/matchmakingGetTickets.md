[beamable-sdk](../../modules.md) / [api](../README.md) / matchmakingGetTickets

# Function: matchmakingGetTickets()

> **matchmakingGetTickets**(`requester`, `IncludeInactive?`, `Limit?`, `Players?`, `Skip?`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`TicketQueryResponse`](../../schema/type-aliases/TicketQueryResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MatchmakingApi.ts:57](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/MatchmakingApi.ts#L57)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### IncludeInactive?

`boolean`

The `IncludeInactive` parameter to include in the API request.

### Limit?

`number`

The `Limit` parameter to include in the API request.

### Players?

`string`[]

The `Players` parameter to include in the API request.

### Skip?

`number`

The `Skip` parameter to include in the API request.

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`TicketQueryResponse`](../../schema/type-aliases/TicketQueryResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
