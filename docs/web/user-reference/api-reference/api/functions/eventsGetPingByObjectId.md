[beamable-sdk](../../modules.md) / [api](../README.md) / eventsGetPingByObjectId

# Function: eventsGetPingByObjectId()

> **eventsGetPingByObjectId**(`requester`, `objectId`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PingRsp`](../../schema/type-aliases/PingRsp.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/EventsApi.ts:178](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/EventsApi.ts#L178)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### objectId

`string`

Format: events.event_content_id.event_started_timestamp

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`PingRsp`](../../schema/type-aliases/PingRsp.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
