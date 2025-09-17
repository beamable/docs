[beamable-sdk](../../../modules.md) / [configs/BeamServerConfig](../README.md) / ServerEventsConfig

# Interface: ServerEventsConfig

Defined in: [src/configs/BeamServerConfig.ts:26](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L26)

Configuration options for server-events.

## Properties

### enabled?

> `optional` **enabled**: `boolean`

Defined in: [src/configs/BeamServerConfig.ts:31](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L31)

Enables the server-events feature (gateway notifications over WebSocket).

#### Default

```ts
false
```

***

### eventWhitelist?

> `optional` **eventWhitelist**: [`ServerEventType`](../../../core/types/ServerEventType/type-aliases/ServerEventType.md)[]

Defined in: [src/configs/BeamServerConfig.ts:33](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/configs/BeamServerConfig.ts#L33)

A list of server events to subscribe to. If not provided, all events will be subscribed to.
