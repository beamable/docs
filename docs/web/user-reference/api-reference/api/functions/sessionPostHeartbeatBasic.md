[beamable-sdk](../../modules.md) / [api](../README.md) / sessionPostHeartbeatBasic

# Function: sessionPostHeartbeatBasic()

> **sessionPostHeartbeatBasic**(`requester`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SessionHeartbeat`](../../schema/type-aliases/SessionHeartbeat.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/SessionApi.ts:27](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/SessionApi.ts#L27)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`SessionHeartbeat`](../../schema/type-aliases/SessionHeartbeat.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
