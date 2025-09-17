[beamable-sdk](../../../modules.md) / [core/BeamBase](../README.md) / BeamBase

# Abstract Class: BeamBase

Defined in: [src/core/BeamBase.ts:30](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L30)

The base class for Beam SDK client and server instances.

## Extended by

- [`Beam`](../../Beam/classes/Beam.md)
- [`BeamServer`](../../BeamServer/classes/BeamServer.md)

## Properties

### cid

> **cid**: `string`

Defined in: [src/core/BeamBase.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L34)

The Beamable Customer ID.

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamBase.ts:36](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L36)

The Beamable Project ID.

***

### requester

> `readonly` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamBase.ts:32](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L32)

The HTTP requester instance used by the Beam SDK.

***

### tokenStorage

> **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/core/BeamBase.ts:42](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L42)

The token storage instance used by the client SDK.
Defaults to `BrowserTokenStorage` in browser environments and `NodeTokenStorage` in Node.js environments.
Can be overridden via the `tokenStorage` option in the `BeamConfig`.

## Accessors

### env

#### Get Signature

> **get** `static` **env**(): [`BeamEnvVars`](../interfaces/BeamEnvVars.md)

Defined in: [src/core/BeamBase.ts:67](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L67)

Environment variables that can be set to configure the Beam SDK.

##### Remarks

These values **must** be supplied at runtime via real environment variables
(e.g. `process.env.REALM_SECRET`), and **must not** be committed directly into your source code.

##### Example

```ts
BeamBase.env.REALM_SECRET = process.env.REALM_SECRET;
const beam = await Beam.init({ ... });
```

##### Returns

[`BeamEnvVars`](../interfaces/BeamEnvVars.md)

## Methods

### use()

#### Call Signature

> `abstract` **use**<`T`\>(`Service`): `this`

Defined in: [src/core/BeamBase.ts:84](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L84)

Dynamically adds a service to the Beam SDK instance.

##### Type Parameters

###### T

`T` *extends* [`ApiService`](../../../services/classes/ApiService.md)

##### Parameters

###### Service

[`ApiServiceCtor`](../../../services/type-aliases/ApiServiceCtor.md)<`T`\>

The service class to add.

##### Returns

`this`

##### Example

```ts
// client-side:
beam.use(StatsService);
await beam.stats.get({...});
// server-side:
beamServer.use(StatsService);
await beamServer.stats.get({...});
```

#### Call Signature

> `abstract` **use**<`T`\>(`Client`): `this`

Defined in: [src/core/BeamBase.ts:99](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L99)

Dynamically adds a microservice client to the Beam SDK instance.

##### Type Parameters

###### T

`T` *extends* [`BeamMicroServiceClient`](../../BeamMicroServiceClient/classes/BeamMicroServiceClient.md)

##### Parameters

###### Client

[`BeamMicroServiceClientCtor`](../../BeamMicroServiceClient/type-aliases/BeamMicroServiceClientCtor.md)<`T`\>

The microservice client class to add.

##### Returns

`this`

##### Example

```ts
// client-side:
beam.use(MyMicroServiceClient);
beam.myMicroServiceClient.serviceName;
// server-side:
beamServer.use(MyMicroServiceClient);
beamServer.myMicroServiceClient.serviceName;
```
