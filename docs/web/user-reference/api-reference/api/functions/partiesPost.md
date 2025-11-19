[beamable-sdk](../../modules.md) / [api](../README.md) / partiesPost

# Function: partiesPost()

> **partiesPost**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/PartyApi.ts:36](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/PartyApi.ts#L36)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`CreateParty`](../../schema/type-aliases/CreateParty.md)

The `CreateParty` instance to use for the API request

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Party`](../../schema/type-aliases/Party.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
