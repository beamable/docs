[beamable-sdk](../../../../../modules.md) / [network/http/types/HttpResponse](../README.md) / HttpResponse

# Interface: HttpResponse<TRes\>

Defined in: [src/network/http/types/HttpResponse.ts:5](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/network/http/types/HttpResponse.ts#L5)

Represents the structure of an HTTP response.

## Type Parameters

### TRes

`TRes` = `any`

The expected type of the response payload.

## Properties

### body

> **body**: `TRes`

Defined in: [src/network/http/types/HttpResponse.ts:13](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/network/http/types/HttpResponse.ts#L13)

The response payload parsed into the expected type TRes.

***

### headers

> **headers**: `Record`<`string`, `string`\>

Defined in: [src/network/http/types/HttpResponse.ts:10](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/network/http/types/HttpResponse.ts#L10)

A collection of HTTP headers included in the response.

***

### status

> **status**: `number`

Defined in: [src/network/http/types/HttpResponse.ts:7](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/network/http/types/HttpResponse.ts#L7)

The HTTP status code returned by the server (e.g., 200, 404, 500).
