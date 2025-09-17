[beamable-sdk](../../../../../modules.md) / [network/http/types/HttpRequest](../README.md) / HttpRequest

# Interface: HttpRequest<TReq\>

Defined in: [src/network/http/types/HttpRequest.ts:7](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L7)

Describes the configuration for an HTTP request.

## Type Parameters

### TReq

`TReq` = `any`

The expected type of the request body.

## Properties

### body?

> `optional` **body**: `TReq`

Defined in: [src/network/http/types/HttpRequest.ts:21](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L21)

The payload to send with the request, of type TReq.

***

### headers?

> `optional` **headers**: `Record`<`string`, `string`\>

Defined in: [src/network/http/types/HttpRequest.ts:18](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L18)

A collection of HTTP headers to include with the request.

***

### method?

> `optional` **method**: [`HttpMethod`](../../HttpMethod/type-aliases/HttpMethod.md)

Defined in: [src/network/http/types/HttpRequest.ts:15](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L15)

The HTTP method to use for the request (e.g., 'GET', 'POST', 'PUT', 'PATCH', 'DELETE').
If omitted, the requester will assume a default (often 'GET').

***

### url

> **url**: `string`

Defined in: [src/network/http/types/HttpRequest.ts:9](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L9)

The URL for the request. Can be a full URL or a path relative to the base URL.

***

### withAuth?

> `optional` **withAuth**: `boolean`

Defined in: [src/network/http/types/HttpRequest.ts:27](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequest.ts#L27)

Whether to automatically include an authorization token (e.g., Bearer token)
in the request headers. Implementations should respect this flag.
