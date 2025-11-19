[beamable-sdk](../../modules.md) / [api](../README.md) / statsPostSearchBasic

# Function: statsPostSearchBasic()

> **statsPostSearchBasic**(`requester`, `payload`, `gamertag?`): `Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`StatsSearchResponse`](../../schema/type-aliases/StatsSearchResponse.md)\>\>

Defined in: [src/\_\_generated\_\_/apis/StatsApi.ts:137](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/apis/StatsApi.ts#L137)

## Parameters

### requester

[`HttpRequester`](../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

The `HttpRequester` type to use for the API request.

### payload

[`StatsSearchRequest`](../../schema/type-aliases/StatsSearchRequest.md)

The `StatsSearchRequest` instance to use for the API request

### gamertag?

`string`

Override the Gamer Tag of the player. This is generally inferred by the auth token.

## Returns

`Promise`<[`HttpResponse`](../../network/http/types/HttpResponse/interfaces/HttpResponse.md)<[`StatsSearchResponse`](../../schema/type-aliases/StatsSearchResponse.md)\>\>

## Remarks

**Authentication:**
This method requires a valid bearer token in the `Authorization` header.
