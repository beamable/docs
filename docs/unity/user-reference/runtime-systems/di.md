# Dependency Injection Overview

The Beamable SDK uses a dependency injection system to manage the creation and life cycle of services used throughout the SDK. The dependency injection system is built around the `IDependencyProvider` interface, which is responsible for creating and managing service instances.

## Dependency Service Lifecycle

Every service in the dependency scope follows a life cycle determined by the service's registration type, and how the dependency scope is disposed. 

A service is instantiated **only** when it is requested from a call to the `IDependencyProvider.GetService<T>()`, _or_ because the service is required to construct a requested service. 

### Service Types

Every service has a _Service Registration Type_. The type defines the life cycle of the service instance itself. There are only 3 types, _Singleton_, _Scoped_, and _Transient_ . 

#### Singleton

Perhaps the most common, the singleton service type is used when there should only ever be a single instance of the service per dependency scope. A single instance will be created when the service is requested, and that instance will be cached inside the dependency scope. Additional calls to get the service will return the cached instance. 

Services that are registered as singletons can safely use internal state to manage business logic, because the same class instance will always be used to handle method invocations. 

If the service scope is forked, the forked scope inherits all existing singletons. A forked scope will not re-create instances of a singleton service. 

#### Scoped

A scoped service is similar to a singleton service, except that a new service will be created for children scopes. The term, _scoped_, implies that there is a service instance per scope, and new scopes can only be created by forking a new child scope from the original parent scope. 

Similar to singletons, once a scope has created a scoped instance, the instance will be cached and returned for all subsequent resolutions on the scope.

#### Transient

Transient service instances are never cached. Every time a transient service is requested, a new instance will be created.

### Disposing Services

A dependency scope can be in one of two states, active, or disposed. A scope is active the moment it is built. However, a scope can be disposed through the `IDependencyProviderScope.Dispose()` method. When a `BeamContext` is stopped, the associated `IDependencyProvider` will be disposed. When a scope is disposed, no calls to `GetService<T>()` are allowed. 

The `IBeamableDisposable` interface informs the dependency scope that a service requires some sort of disposal logic before the scope is finished transitioning to the disposed state. In the example code below, the `ExampleService` will print a log message when the service scope is disposed. If you are implementing custom services that require stateful operation, consider using the `IBeamableDisposable` interface. However, the Beamable SDK does not guarantee that a `BeamContext` will be stopped when the game is quit, and therefor, does not guarantee that the service scope will be disposed. 

```csharp
public class ExampleService : IBeamableDisposable
{
	public Promise OnDispose()
	{
		Debug.Log("cleaning up.");
		return Promise.Success;
	}
}
```

!!! warning "Transient services do not use IBeamableDisposable"
    Any service registered as Transient will not honor the `IBeamableDisposable` interface. Transient services are not meant to contain any state.

### Hierarchical Scopes

A dependency scope represents a group of related services that use each other as internal dependencies. A scope can spawn a new child scope; a process referred to as "scope forking". A child scope inherits all previously configured service registrations. Additionally, all singleton instances from the parent scope are used in the child scope. However, any service registered as a scoped service will instantiate new instances for the child scope. Transient services (as always), result in new instances.

If a parent dependency scope is disposed, then all child scopes will be disposed as well.

When a scope is forked, there is an opportunity to modify service registrations for the child scope. The service registrations could be appended or mutated. In practice, this is used to provide _context_ to a specific scope.

```csharp
var child = scope.Fork(builder =>
{
    builder.AddScoped<ExampleService>();
});
```

## Custom Services

One benefit of a dependency injection system is the ability to override existing service implementations, or provide new services for custom use cases.

### Adding Services

The Beamable SDK has a global `IDependencyBuilder` available via `Beam.DependencyBuilder`. Despite the `IDependencyBuilder` being accessible globally, the correct way to modify service registrations is to create a static method that meets the following requirements...

1. Is in a class marked with the `BeamContextSystem` attribute,
2. Is a method marked with the `RegisterBeamableDependencies` attribute,
3. takes 1 input parameter of type, `IDependencyBuilder`

The example below will receive the `IDependencyBuilder`and add a singleton `ExampleService`.

```csharp
[BeamContextSystem]
public class CustomRegistrations
{
	[RegisterBeamableDependencies]
	public static void Register(IDependencyBuilder builder)
	{
		builder.AddSingleton<ExampleService>();
	}
}
```

The `RegisterBeamableDependencies` takes two arguments, `order`, and `origin` that control which dependency scope is being configured, and in what order.

The `origin` option is an enum that is `RegistrationOrigin.RUNTIME` by default. The other option is `RegistrationOrigin.EDITOR`. Beamable uses the same dependency injection concepts in the Unity Editor environment as well. If you want to override an editor service, set the origin to `EDITOR`.

The `order` option controls the invocation ordering of `RegisterBeamableDependencies` methods. Ideally, all custom services should be registered in a single `RegisterBeamableDependencies` method. However, sometimes due to logical separation or package separation, it isn't possible to centralize dependency registrations. In this case, there are multiple functions tagged with the `RegisterBeamableDependencies` attribute, and the _order_ they are invoked in can drastically change the outcome. All Beamable services are registered at an effective order value of -1000. The default `order` value for all custom `RegisterBeamableDependencies` methods is 0.

### Modifying Services

In a `RegisterBeamableDependencies` method, the `IDependencyBuilder` instance can be used to _remove_ existing registrations. Beamable automatically registers all of the services it needs to operate the base SDK. However, as an advanced developer, it is possible to remove Beamable service classes and replace them with custom implementations. To find the Beamable service registration listings, see the `com.beamable/Runtime/Beam.cs`static constructor. Additionally, look for references of `RegisterBeamableDependencies` to find any special places where services are added.

In the example below, the `IDeviceIdResolver` interface reconfigured to use a custom implementation. The `IDeviceIdResolver` is the interface responsible for identifying a device identifier used for Beamable Auth Device Id.

```csharp
[BeamContextSystem]
public class CustomRegistrations
{
	[RegisterBeamableDependencies]
	public static void Register(IDependencyBuilder builder)
	{
		builder.ReplaceSingleton<IDeviceIdResolver, ExampleService>();
	}
}

public class ExampleService : IDeviceIdResolver
{
	public Promise<string> GetDeviceId()
	{
		throw new NotImplementedException();
	}
}
```

## Microservices

The Beamable Unity SDK uses `IDependencyBuilder` and `IDependencyProvider` to manage dependencies. Beamable Microservices use the same structures to manage their dependencies as well. The same concepts from the SDK apply in the Microservices, but some minor details change.

### Life Cycle

When a Microservice starts, there is one main `IDependencyBuilder` . In order to initialize and connect to Beamable, the `IDependencyBuilder` creates a main `IDependencyProvider`. However, every request sent to a Microservice will get a unique `IDependencyProvider`. The main scope is forked and modified with the `RequestContext` information for the request. When the request terminates, the child scope is disposed.

#### Scoped vs Singleton

In a Microservice, a service registered as a singleton will be the only instance of that service between all requests. It can be used to store a limited amount of state between service requests.

!!! warning "Do not store critical state in memory"
Remember that a Microservice may be running multiple instances when deployed. This means that you should not assume that a singleton's class variables are stable across _all_ requests. They are only stable for requests sent to the given instance of the Microservice.

A scoped service will be re-instantiated for each request.

### Service Registration

In order to add or modify service registrations, the `Microservice` class must have a static method that is tagged with the `ConfigureServices` attribute, and accepts an `IServiceBuilder` instance. The `IServiceBuilder` has a `.Builder` accessor that exposes a `IDependencyBuilder`.

```csharp
[ConfigureServices]
public static void Configure(IServiceBuilder builder)
{
  builder.Builder.AddScoped<ExampleService>();
}
```

### Service Resolution

In a Microservice, you can access the request's `IDependencyProvider` through the internal class members of the `Microservice` class.

```csharp
[ClientCallable]
public void Test()
{
    var service = Provider.GetService<ExampleService>();
}
```
