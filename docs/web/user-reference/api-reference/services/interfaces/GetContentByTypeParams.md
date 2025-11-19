[beamable-sdk](../../modules.md) / [services](../README.md) / GetContentByTypeParams

# Interface: GetContentByTypeParams<T\>

Defined in: [src/services/ContentService.ts:45](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/ContentService.ts#L45)

## Type Parameters

### T

`T` *extends* keyof [`ContentTypeMap`](../../contents/types/interfaces/ContentTypeMap.md)

## Properties

### manifestId?

> `optional` **manifestId**: `string`

Defined in: [src/services/ContentService.ts:47](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/ContentService.ts#L47)

Optional manifest ID to fetch specific content, defaults to 'global'

***

### type

> **type**: `T`

Defined in: [src/services/ContentService.ts:48](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/ContentService.ts#L48)
