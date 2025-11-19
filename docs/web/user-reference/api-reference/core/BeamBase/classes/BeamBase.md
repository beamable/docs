[beamable-sdk](../../../modules.md) / [core/BeamBase](../README.md) / BeamBase

# Abstract Class: BeamBase

Defined in: [src/core/BeamBase.ts:30](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L30)

The base class for Beam SDK client and server instances.

## Extended by

- [`Beam`](../../Beam/classes/Beam.md)
- [`BeamServer`](../../BeamServer/classes/BeamServer.md)

## Properties

### cid

> **cid**: `string`

Defined in: [src/core/BeamBase.ts:34](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L34)

The Beamable Customer ID.

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamBase.ts:36](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L36)

The Beamable Project ID.

***

### requester

> `readonly` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamBase.ts:32](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L32)

The HTTP requester instance used by the Beam SDK.

***

### tokenStorage

> **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/core/BeamBase.ts:42](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L42)

The token storage instance used by the client SDK.
Defaults to `BrowserTokenStorage` in browser environments and `NodeTokenStorage` in Node.js environments.
Can be overridden via the `tokenStorage` option in the `BeamConfig`.

## Accessors

### env

#### Get Signature

> **get** `static` **env**(): [`BeamEnvVars`](../interfaces/BeamEnvVars.md)

Defined in: [src/core/BeamBase.ts:67](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L67)

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

> `abstract` **use**<`T`\>(`ctors`): `this`

Defined in: [src/core/BeamBase.ts:86](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L86)

Dynamically adds multiple api services or microservice clients to the Beam SDK.

##### Type Parameters

###### T

`T` *extends* [`ApiServiceCtor`](../../../services/type-aliases/ApiServiceCtor.md)<`any`\> \| [`BeamMicroServiceClientCtor`](../../BeamMicroServiceClient/type-aliases/BeamMicroServiceClientCtor.md)<`any`\>

##### Parameters

###### ctors

readonly `T`[]

An array of constructors for the api service or microservice client.

##### Returns

`this`

The current instance of BeamBase.

##### Example

```ts
const beam = await Beam.init({ ... });
beam.use([LeadboardService, StatsService]);
```
or
```ts
const beam = await Beam.init({ ... });
beam.use([MyMicroserviceClient, MyOtherMicroserviceClient]);
```

#### Call Signature

> `abstract` **use**<`T`\>(`ctor`): `this`

Defined in: [src/core/BeamBase.ts:105](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamBase.ts#L105)

Dynamically adds a single api service or microservice client to the Beam SDK.

##### Type Parameters

###### T

`T` *extends* [`ApiServiceCtor`](../../../services/type-aliases/ApiServiceCtor.md)<`any`\> \| [`BeamMicroServiceClientCtor`](../../BeamMicroServiceClient/type-aliases/BeamMicroServiceClientCtor.md)<`any`\>

##### Parameters

###### ctor

`T`

The constructor for the api service or microservice client.

##### Returns

`this`

The current instance of BeamBase.

##### Example

```ts
const beam = await Beam.init({ ... });
beam.use(StatsService);
```
or
```ts
const beam = await Beam.init({ ... });
beam.use(MyMicroserviceClient);
```
