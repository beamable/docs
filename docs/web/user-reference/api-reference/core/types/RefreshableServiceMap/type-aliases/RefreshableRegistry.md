[beamable-sdk](../../../../modules.md) / [core/types/RefreshableServiceMap](../README.md) / RefreshableRegistry

# Type Alias: RefreshableRegistry

> **RefreshableRegistry** = `{ [K in keyof RefreshableServiceMap]: RefreshableService<RefreshableServiceMap[K]["data"]> }`

Defined in: [src/core/types/RefreshableServiceMap.ts:20](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/types/RefreshableServiceMap.ts#L20)

The `RefreshableRegistry` maps a service key to its `RefreshableService` instance.
