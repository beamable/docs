[beamable-sdk](../../modules.md) / [api](../README.md) / partiesGetById

# Function: partiesGetById()

> **partiesGetById**(`requester`, `id`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PartyApi.ts:85](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/apis/PartyApi.ts#L85)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id

`string`

Id of the party

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
