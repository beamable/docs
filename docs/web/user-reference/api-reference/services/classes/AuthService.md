[beamable-sdk](../../modules.md) / [services](../README.md) / AuthService

# Class: AuthService

Defined in: [src/services/AuthService.ts:52](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L52)

## Extends

- [`ApiService`](ApiService.md)

## Constructors

### Constructor

> **new AuthService**(`props`): `AuthService`

Defined in: [src/services/AuthService.ts:53](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L53)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`AuthService`

#### Overrides

`ApiService.constructor`

## Methods

### handleThirdPartyAuthFlow()

> **handleThirdPartyAuthFlow**(`params`): `Promise`<`void`\>

Defined in: [src/services/AuthService.ts:247](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L247)

Orchestrates a third-party login / linking flow

#### Parameters

##### params

[`LoginWithThirdPartyParams`](../interfaces/LoginWithThirdPartyParams.md)

#### Returns

`Promise`<`void`\>

#### Remarks

This method handles the logic for logging in with a third-party provider
or linking a third-party account to an existing Beamable account.
This will only work in the client SDK and auto refresh the Beam instance.

#### Example

```ts
await beam.auth.handleThirdPartyAuthFlow({
  provider: ThirdPartyAuthProvider.Google,
  token: 'google-auth-token',
});
```

#### Throws

If the authentication flow fails.

***

### loginAsGuest()

> **loginAsGuest**(): `Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

Defined in: [src/services/AuthService.ts:71](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L71)

Authenticates a guest user.

#### Returns

`Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

#### Example

```ts
const tokenResponse = await beam.auth.loginAsGuest();
await beam.refresh(tokenResponse);
```

#### Throws

If the authentication fails.

***

### loginWithEmail()

> **loginWithEmail**(`params`): `Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

Defined in: [src/services/AuthService.ts:96](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L96)

Authenticates a user with an email and password.

#### Parameters

##### params

[`LoginWithEmailParams`](../interfaces/LoginWithEmailParams.md)

#### Returns

`Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

#### Example

```ts
const tokenResponse = await beam.auth.loginWithEmail({
  email: "user@example.com",
  password: "password123"
});
await beam.refresh(tokenResponse);
```

#### Throws

If the authentication fails.

***

### loginWithExternalIdentity()

> **loginWithExternalIdentity**(`params`): `Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

Defined in: [src/services/AuthService.ts:159](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L159)

Authenticates a user with an external identity.

#### Parameters

##### params

[`LoginWithExternalIdentityParams`](../interfaces/LoginWithExternalIdentityParams.md)

#### Returns

`Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

#### Example

```ts
const tokenResponse = await beam.auth.loginWithExternalIdentity({
  externalToken: 'acme-auth-token',
  providerService: acmeServiceClient.serviceName,
  providerNamespace: acmeServiceClient.federationIds.acme,
  // optional
  challengeHandler: (challenge) => {
    // Handle the challenge, e.g., by displaying a CAPTCHA or OTP to the user
    return prompt(challenge);
  },
});
await beam.refresh(tokenResponse);

```

#### Throws

If the authentication fails.

***

### loginWithThirdParty()

> **loginWithThirdParty**(`params`): `Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

Defined in: [src/services/AuthService.ts:123](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L123)

Authenticates a user with a third-party provider (e.g., Google, Facebook).

#### Parameters

##### params

[`LoginWithThirdPartyParams`](../interfaces/LoginWithThirdPartyParams.md)

#### Returns

`Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

#### Example

```ts
const tokenResponse = await beam.auth.loginWithThirdParty({
  provider: ThirdPartyAuthProvider.Google,
  token: "google-auth-token"
});
await beam.refresh(tokenResponse);
```

#### Throws

If the authentication fails.

***

### refreshAuthToken()

> **refreshAuthToken**(`params`): `Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

Defined in: [src/services/AuthService.ts:313](https://github.com/beamable/BeamableProduct/blob/8522a95acdbee31d2e40c5c43a7ae65ea7f2809f/web/src/services/AuthService.ts#L313)

Requests a new access token using the stored refresh token.

#### Parameters

##### params

[`RefreshTokenParams`](../interfaces/RefreshTokenParams.md)

#### Returns

`Promise`<[`TokenResponse`](../../schema/type-aliases/TokenResponse.md)\>

#### Example

```ts
const tokenResponse = await beam.auth.refreshAuthToken({
  refreshToken: "your-refresh-token"
});
```

#### Throws

If the refresh token is invalid or the request fails.
