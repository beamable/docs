[beamable-sdk](../../../../modules.md) / [platform/types/TokenStorage](../README.md) / TokenStorage

# Abstract Class: TokenStorage

Defined in: [src/platform/types/TokenStorage.ts:10](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L10)

Abstraction for managing a persisted authentication token.

## Constructors

### Constructor

> **new TokenStorage**(): `TokenStorage`

#### Returns

`TokenStorage`

## Accessors

### isExpired

#### Get Signature

> **get** **isExpired**(): `boolean`

Defined in: [src/platform/types/TokenStorage.ts:32](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L32)

True if the token has already expired OR will expire within the next 24 hours.

##### Returns

`boolean`

## Methods

### clear()

> `abstract` **clear**(): `void`

Defined in: [src/platform/types/TokenStorage.ts:26](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L26)

Clears all stored tokens and expiry information.

#### Returns

`void`

***

### dispose()

> `abstract` **dispose**(): `void`

Defined in: [src/platform/types/TokenStorage.ts:29](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L29)

Clean up BroadcastChannel and storage listener in the case of browser environment (e.g., on logout).

#### Returns

`void`

***

### getTokenData()

> `abstract` **getTokenData**(): `Promise`<[`TokenData`](../interfaces/TokenData.md)\>

Defined in: [src/platform/types/TokenStorage.ts:16](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L16)

Retrieves the stored token data.

#### Returns

`Promise`<[`TokenData`](../interfaces/TokenData.md)\>

***

### setTokenData()

> `abstract` **setTokenData**(`data`): `Promise`<`TokenStorage`\>

Defined in: [src/platform/types/TokenStorage.ts:23](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/types/TokenStorage.ts#L23)

Updates the stored token data. Fields not provided are left unchanged.
Set a field to `null` to clear it.

#### Parameters

##### data

`Partial`<[`TokenData`](../interfaces/TokenData.md)\>

#### Returns

`Promise`<`TokenStorage`\>

#### Remarks

When setting the `expiresIn`, use the raw `expires_in` from the token response plus Date.now() to compute the absolute expiry time.
