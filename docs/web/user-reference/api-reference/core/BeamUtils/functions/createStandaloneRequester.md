[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / createStandaloneRequester

# Function: createStandaloneRequester()

> **createStandaloneRequester**(`props`): [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamUtils.ts:86](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/core/BeamUtils.ts#L86)

Creates a `HttpRequester` instance for standalone API requests.
This is useful when you need to make API calls without initializing the SDK.

## Parameters

### props

[`StandaloneRequesterProps`](../interfaces/StandaloneRequesterProps.md)

Configuration properties for the standalone requester.

## Returns

[`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

A `HttpRequester` instance.
