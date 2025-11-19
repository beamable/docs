[beamable-sdk](../../modules.md) / [defaults](../README.md) / readConfig

# Function: readConfig()

> **readConfig**(): `Promise`<\{ `cid`: `string`; `pid`: `string`; \}\>

Defined in: [src/platform/NodeConfigStorage.ts:10](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/platform/NodeConfigStorage.ts#L10)

Reads the Beamable configuration from storage.
In Node.js environments, it reads from a JSON file in the user's home directory.

## Returns

`Promise`<\{ `cid`: `string`; `pid`: `string`; \}\>
