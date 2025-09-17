[beamable-sdk](../../../modules.md) / [core/BeamEnvironmentRegistry](../README.md) / BeamEnvironmentRegistry

# Class: BeamEnvironmentRegistry

Defined in: [src/core/BeamEnvironmentRegistry.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamEnvironmentRegistry.ts#L34)

A registry for Beamable environment configurations.
Allows for registering and retrieving environment configurations by name.

## Constructors

### Constructor

> **new BeamEnvironmentRegistry**(`initial`): `BeamEnvironmentRegistry`

Defined in: [src/core/BeamEnvironmentRegistry.ts:37](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamEnvironmentRegistry.ts#L37)

#### Parameters

##### initial

`Record`<[`BuiltInEnv`](../../../configs/BeamEnvironmentConfig/type-aliases/BuiltInEnv.md), [`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)\> = `defaultEnvironments`

#### Returns

`BeamEnvironmentRegistry`

## Methods

### get()

> **get**(`name`): [`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)

Defined in: [src/core/BeamEnvironmentRegistry.ts:52](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamEnvironmentRegistry.ts#L52)

Get a registered environment configuration.

#### Parameters

##### name

[`BeamEnvironmentName`](../../../configs/BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

#### Returns

[`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)

***

### list()

> **list**(): `Readonly`<`Record`<`string`, [`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)\>\>

Defined in: [src/core/BeamEnvironmentRegistry.ts:47](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamEnvironmentRegistry.ts#L47)

Read-only snapshot of all registered environments (useful for debugging/UIs).

#### Returns

`Readonly`<`Record`<`string`, [`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)\>\>

***

### register()

> **register**(`name`, `cfg`): `void`

Defined in: [src/core/BeamEnvironmentRegistry.ts:42](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamEnvironmentRegistry.ts#L42)

Add or overwrite an environment configuration at runtime.

#### Parameters

##### name

[`BeamEnvironmentName`](../../../configs/BeamEnvironmentConfig/type-aliases/BeamEnvironmentName.md)

##### cfg

[`BeamEnvironmentConfig`](../../../configs/BeamEnvironmentConfig/interfaces/BeamEnvironmentConfig.md)

#### Returns

`void`
