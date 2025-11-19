[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / StandaloneRequesterProps

# Interface: StandaloneRequesterProps

Defined in: [src/core/BeamUtils.ts:53](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L53)

## Properties

### cid

> **cid**: `string`

Defined in: [src/core/BeamUtils.ts:55](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L55)

The Beamable Customer ID.

***

### environment?

> `optional` **environment**: [`BeamEnvironmentName`](../../../configs/BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

Defined in: [src/core/BeamUtils.ts:63](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L63)

The Beamable environment to connect to.
Can be one of 'prod', 'stg', 'dev', or a custom environment name.

#### Default

```ts
'prod'
```

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamUtils.ts:57](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L57)

The Beamable Project ID.

***

### requester?

> `optional` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamUtils.ts:65](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L65)

The custom `HttpRequester` to use for the API requests. If not provided, a default one will be used.

***

### tokenStorage?

> `optional` **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/core/BeamUtils.ts:67](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L67)

The custom `TokenStorage` to use for the API requests. If not provided, a default one will be used.

***

### tokenStorageTag?

> `optional` **tokenStorageTag**: `string`

Defined in: [src/core/BeamUtils.ts:69](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L69)

Unique tag for instance-specific token storage synchronization.

***

### useSignedRequest?

> `optional` **useSignedRequest**: `boolean`

Defined in: [src/core/BeamUtils.ts:77](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L77)

Enables signing outgoing requests with a signature header.

#### Remarks

This option is only supported in Node.js environments.
When running in a browser, this setting will be ignored.

#### Default Value

```ts
false
```
