[beamable-sdk](../../../modules.md) / [contents/types](../README.md) / ContentTypeFromId

# Type Alias: ContentTypeFromId<Id\>

> **ContentTypeFromId**<`Id`\> = `Id` *extends* keyof [`ContentTypeMap`](../interfaces/ContentTypeMap.md) ? [`ContentTypeMap`](../interfaces/ContentTypeMap.md)\[`Id`\] : `ExtractPrefixes`<`Id`\> *extends* infer Prefixes ? `Prefixes` *extends* keyof [`ContentTypeMap`](../interfaces/ContentTypeMap.md) ? [`ContentTypeMap`](../interfaces/ContentTypeMap.md)\[`Prefixes`\] : [`ContentBase`](../interfaces/ContentBase.md) : [`ContentBase`](../interfaces/ContentBase.md)

Defined in: [src/contents/types/ContentTypeFromId.ts:40](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/contents/types/ContentTypeFromId.ts#L40)

Derives the most specific TypeScript type for a given content ID.

This utility searches for a type by first attempting an exact match on the ID.
If no direct match is found, it falls back to checking the parent ID
(the string with its last segment removed). If no match is found, it defaults
to the base `ContentBase` type.

## Type Parameters

### Id

`Id` *extends* `string`

The dot-delimited content identifier.

## Example

```ts
// Assuming ContentTypeMap contains:
// "items": ItemContent
// "items.shield": ShieldContent
// "items.shield.wooden": WoodenShieldContent

type T1 = ContentTypeFromId<"items.shield.wooden.rare">; // -> WoodenShieldContent
type T2 = ContentTypeFromId<"items.shield.metal">; // -> ShieldContent
type T3 = ContentTypeFromId<"items.weapon">; // -> ItemContent
type T4 = ContentTypeFromId<"unknown.type">; // -> ContentBase
```
