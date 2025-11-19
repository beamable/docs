[beamable-sdk](../../modules.md) / [schema](../README.md) / JobDefinitionSaveRequest

# Type Alias: JobDefinitionSaveRequest

> **JobDefinitionSaveRequest** = `object`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:13](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L13)

## Properties

### id?

> `optional` **id**: `string` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:14](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L14)

***

### isUnique?

> `optional` **isUnique**: `boolean` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:15](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L15)

***

### jobAction?

> `optional` **jobAction**: [`HttpCall`](HttpCall.md) \| [`PublishMessage`](PublishMessage.md) \| [`ServiceCall`](ServiceCall.md)

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:16](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L16)

***

### name?

> `optional` **name**: `string`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:17](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L17)

***

### retryPolicy?

> `optional` **retryPolicy**: [`JobRetryPolicy`](JobRetryPolicy.md)

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:18](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L18)

***

### source?

> `optional` **source**: `string` \| `null`

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:19](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L19)

***

### triggers?

> `optional` **triggers**: ([`CronTrigger`](CronTrigger.md) \| [`ExactTrigger`](ExactTrigger.md))[]

Defined in: [src/\_\_generated\_\_/schemas/JobDefinitionSaveRequest.ts:20](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/__generated__/schemas/JobDefinitionSaveRequest.ts#L20)
