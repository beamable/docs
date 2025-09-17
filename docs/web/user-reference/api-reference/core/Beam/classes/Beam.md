[beamable-sdk](../../../modules.md) / [core/Beam](../README.md) / Beam

# Class: Beam

Defined in: [src/core/Beam.ts:32](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L32)

The main class for interacting with the Beam Client SDK.

## Extends

- [`BeamBase`](../../BeamBase/classes/BeamBase.md)<`this`\>.`BeamServiceType`

## Properties

### account

> **account**: [`AccountService`](../../../services/classes/AccountService.md)

***

### announcements

> **announcements**: [`AnnouncementsService`](../../../services/classes/AnnouncementsService.md)

***

### auth

> **auth**: [`AuthService`](../../../services/classes/AuthService.md)

***

### cid

> **cid**: `string`

Defined in: [src/core/BeamBase.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L34)

The Beamable Customer ID.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`cid`](../../BeamBase/classes/BeamBase.md#cid)

***

### content

> **content**: [`ContentService`](../../../services/classes/ContentService.md)

***

### leaderboards

> **leaderboards**: [`LeaderboardsService`](../../../services/classes/LeaderboardsService.md)

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamBase.ts:36](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L36)

The Beamable Project ID.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`pid`](../../BeamBase/classes/BeamBase.md#pid)

***

### player

> **player**: [`PlayerService`](../../../services/classes/PlayerService.md)

Defined in: [src/core/Beam.ts:37](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L37)

A namespace of player-related services.
Use `beam.player.<method>` to access player-specific operations.

***

### requester

> `readonly` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamBase.ts:32](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L32)

The HTTP requester instance used by the Beam SDK.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`requester`](../../BeamBase/classes/BeamBase.md#requester)

***

### stats

> **stats**: [`StatsService`](../../../services/classes/StatsService.md)

***

### tokenStorage

> **tokenStorage**: [`TokenStorage`](../../../platform/types/TokenStorage/classes/TokenStorage.md)

Defined in: [src/core/BeamBase.ts:42](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L42)

The token storage instance used by the client SDK.
Defaults to `BrowserTokenStorage` in browser environments and `NodeTokenStorage` in Node.js environments.
Can be overridden via the `tokenStorage` option in the `BeamConfig`.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`tokenStorage`](../../BeamBase/classes/BeamBase.md#tokenstorage)

## Accessors

### env

#### Get Signature

> **get** `static` **env**(): [`BeamEnvVars`](../../BeamBase/interfaces/BeamEnvVars.md)

Defined in: [src/core/Beam.ts:74](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L74)

Environment variables that can be set to configure the Beam SDK.

##### Remarks

These values **must** be supplied at runtime via real environment variables
(e.g. `process.env.REALM_SECRET`), and **must not** be committed directly into your source code.

##### Example

```ts
BeamBase.env.REALM_SECRET = process.env.REALM_SECRET;
const beam = await Beam.init({ ... });
```

##### Returns

[`BeamEnvVars`](../../BeamBase/interfaces/BeamEnvVars.md)

#### Overrides

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`env`](../../BeamBase/classes/BeamBase.md#env)

## Methods

### off()

> **off**<`K`\>(`context`, `handler?`): `void`

Defined in: [src/core/Beam.ts:245](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L245)

Unsubscribes from a specific context or removes all subscriptions if no handler is provided.

#### Type Parameters

##### K

`K` *extends* keyof [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)

#### Parameters

##### context

`K`

The context to unsubscribe from, e.g., 'inventory.refresh'.

##### handler?

(`data`) => `void`

The callback to remove. If not provided, all handlers for the context are removed.

#### Returns

`void`

#### Example

```ts
beam.off('inventory.refresh', handler);
// or to remove all handlers for the context
beam.off('inventory.refresh');
```

***

### on()

> **on**<`K`\>(`context`, `handler`): `void`

Defined in: [src/core/Beam.ts:196](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L196)

Subscribes to a specific context and listens for messages.

#### Type Parameters

##### K

`K` *extends* keyof [`RefreshableServiceMap`](../../types/RefreshableServiceMap/interfaces/RefreshableServiceMap.md)

#### Parameters

##### context

`K`

The context to subscribe to, e.g., 'inventory.refresh'.

##### handler

(`data`) => `void`

The callback to process the data when a message is received.

#### Returns

`void`

#### Example

```ts
const handler = (data) => {
  console.log('New inventory data:', data);
}
beam.use(InventoryService);
beam.on('inventory.refresh', handler);
```

***

### refresh()

> **refresh**(`tokenResponse?`): `Promise`<`void`\>

Defined in: [src/core/Beam.ts:169](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L169)

Refreshes the current Beam SDK instance with a new token response.
This method re-initializes the SDK with the provided token,
updates the internal state, and re-establishes necessary connections.

#### Parameters

##### tokenResponse?

[`TokenResponse`](../../../schema/type-aliases/TokenResponse.md)

The new token response to use for refreshing the SDK.

#### Returns

`Promise`<`void`\>

#### Example

```ts
const newToken = await beam.auth.loginWithEmail({ email, password });
await beam.refresh(newToken);
```

***

### use()

#### Call Signature

> **use**<`T`\>(`Service`): `this`

Defined in: [src/core/Beam.ts:78](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L78)

Dynamically adds a service to the Beam SDK instance.

##### Type Parameters

###### T

`T` *extends* [`ApiService`](../../../services/classes/ApiService.md)

##### Parameters

###### Service

[`ApiServiceCtor`](../../../services/type-aliases/ApiServiceCtor.md)<`T`\>

The service class to add.

##### Returns

`this`

##### Example

```ts
// client-side:
beam.use(StatsService);
await beam.stats.get({...});
// server-side:
beamServer.use(StatsService);
await beamServer.stats.get({...});
```

##### Overrides

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`use`](../../BeamBase/classes/BeamBase.md#use)

#### Call Signature

> **use**<`T`\>(`Client`): `this`

Defined in: [src/core/Beam.ts:79](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L79)

Dynamically adds a microservice client to the Beam SDK instance.

##### Type Parameters

###### T

`T` *extends* [`BeamMicroServiceClient`](../../BeamMicroServiceClient/classes/BeamMicroServiceClient.md)

##### Parameters

###### Client

[`BeamMicroServiceClientCtor`](../../BeamMicroServiceClient/type-aliases/BeamMicroServiceClientCtor.md)<`T`\>

The microservice client class to add.

##### Returns

`this`

##### Example

```ts
// client-side:
beam.use(MyMicroServiceClient);
beam.myMicroServiceClient.serviceName;
// server-side:
beamServer.use(MyMicroServiceClient);
beamServer.myMicroServiceClient.serviceName;
```

##### Overrides

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`use`](../../BeamBase/classes/BeamBase.md#use)

***

### init()

> `static` **init**(`config`): `Promise`<`Beam`\>

Defined in: [src/core/Beam.ts:44](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/Beam.ts#L44)

Initialize a new Beam client instance.

#### Parameters

##### config

[`BeamConfig`](../../../configs/BeamConfig/interfaces/BeamConfig.md)

#### Returns

`Promise`<`Beam`\>
