[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / StandaloneRequesterProps

# Interface: StandaloneRequesterProps

Defined in: [src/core/BeamUtils.ts:43](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L43)

## Properties

### cid

> **cid**: `string`

Defined in: [src/core/BeamUtils.ts:45](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L45)

The Beamable Customer ID.

***

### environment?

> `optional` **environment**: [`BeamEnvironmentName`](../../../configs/BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

Defined in: [src/core/BeamUtils.ts:53](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L53)

The Beamable environment to connect to.
Can be one of 'prod', 'stg', 'dev', or a custom environment name.

#### Default

```ts
'prod'
```

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamUtils.ts:47](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L47)

The Beamable Project ID.

***

### requester?

> `optional` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamUtils.ts:55](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L55)

The custom `HttpRequester` to use for the API requests. If not provided, a default one will be used.

***

### tokenStorage?

> `optional` **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/core/BeamUtils.ts:57](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L57)

The custom `TokenStorage` to use for the API requests. If not provided, a default one will be used.

***

### tokenStorageTag?

> `optional` **tokenStorageTag**: `string`

Defined in: [src/core/BeamUtils.ts:59](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L59)

Unique tag for instance-specific token storage synchronization.

***

### useSignedRequest?

> `optional` **useSignedRequest**: `boolean`

Defined in: [src/core/BeamUtils.ts:67](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L67)

Enables signing outgoing requests with a signature header.

#### Remarks

This option is only supported in Node.js environments.
When running in a browser, this setting will be ignored.

#### Default Value

```ts
false
```
