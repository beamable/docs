[beamable-sdk](../../modules.md) / [api](../README.md) / matchmakingGetMatchesById

# Function: matchmakingGetMatchesById()

> **matchmakingGetMatchesById**(`requester`, `id`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Match`](../../schema/type-aliases/Match.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/MatchmakingApi.ts:31](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/MatchmakingApi.ts#L31)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### id

`string`

Match ID

### gamertag?

`string`

Override the playerId of the requester. This is only necessary when not using a JWT bearer token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`Match`](../../schema/type-aliases/Match.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
