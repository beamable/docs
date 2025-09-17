[beamable-sdk](../../modules.md) / [services](../README.md) / ExternalChallengeResponse

# Interface: ExternalChallengeResponse

Defined in: [src/services/AuthService.ts:31](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AuthService.ts#L31)

## Properties

### challenge\_token

> **challenge\_token**: `string`

Defined in: [src/services/AuthService.ts:35](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AuthService.ts#L35)

The challenge token associated with the external authentication.

***

### challenge\_ttl

> **challenge\_ttl**: `number`

Defined in: [src/services/AuthService.ts:40](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AuthService.ts#L40)

The time-to-live (TTL) of the challenge.
When provided, it indicates that the external authentication is pending verification.

***

### user\_id?

> `optional` **user\_id**: `string`

Defined in: [src/services/AuthService.ts:33](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AuthService.ts#L33)

The user ID in the external system (wallet ID, OAuth ID, etc.)
