[beamable-sdk](../../../modules.md) / [core/BeamUtils](../README.md) / createStandaloneRequester

# Function: createStandaloneRequester()

> **createStandaloneRequester**(`props`): [`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

Defined in: [src/core/BeamUtils.ts:76](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/core/BeamUtils.ts#L76)

Creates a `HttpRequester` instance for standalone API requests.
This is useful when you need to make API calls without initializing the SDK.

## Parameters

### props

[`StandaloneRequesterProps`](../interfaces/StandaloneRequesterProps.md)

Configuration properties for the standalone requester.

## Returns

[`HttpRequester`](../../../network/http/types/HttpRequester/interfaces/HttpRequester.md)

A `HttpRequester` instance.
