[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / parseSocketMessage

# Function: parseSocketMessage()

> **parseSocketMessage**<`K`\>(`rawMessage`): [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)\[`K`\]

Defined in: [src/core/BeamUtils.ts:28](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L28)

Parses a raw socket message string into a structured object based on the expected `RefreshableServiceMap` type.

## Type Parameters

### K

`K` *extends* keyof [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)

## Parameters

### rawMessage

`string`

## Returns

[`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)\[`K`\]
