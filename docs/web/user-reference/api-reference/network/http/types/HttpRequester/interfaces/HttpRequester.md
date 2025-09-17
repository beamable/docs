[beamable-sdk](../../../../../modules.md) / [network/http/types/HttpRequester](../README.md) / HttpRequester

# Interface: HttpRequester

Defined in: [src/network/http/types/HttpRequester.ts:5](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequester.ts#L5)

A pluggable HTTP client abstraction that can send requests and receive typed responses.

## Accessors

### baseUrl

#### Set Signature

> **set** **baseUrl**(`url`): `void`

Defined in: [src/network/http/types/HttpRequester.ts:18](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequester.ts#L18)

Overrides the base URL used for all subsequent requests.

##### Parameters

###### url

`string`

##### Returns

`void`

***

### defaultHeaders

#### Set Signature

> **set** **defaultHeaders**(`header`): `void`

Defined in: [src/network/http/types/HttpRequester.ts:21](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequester.ts#L21)

Sets the default headers to include on every request.

##### Parameters

###### header

`Record`<`string`, `string`\>

##### Returns

`void`

## Methods

### request()

> **request**<`TRes`, `TReq`\>(`req`): `Promise`<[`HttpResponse`](../../HttpResponse/interfaces/HttpResponse.md)<`TRes`\>\>

Defined in: [src/network/http/types/HttpRequester.ts:13](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/network/http/types/HttpRequester.ts#L13)

Sends an HTTP request and returns a typed response.

#### Type Parameters

##### TRes

`TRes` = `any`

The expected type of the response body.

##### TReq

`TReq` = `any`

The type of the request payload.

#### Parameters

##### req

[`HttpRequest`](../../HttpRequest/interfaces/HttpRequest.md)<`TReq`\>

Configuration for the HTTP request, including URL, method, headers, optional body, etc.

#### Returns

`Promise`<[`HttpResponse`](../../HttpResponse/interfaces/HttpResponse.md)<`TRes`\>\>

A promise that resolves with an HttpResponse containing status, headers, and the parsed body as TRes.
