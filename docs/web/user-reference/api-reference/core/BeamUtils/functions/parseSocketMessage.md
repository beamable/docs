[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / parseSocketMessage

# Function: parseSocketMessage()

> **parseSocketMessage**<`K`\>(`rawMessage`): [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)\[`K`\]

Defined in: [src/core/BeamUtils.ts:38](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L38)

Parses a raw socket message string into a structured object based on the expected `RefreshableServiceMap` type.

## Type Parameters

### K

`K` *extends* keyof [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)

## Parameters

### rawMessage

`string`

## Returns

[`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)\[`K`\]
