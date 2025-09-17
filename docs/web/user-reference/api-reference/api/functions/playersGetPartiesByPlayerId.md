[beamable-sdk](../../modules.md) / [api](../README.md) / playersGetPartiesByPlayerId

# Function: playersGetPartiesByPlayerId()

> **playersGetPartiesByPlayerId**(`requester`, `playerId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PlayerPartyApi.ts:27](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PlayerPartyApi.ts#L27)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### playerId

`string`

Player Id

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
