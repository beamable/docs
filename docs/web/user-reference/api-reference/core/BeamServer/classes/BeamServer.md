[beamable-sdk](../../../modules.md) / [core/BeamServer](../README.md) / BeamServer

# Class: BeamServer

Defined in: [src/core/BeamServer.ts:30](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L30)

The main class for interacting with the Beam Server SDK.

## Extends

- [`BeamBase`](../../BeamBase/classes/BeamBase.md)<`this`\>.`BeamServerServiceType`

## Properties

### account()

> **account**: (`userId`) => [`AccountService`](../../../services/classes/AccountService.md)

#### Parameters

##### userId

`string`

#### Returns

[`AccountService`](../../../services/classes/AccountService.md)

***

### announcements()

> **announcements**: (`userId`) => [`AnnouncementsService`](../../../services/classes/AnnouncementsService.md)

#### Parameters

##### userId

`string`

#### Returns

[`AnnouncementsService`](../../../services/classes/AnnouncementsService.md)

***

### auth()

> **auth**: (`userId`) => [`AuthService`](../../../services/classes/AuthService.md)

#### Parameters

##### userId

`string`

#### Returns

[`AuthService`](../../../services/classes/AuthService.md)

***

### cid

> **cid**: `string`

Defined in: [src/core/BeamBase.ts:34](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L34)

The Beamable Customer ID.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`cid`](../../BeamBase/classes/BeamBase.md#cid)

***

### content()

> **content**: (`userId`) => [`ContentService`](../../../services/classes/ContentService.md)

#### Parameters

##### userId

`string`

#### Returns

[`ContentService`](../../../services/classes/ContentService.md)

***

### leaderboards()

> **leaderboards**: (`userId`) => [`LeaderboardsService`](../../../services/classes/LeaderboardsService.md)

#### Parameters

##### userId

`string`

#### Returns

[`LeaderboardsService`](../../../services/classes/LeaderboardsService.md)

***

### pid

> **pid**: `string`

Defined in: [src/core/BeamBase.ts:36](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L36)

The Beamable Project ID.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`pid`](../../BeamBase/classes/BeamBase.md#pid)

***

### requester

> `readonly` **requester**: [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamBase.ts:32](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamBase.ts#L32)

The HTTP requester instance used by the Beam SDK.

#### Inherited from

[`BeamBase`](../../BeamBase/classes/BeamBase.md).[`requester`](../../BeamBase/classes/BeamBase.md#requester)

***

### stats()

> **stats**: (`userId`) => [`StatsService`](../../../services/classes/StatsService.md)

#### Parameters

##### userId

`string`

#### Returns

[`StatsService`](../../../services/classes/StatsService.md)

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

Defined in: [src/core/BeamServer.ts:60](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L60)

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

> **off**<`K`\>(`eventType`, `handler?`): `void`

Defined in: [src/core/BeamServer.ts:144](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L144)

Unsubscribes from a specific server-event or removes all subscriptions if no handler is provided.

#### Type Parameters

##### K

`K` *extends* [`ServerEventType`](../../types/ServerEventType/type-aliases/ServerEventType.md)

#### Parameters

##### eventType

`K`

The server-event to unsubscribe from, e.g., 'content.manifest'.

##### handler?

(`data`) => `void`

The callback to remove. If not provided, all handlers for the server-event are removed.

#### Returns

`void`

#### Example

```ts
beamServer.off('content.manifest', handler);
// or to remove all handlers for the server-event
beamServer.off('content.manifest');
```

***

### on()

> **on**<`K`\>(`eventType`, `handler`): `void`

Defined in: [src/core/BeamServer.ts:113](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L113)

Subscribes to a server-event and listens for messages.

#### Type Parameters

##### K

`K` *extends* [`ServerEventType`](../../types/ServerEventType/type-aliases/ServerEventType.md)

#### Parameters

##### eventType

`K`

The server-event to subscribe to, e.g., 'content.manifest'.

##### handler

(`data`) => `void`

The callback to process the data when a message is received.

#### Returns

`void`

#### Example

```ts
const handler = (data) => {
  console.log('Content manifest received:', data);
};
beamServer.on('content.manifest', handler);
```

***

### use()

#### Call Signature

> **use**<`T`\>(`Service`): `this`

Defined in: [src/core/BeamServer.ts:64](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L64)

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

Defined in: [src/core/BeamServer.ts:65](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L65)

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

> `static` **init**(`config`): `Promise`<`BeamServer`\>

Defined in: [src/core/BeamServer.ts:36](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamServer.ts#L36)

Initialize a new Beam server instance.

#### Parameters

##### config

[`BeamServerConfig`](../../../configs/BeamServerConfig/interfaces/BeamServerConfig.md)

#### Returns

`Promise`<`BeamServer`\>
