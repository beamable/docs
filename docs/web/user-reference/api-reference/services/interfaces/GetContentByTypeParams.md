[beamable-sdk](../../modules.md) / [services](../README.md) / GetContentByTypeParams

# Interface: GetContentByTypeParams<T\>

Defined in: [src/services/ContentService.ts:45](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L45)

## Type Parameters

### T

`T` *extends* keyof [`ContentTypeMap`](../../contents/types/interfaces/ContentTypeMap.md)

## Properties

### manifestId?

> `optional` **manifestId**: `string`

Defined in: [src/services/ContentService.ts:47](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L47)

Optional manifest ID to fetch specific content, defaults to 'global'

***

### type

> **type**: `T`

Defined in: [src/services/ContentService.ts:48](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L48)
