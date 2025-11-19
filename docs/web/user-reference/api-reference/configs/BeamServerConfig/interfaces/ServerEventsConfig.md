[beamable-sdk](../../../modules.md) / [configs/BeamServerConfig](../README.md) / ServerEventsConfig

# Interface: ServerEventsConfig

Defined in: [src/configs/BeamServerConfig.ts:41](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamServerConfig.ts#L41)

Configuration options for server-events.

## Properties

### enabled?

> `optional` **enabled**: `boolean`

Defined in: [src/configs/BeamServerConfig.ts:46](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamServerConfig.ts#L46)

Enables the server-events feature (gateway notifications over WebSocket).

#### Default

```ts
false
```

***

### eventWhitelist?

> `optional` **eventWhitelist**: [`ServerEventType`](../../../core/types/ServerEventType/type-aliases/ServerEventType.md)[]

Defined in: [src/configs/BeamServerConfig.ts:48](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/configs/BeamServerConfig.ts#L48)

A list of server events to subscribe to. If not provided, all events will be subscribed to.
