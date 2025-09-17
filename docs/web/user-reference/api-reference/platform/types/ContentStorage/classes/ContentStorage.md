[beamable-sdk](../../../../modules.md) / [platform/types/ContentStorage](../README.md) / ContentStorage

# Abstract Class: ContentStorage

Defined in: [src/platform/types/ContentStorage.ts:6](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L6)

Abstraction for managing and storing Beamable contents.

## Constructors

### Constructor

> **new ContentStorage**(): `ContentStorage`

#### Returns

`ContentStorage`

## Methods

### clear()

> `abstract` **clear**(): `Promise`<`void`\>

Defined in: [src/platform/types/ContentStorage.ts:31](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L31)

Clears the entire content storage.

#### Returns

`Promise`<`void`\>

***

### close()

> **close**(): `void`

Defined in: [src/platform/types/ContentStorage.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L34)

Closes the content storage.

#### Returns

`void`

***

### del()

> `abstract` **del**(`key`): `Promise`<`void`\>

Defined in: [src/platform/types/ContentStorage.ts:28](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L28)

Deletes a value from the content storage.

#### Parameters

##### key

`string`

#### Returns

`Promise`<`void`\>

***

### get()

> `abstract` **get**<`T`\>(`key`): `Promise`<`undefined` \| `T`\>

Defined in: [src/platform/types/ContentStorage.ts:22](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L22)

Gets a value from the content storage.

#### Type Parameters

##### T

`T` = `unknown`

#### Parameters

##### key

`string`

#### Returns

`Promise`<`undefined` \| `T`\>

***

### has()

> `abstract` **has**(`key`): `Promise`<`boolean`\>

Defined in: [src/platform/types/ContentStorage.ts:25](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L25)

Checks if a value exists in the content storage.

#### Parameters

##### key

`string`

#### Returns

`Promise`<`boolean`\>

***

### set()

> `abstract` **set**<`T`\>(`key`, `value`): `Promise`<`void`\>

Defined in: [src/platform/types/ContentStorage.ts:19](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L19)

Sets a value in the content storage.

#### Type Parameters

##### T

`T`

#### Parameters

##### key

`string`

##### value

`T`

#### Returns

`Promise`<`void`\>

***

### open()

> `static` **open**(): `Promise`<`ContentStorage`\>

Defined in: [src/platform/types/ContentStorage.ts:12](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/ContentStorage.ts#L12)

Opens a content storage.

#### Returns

`Promise`<`ContentStorage`\>
