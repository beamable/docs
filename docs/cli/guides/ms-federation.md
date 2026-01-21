# Microservice Federation

Federate Standalone Microservices with external services

## Dependencies

Before you can federate using Beamable Standalone Microservices, you need to complete the [Getting-Started Guide](getting-started.md). That means having [Dotnet 10](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) installed, and getting the  [Beam CLI](https://www.nuget.org/packages/Beamable.Tools). 

You can confirm you have everything installed checking the versions of the tools.
```sh
dotnet --version
beam version # beam --version also works.
```

In order to federate using a Microservice, you also need to have a local `.beamable` workspace with a Beamable Standalone Microservice. As a reminder, you can create one quickly using the commands below.

```sh
beam init MyProject
cd MyProject
dotnet beam project new service HelloWorld
```

## Federation

Microservice _Federation_ is the ability to inject custom server logic in the middle of existing Beamable server functionality. Federation can be used to add custom behaviour to your game like supporting external identity auth providers, using a block chain as the backing data provider for player inventory, managing how match making works, and more. 

There are 4 types of federation. All of these federations have C# interfaces 
that define the types of functions that they require. 
1. `IFederatedLogin`
2. `IFederatedInventory`
3. `IFederatedGameServer`
4. `IFederatedPlayerInit`

A Microservice supports these federations when The `Microservice` class includes the associated federation interface


A service that federates login functionality may have a class signature like the following.

```csharp
public partial class ExampleService : IFederatedLogin<MySample> 
{
	// implementation
}
```

The `MySample` class included as the generic type in the `IFederatedLogin` interface specifies the id for the federated login. The class signature for these types must implement the `IFederationId` type, and be annotated with a `FederationId` attribute. The string argument for the attribute constructor must be stable between releases of your service. It also needs to be unique.

```csharp
[FederationId("myId")]
public class MySample : IFederationId { }
```

### Federated Login

This feature allows you to implement OAuth2, OpenID Connect, or custom external authentication providers within Beamable. It also supports two-way, challenge-based flows for PKI-based authentication, commonly used in Web3/blockchain scenarios.

#### Use Cases

- **Blockchain Wallet Authentication**: Attach a wallet to a player's account and use it for secure authentication.
- **External Provider Integration**: Integrate with providers like **Auth0** to provide a Single Sign-On (SSO) experience for your game.

#### Implementation

To add support for federated login, implement the `IFederatedLogin<FederationId>` interface. This interface requires the implementation of the `Authenticate` method, which is used to verify a player's identity via the federated provider. This method supports both standard single-step authentication and two-step challenge-response flows.

It can be used for 2 step verification as well as regular authentication.

!!! info "User Id generation"

    Ensure that User IDs are generated deterministically. For a given input from the provider, the resulting User ID must always be the same. Avoid using `Guid.NewGuid().ToString()`, as this creates a new account for every login attempt. Instead, use a unique identifier provided by the external auth provider (e.g., a subject ID or public key).

#### Simple Implementation (Single-Step)

This implementation assumes the external provider gives a token that can be validated immediately.

```csharp
public async Promise<FederatedAuthenticationResponse> Authenticate(string token, string challenge, string solution)
{
	var externalId = await CallExternalAuthProvider(token);
	return new FederatedAuthenticationResponse { user_id = externalId };
}

async Promise<string> CallExternalAuthProvider(string token)
{
    // Call external auth provider API here
    return token;
}
```

#### Two-Step Verification (Challenge-Response)

For scenarios like [Solana/Phantom wallet authentication](https://github.com/beamable/solana-example/tree/develop/Packages/com.beamable.solana/Runtime/BeamableServices~/SolanaFederation), you must issue a challenge for the client to sign.

```csharp
public Promise<FederatedAuthenticationResponse> Authenticate(string token, string challenge, string solution)
{
    if (string.IsNullOrEmpty(token))
    {
        BeamableLogger.LogError("We didn't receive a token (public key)");
        throw new InvalidAuthenticationRequest("Token (public key) is required");
    }

    if (!string.IsNullOrEmpty(challenge) && !string.IsNullOrEmpty(solution))
    {
        // Verify the solution
        if (AuthenticationService.IsSignatureValid(token, challenge, solution))
            // User identity is confirmed
            return Promise<FederatedAuthenticationResponse>.Successful(new FederatedAuthenticationResponse
                { user_id = token });
        // Signature is invalid, user identity isn't confirmed
        BeamableLogger.LogWarning(
            "Invalid signature {signature} for challenge {challenge} and wallet {wallet}", solution,
            challenge, token);
        throw new UnauthorizedException();
    }

    // Generate a challenge
    return Promise<FederatedAuthenticationResponse>.Successful(new FederatedAuthenticationResponse
    {
        challenge = $"Please sign this random message to authenticate, {Guid.NewGuid()}",
        challenge_ttl = Configuration.AuthenticationChallengeTtlSec
    });
}
```

---

## CLI Commands

The CLI offers a few commands to enable and disable federations for a service. The `beam fed` command suite allows you to read and write federation data. None of the commands will modify your C# source files. 

The `beam fed list` command will show all federations for all services. 
```sh
dotnet beam fed list
 {                                                                               
    "cid": "1338004997867618",                                                   
    "pid": "DE_1754280032981028",                                                
    "services": [                                                                
       {                                                                         
          "beamoName": "ExampleService",                                         
          "routingKey": "chriss-macbook-pro-2_59e8e38ad189aefe093dfa7d74e18841", 
          "federations": {                                                       
             "myId": [                                                           
                {                                                                
                   "interface": "IFederatedLogin"                                
                }                                                                
             ]    
            
```

---

## Possible Issues and Solutions

### Invalid Federation Id detected

**Example Code Triggering the Error**:
```csharp
[FederationId("123-MyFederation")]
public class MyFederation : IFederationId {}

public partial class MyMicroservice : Microservice, IFederatedInventory<MyFederation> {}
```

**Example Error Message**:
```
The following IFederationId is invalid. They must: Start with a letter. Contain only alphanumeric characters and/or `_`. Microservice=MyMicroservice, Id=123-MyFederation.
```

**Solutions**:
- Rename the federation ID to follow the format, e.g. `MyFederation`.

---

### IFederationId is missing FederationIdAttribute

**Example Code Triggering the Error**:
```csharp
public class MyFederation : IFederationId {}
```

**Example Error Message**:
```
IFederationId is missing FederationIdAttribute
```

**Solutions**:
- Add the attribute to your federation class:
  ```csharp
  [FederationId("MyFederation")]
  public class MyFederation : IFederationId {}
  ```

---

### IFederationId must be default

**Example Code Triggering the Error**:
```csharp
public class MyFederation : IFederationId {}
```

**Example Message**:
```
The following IFederationId must be annotated with a FederationIdAttribute with a value of "default", Id=MyFederation
```

**Solutions**:
- Update the federation interface:
  ```csharp
  [FederationId("default")]
  public interface MyFederation : IFederationId {}
  ```

---
