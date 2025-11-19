[beamable-sdk](../../../modules.md) / [configs/BeamConfig](../README.md) / BeamConfig

# Interface: BeamConfig

Defined in: [src/configs/BeamConfig.ts:5](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamConfig.ts#L5)

Configuration options for initializing the Beam Client SDK.

## Extends

- `BeamBaseConfig`

## Properties

### cid

> **cid**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:8](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L8)

Beamable Customer ID (CID).

#### Inherited from

`BeamBaseConfig.cid`

***

### contentNamespaces?

> `optional` **contentNamespaces**: `string`[]

Defined in: [src/configs/BeamBaseConfig.ts:33](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L33)

List of content namespaces to load. By default, only 'global' is loaded.

#### Inherited from

`BeamBaseConfig.contentNamespaces`

***

### environment?

> `optional` **environment**: [`BeamEnvironmentName`](../../BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

Defined in: [src/configs/BeamBaseConfig.ts:18](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L18)

The Beamable environment to connect to.
Can be one of 'prod', 'stg', 'dev', or a custom environment name.

#### Default

```ts
'prod'
```

#### Inherited from

`BeamBaseConfig.environment`

***

### gameEngine?

> `optional` **gameEngine**: `string`

Defined in: [src/configs/BeamConfig.ts:7](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamConfig.ts#L7)

Name of the game engine (e.g., "Three.js", "Phaser", "Babylon", "PlayCanvas").

***

### gameEngineVersion?

> `optional` **gameEngineVersion**: `string`

Defined in: [src/configs/BeamConfig.ts:10](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamConfig.ts#L10)

Version of the game engine.

***

### gameVersion?

> `optional` **gameVersion**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:30](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L30)

Published version of the game.

#### Inherited from

`BeamBaseConfig.gameVersion`

***

### instanceTag?

> `optional` **instanceTag**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:27](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L27)

Unique tag for instance-specific token storage synchronization.

#### Inherited from

`BeamBaseConfig.instanceTag`

***

### pid

> **pid**: `string`

Defined in: [src/configs/BeamBaseConfig.ts:11](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L11)

Beamable Project ID (PID).

#### Inherited from

`BeamBaseConfig.pid`

***

### requester?

> `optional` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/configs/BeamBaseConfig.ts:21](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L21)

Custom HTTP requester implementation.

#### Inherited from

`BeamBaseConfig.requester`

***

### services()?

> `optional` **services**: (`beam`) => `void`

Defined in: [src/configs/BeamConfig.ts:24](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamConfig.ts#L24)

Optional callback invoked during Beam Client SDK initialization to register or configure client services.

#### Parameters

##### beam

[`Beam`](../../../core/Beam/classes/Beam.md)

#### Returns

`void`

#### Example

```ts
import { clientServices } from "beamable-sdk";

const config: BeamConfig = {
  services: clientServices,
};
```

***

### tokenStorage?

> `optional` **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/configs/BeamBaseConfig.ts:24](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamBaseConfig.ts#L24)

Custom token storage implementation.

#### Inherited from

`BeamBaseConfig.tokenStorage`
