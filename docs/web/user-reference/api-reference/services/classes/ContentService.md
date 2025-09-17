[beamable-sdk](../../modules.md) / [services](../README.md) / ContentService

# Class: ContentService

Defined in: [src/services/ContentService.ts:56](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L56)

Represents a service that can be refreshed.

## Extends

- [`ApiService`](ApiService.md)

## Implements

- [`RefreshableService`](../interfaces/RefreshableService.md)<[`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)\>

## Constructors

### Constructor

> **new ContentService**(`props`): `ContentService`

Defined in: [src/services/ContentService.ts:73](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L73)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`ContentService`

#### Overrides

`ApiService.constructor`

## Accessors

### contentsCache

#### Get Signature

> **get** **contentsCache**(): `Record`<`string`, `Record`<`string`, [`ContentBase`](../../contents/types/interfaces/ContentBase.md)\>\>

Defined in: [src/services/ContentService.ts:84](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L84)

Retrieves the contents cache.

##### Returns

`Record`<`string`, `Record`<`string`, [`ContentBase`](../../contents/types/interfaces/ContentBase.md)\>\>

***

### manifestChecksumsCache

#### Get Signature

> **get** **manifestChecksumsCache**(): `Record`<`string`, [`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)\>

Defined in: [src/services/ContentService.ts:89](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L89)

Retrieves the manifest checksums cache.

##### Returns

`Record`<`string`, [`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)\>

***

### manifestEntriesCache

#### Get Signature

> **get** **manifestEntriesCache**(): `Record`<`string`, [`ClientContentInfoJson`](../../schema/type-aliases/ClientContentInfoJson.md)[]\>

Defined in: [src/services/ContentService.ts:94](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L94)

Retrieves the manifest entries cache.

##### Returns

`Record`<`string`, [`ClientContentInfoJson`](../../schema/type-aliases/ClientContentInfoJson.md)[]\>

## Methods

### getById()

> **getById**<`T`\>(`params`): `Promise`<[`ContentTypeFromId`](../../contents/types/type-aliases/ContentTypeFromId.md)<`T`\>\>

Defined in: [src/services/ContentService.ts:162](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L162)

Retrieves content by its ID.

#### Type Parameters

##### T

`T` *extends* `string`

#### Parameters

##### params

[`GetContentByIdParams`](../interfaces/GetContentByIdParams.md)<`T`\>

#### Returns

`Promise`<[`ContentTypeFromId`](../../contents/types/type-aliases/ContentTypeFromId.md)<`T`\>\>

The content object.

#### Remarks

This method first checks the in-memory cache, then persistent storage, and finally fetches from the API if not found or if the content is outdated.

#### Example

```ts
const item = await beam.content.getById({
  id: 'items.my_item',
  manifestId: 'global', // Optional, defaults to 'global'
});
console.log(item.properties);
```

#### Throws

If the content is not found or cannot be retrieved.

***

### getByIds()

> **getByIds**(`params`): `Promise`<[`ContentBase`](../../contents/types/interfaces/ContentBase.md)<`unknown`\>[]\>

Defined in: [src/services/ContentService.ts:185](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L185)

Retrieves group of contents by their IDs.

#### Parameters

##### params

[`GetContentByIdsParams`](../interfaces/GetContentByIdsParams.md)

#### Returns

`Promise`<[`ContentBase`](../../contents/types/interfaces/ContentBase.md)<`unknown`\>[]\>

An array of content objects.

#### Remarks

This method first checks the in-memory cache, then persistent storage, and finally fetches from the API if not found or if the content is outdated.

#### Example

```ts
const items = await beam.content.getByIds({
  ids: ['items.my_item_1', 'items.my_item_2'],
  manifestId: 'global', // Optional, defaults to 'global'
});
console.log(items[0].properties);
```

#### Throws

If any content is not found or cannot be retrieved.

***

### getByType()

> **getByType**<`T`\>(`params`): `Promise`<[`ContentTypeFromId`](../../contents/types/type-aliases/ContentTypeFromId.md)<`T`\>[]\>

Defined in: [src/services/ContentService.ts:211](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L211)

Retrieves group of contents by their type.

#### Type Parameters

##### T

`T` *extends* keyof [`ContentTypeMap`](../../contents/types/interfaces/ContentTypeMap.md)

#### Parameters

##### params

[`GetContentByTypeParams`](../interfaces/GetContentByTypeParams.md)<`T`\>

#### Returns

`Promise`<[`ContentTypeFromId`](../../contents/types/type-aliases/ContentTypeFromId.md)<`T`\>[]\>

An array of content objects of the specified type.

#### Remarks

This method first checks the in-memory cache, then persistent storage, and finally fetches from the API if not found or if the content is outdated.

#### Example

```ts
const items = await beam.content.getByType({
  type: 'items',
  manifestId: 'global', // Optional, defaults to 'global'
});
console.log(items[0].properties);
```

#### Throws

If the content is not found or cannot be retrieved.

***

### getManifestEntries()

> **getManifestEntries**(`params`): `Promise`<[`ClientContentInfoJson`](../../schema/type-aliases/ClientContentInfoJson.md)[]\>

Defined in: [src/services/ContentService.ts:135](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L135)

Retrieves all manifest entries for a given manifest ID.

#### Parameters

##### params

[`GetManifestEntriesParams`](../interfaces/GetManifestEntriesParams.md) = `{}`

#### Returns

`Promise`<[`ClientContentInfoJson`](../../schema/type-aliases/ClientContentInfoJson.md)[]\>

An array of manifest entries.

#### Remarks

This method first checks the in-memory cache, then persistent storage, and finally fetches from the API if not found.

#### Example

```ts
const entries = await beam.content.getManifestEntries({
  manifestId: 'global', // Optional, defaults to 'global'
});
console.log(entries[0].contentId);
```

***

### refresh()

> **refresh**(`data`): `Promise`<[`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)\>

Defined in: [src/services/ContentService.ts:111](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/ContentService.ts#L111)

Refreshes the content manifest for a given ID.

#### Parameters

##### data

[`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)

#### Returns

`Promise`<[`ContentManifestChecksum`](../interfaces/ContentManifestChecksum.md)\>

#### Remarks

This method fetches the latest content manifest and updates the local cache.

#### Example

```ts
await beam.content.refresh({
  id: 'global',
  checksum: 'some-checksum',
  uid: 'some-uid',
});
```

#### Throws

If the refresh fails.

#### Implementation of

[`RefreshableService`](../interfaces/RefreshableService.md).[`refresh`](../interfaces/RefreshableService.md#refresh)
