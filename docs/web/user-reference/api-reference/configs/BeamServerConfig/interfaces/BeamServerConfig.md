[beamable-sdk](../../../modules.md) / [configs/BeamServerConfig](../README.md) / BeamServerConfig

# Interface: BeamServerConfig

Defined in: [src/configs/BeamServerConfig.ts:5](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L5)

Configuration options for initializing the Beam Server SDK.

## Extends

- `BeamBaseConfig`

## Properties

### cid

> **cid**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:8](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L8)

Beamable Customer ID (CID).

#### Inherited from

`BeamBaseConfig.cid`

***

### contentNamespaces?

> `optional` **contentNamespaces**: `string`[]

Defined in: [src/configs/BeamBaseConfig.ts:33](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L33)

List of content namespaces to load. By default, only 'global' is loaded.

#### Inherited from

`BeamBaseConfig.contentNamespaces`

***

### engine?

> `optional` **engine**: `string`

Defined in: [src/configs/BeamServerConfig.ts:7](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L7)

Name of the engine (e.g., "Node", "Deno", "Express", "Hono").

***

### engineVersion?

> `optional` **engineVersion**: `string`

Defined in: [src/configs/BeamServerConfig.ts:10](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L10)

Version of the engine.

***

### environment?

> `optional` **environment**: [`BeamEnvironmentName`](../../BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

Defined in: [src/configs/BeamBaseConfig.ts:18](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L18)

The Beamable environment to connect to.
Can be one of 'prod', 'stg', 'dev', or a custom environment name.

#### Default

```ts
'prod'
```

#### Inherited from

`BeamBaseConfig.environment`

***

### gameVersion?

> `optional` **gameVersion**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:30](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L30)

Published version of the game.

#### Inherited from

`BeamBaseConfig.gameVersion`

***

### instanceTag?

> `optional` **instanceTag**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:27](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L27)

Unique tag for instance-specific token storage synchronization.

#### Inherited from

`BeamBaseConfig.instanceTag`

***

### pid

> **pid**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:11](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L11)

Beamable Project ID (PID).

#### Inherited from

`BeamBaseConfig.pid`

***

### requester?

> `optional` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/configs/BeamBaseConfig.ts:21](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L21)

Custom HTTP requester implementation.

#### Inherited from

`BeamBaseConfig.requester`

***

### serverEvents?

> `optional` **serverEvents**: [`ServerEventsConfig`](ServerEventsConfig.md)

Defined in: [src/configs/BeamServerConfig.ts:22](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L22)

Configuration for server-events.

***

### tokenStorage?

> `optional` **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/configs/BeamBaseConfig.ts:24](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamBaseConfig.ts#L24)

Custom token storage implementation.

#### Inherited from

`BeamBaseConfig.tokenStorage`

***

### useSignedRequest?

> `optional` **useSignedRequest**: `boolean`

Defined in: [src/configs/BeamServerConfig.ts:19](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L19)

Enables signing outgoing requests with a signature header.

#### Remarks

This option is only supported in Node.js environments.
When running in a browser, this setting will be ignored.

#### Default Value

```ts
false
```
