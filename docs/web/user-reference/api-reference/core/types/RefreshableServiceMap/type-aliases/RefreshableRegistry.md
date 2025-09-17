[beamable-sdk](../../../../modules.md) / [core/types/RefreshableServiceMap](../README.md) / RefreshableRegistry

# Type Alias: RefreshableRegistry

> **RefreshableRegistry** = `{ [K in keyof RefreshableServiceMap]: RefreshableService<RefreshableServiceMap[K]["data"]> }`

Defined in: [src/core/types/RefreshableServiceMap.ts:20](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/types/RefreshableServiceMap.ts#L20)

The `RefreshableRegistry` maps a service key to its `RefreshableService` instance.
