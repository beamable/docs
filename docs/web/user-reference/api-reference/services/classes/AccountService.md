[beamable-sdk](../../modules.md) / [services](../README.md) / AccountService

# Class: AccountService

Defined in: [src/services/AccountService.ts:54](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L54)

## Extends

- [`ApiService`](ApiService.md)

## Constructors

### Constructor

> **new AccountService**(`props`): `AccountService`

Defined in: [src/services/AccountService.ts:55](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L55)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`AccountService`

#### Overrides

`ApiService.constructor`

## Methods

### addCredentials()

> **addCredentials**(`params`): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:100](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L100)

Registers a new account with the given email and password, and associates it with the current player.

#### Parameters

##### params

[`UserCredentialParams`](../interfaces/UserCredentialParams.md)

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// register a new account
const playerAccount = await account.addCredentials({
  email: 'player@example.com',
  password: 'password123',
});
```

#### Throws

If the registration fails (e.g., email already exists, invalid password).

***

### addExternalIdentity()

> **addExternalIdentity**(`params`): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:175](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L175)

Links an external identity to the current player's Beamable account.

#### Parameters

##### params

[`ExternalIdentityCredentialParams`](../interfaces/ExternalIdentityCredentialParams.md)

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// link an external identity
const playerAccount = await account.addExternalIdentity({
  externalToken: 'acme-auth-token',
  providerService: acmeServiceClient.serviceName,
  providerNamespace: acmeServiceClient.federationIds.acme,
  // optional
  challengeHandler: (challenge) => {
    // Handle the challenge, e.g., by displaying a CAPTCHA or OTP to the user
    return prompt(challenge);
  },
});
```

#### Throws

If the linking fails (e.g., invalid token, account already linked).

***

### addThirdParty()

> **addThirdParty**(`params`): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:134](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L134)

Associates a third-party account with the current player's Beamable account.

#### Parameters

##### params

[`ThirdPartyCredentialParams`](../interfaces/ThirdPartyCredentialParams.md)

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// add third-party credentials
const playerAccount = await account.addThirdParty({
  provider: ThirdPartyAuthProvider.Google,
  token: 'google-auth-token',
});
```

#### Throws

If the association fails (e.g., invalid token, account already linked).

***

### confirmEmailUpdate()

> **confirmEmailUpdate**(`params`): `Promise`<`void`\>

Defined in: [src/services/AccountService.ts:445](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L445)

Confirms an email update process for the current player's account using a provided confirmation code and password.

#### Parameters

##### params

[`EmailUpdateConfirmation`](../../schema/type-aliases/EmailUpdateConfirmation.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// confirm email update
await account.confirmEmailUpdate({
  code: 'confirmation-code',
  password: 'current-password',
});
```

#### Throws

If the confirmation fails (e.g., invalid code, incorrect password).

***

### confirmPasswordUpdate()

> **confirmPasswordUpdate**(`params`): `Promise`<`void`\>

Defined in: [src/services/AccountService.ts:495](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L495)

Confirms a password update process for the current player's account using a provided confirmation code and new password.

#### Parameters

##### params

[`PasswordUpdateConfirmation`](../../schema/type-aliases/PasswordUpdateConfirmation.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// confirm password update
await account.confirmPasswordUpdate({
  code: 'confirmation-code',
  newPassword: 'new-password',
});
```

#### Throws

If the confirmation fails (e.g., invalid code, invalid new password).

***

### current()

> **current**(): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:75](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L75)

Fetches the current player's account information.

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const playerAccount = await beam.account.current();
// server-side:
const playerAccount = await beamServer.account(playerId).current();
```

#### Throws

If the request fails.

***

### getEmailCredentialStatus()

> **getEmailCredentialStatus**(`params`): `Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

Defined in: [src/services/AccountService.ts:315](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L315)

Checks the status of an email credential.

#### Parameters

##### params

[`EmailCredentialParams`](../interfaces/EmailCredentialParams.md)

#### Returns

`Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// check the status of an email credential
const status = await account.getEmailCredentialStatus({
  email: 'player@example.com',
});
if (status === CredentialStatus.NotAssigned) {
  console.log('Email credential not assigned.');
}
```

***

### getExternalIdentityStatus()

> **getExternalIdentityStatus**(`params`): `Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

Defined in: [src/services/AccountService.ts:387](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L387)

Checks the status of an external identity credential.

#### Parameters

##### params

[`ExternalIdentityParams`](../interfaces/ExternalIdentityParams.md)

#### Returns

`Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// check the status of an external identity credential
const status = await account.getExternalIdentityStatus({
  providerService: acmeServiceClient.serviceName,
  providerNamespace: acmeServiceClient.federationIds.acme,
  externalUserId: 'acme-user-id',
});
if (status === CredentialStatus.NotAssigned) {
  console.log('External identity credential not assigned.');
}
```

***

### getThirdPartyStatus()

> **getThirdPartyStatus**(`params`): `Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

Defined in: [src/services/AccountService.ts:350](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L350)

Checks the status of a third-party credential.

#### Parameters

##### params

[`ThirdPartyCredentialParams`](../interfaces/ThirdPartyCredentialParams.md)

#### Returns

`Promise`<[`CredentialStatus`](../enumerations/CredentialStatus.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// check the status of a third-party credential
const status = await account.getThirdPartyStatus({
  provider: ThirdPartyAuthProvider.Google,
  token: 'google-auth-token',
});
if (status === CredentialStatus.NotAssigned) {
  console.log('Google credential not assigned.');
}
```

***

### initiateEmailUpdate()

> **initiateEmailUpdate**(`params`): `Promise`<`void`\>

Defined in: [src/services/AccountService.ts:421](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L421)

Initiates an email update process for the current player's account.

#### Parameters

##### params

[`EmailUpdateRequest`](../../schema/type-aliases/EmailUpdateRequest.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// initiate email update
await account.initiateEmailUpdate({
  email: 'new-email@example.com',
});
```

#### Throws

If the initiation fails (e.g., email already in use, invalid email).

***

### initiatePasswordUpdate()

> **initiatePasswordUpdate**(`params`): `Promise`<`void`\>

Defined in: [src/services/AccountService.ts:468](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L468)

Initiates a password update process for the current player's account.

#### Parameters

##### params

[`EmailCredentialParams`](../interfaces/EmailCredentialParams.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// initiate password update
await account.initiatePasswordUpdate({
  email: 'player@example.com',
});
```

#### Throws

If the initiation fails (e.g., invalid email).

***

### removeExternalIdentity()

> **removeExternalIdentity**(`params`): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:282](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L282)

Removes an external identity association from the current player's Beamable account.

#### Parameters

##### params

[`ExternalIdentityParams`](../interfaces/ExternalIdentityParams.md)

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// remove an external identity
const playerAccount = await account.removeExternalIdentity({
  providerService: acmeServiceClient.serviceName,
  providerNamespace: acmeServiceClient.federationIds.acme,
  externalUserId: 'acme-user-id',
});
```

#### Throws

If the disassociation fails (e.g., invalid token, account not linked).

***

### removeThirdParty()

> **removeThirdParty**(`params`): `Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

Defined in: [src/services/AccountService.ts:247](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AccountService.ts#L247)

Removes a third-party account association from the current player's Beamable account.

#### Parameters

##### params

[`ThirdPartyCredentialParams`](../interfaces/ThirdPartyCredentialParams.md)

#### Returns

`Promise`<[`AccountPlayerView`](../../schema/type-aliases/AccountPlayerView.md)\>

#### Example

```ts
// client-side:
const account = beam.account;
// server-side:
const account = beamServer.account(playerId);
// remove third-party credentials
const playerAccount = await account.removeThirdParty({
  provider: ThirdPartyAuthProvider.Google,
  token: 'google-auth-token',
});
```

#### Throws

If the disassociation fails (e.g., invalid token, account not linked).
