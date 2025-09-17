[beamable-sdk](../../modules.md) / [schema](../README.md) / JobDefinition

# Type Alias: JobDefinition

> **JobDefinition** = `object`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:14](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L14)

## Properties

### analytics?

> `optional` **analytics**: [`JobAnalytics`](JobAnalytics.md)

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:15](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L15)

***

### id?

> `optional` **id**: `string`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:16](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L16)

***

### isUnique?

> `optional` **isUnique**: `boolean`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:17](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L17)

***

### jobAction?

> `optional` **jobAction**: [`HttpCall`](HttpCall.md) \| [`PublishMessage`](PublishMessage.md) \| [`ServiceCall`](ServiceCall.md)

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:18](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L18)

***

### lastUpdate?

> `optional` **lastUpdate**: `Date`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:19](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L19)

***

### name?

> `optional` **name**: `string`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:20](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L20)

***

### nonce?

> `optional` **nonce**: `string` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:21](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L21)

***

### owner?

> `optional` **owner**: `string`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:22](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L22)

***

### retryPolicy?

> `optional` **retryPolicy**: [`JobRetryPolicy`](JobRetryPolicy.md)

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:23](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L23)

***

### source?

> `optional` **source**: `string` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:24](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L24)

***

### suspendedAt?

> `optional` **suspendedAt**: `Date` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:25](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L25)

***

### triggers?

> `optional` **triggers**: ([`CronTrigger`](CronTrigger.md) \| [`ExactTrigger`](ExactTrigger.md))[]

Defined in: [src/\_\_generated\_\_/schemas/JobDefinition.ts:26](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/__generated__/schemas/JobDefinition.ts#L26)
