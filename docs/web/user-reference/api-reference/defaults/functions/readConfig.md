[beamable-sdk](../../modules.md) / [defaults](../README.md) / readConfig

# Function: readConfig()

> **readConfig**(): `Promise`<\{ `cid`: `string`; `pid`: `string`; \}\>

Defined in: [src/platform/NodeConfigStorage.ts:10](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/platform/NodeConfigStorage.ts#L10)

Reads the Beamable configuration from storage.
In Node.js environments, it reads from a JSON file in the user's home directory.

## Returns

`Promise`<\{ `cid`: `string`; `pid`: `string`; \}\>
