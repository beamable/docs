# Dependency Service Lifecycle

Every service in the dependency scope follows a life cycle determined by the service's registration type, and how the dependency scope is disposed. 

A service is instantiated **only** when it is requested from a call to the `IDependencyProvider.GetService<T>()`, _or_ because the service is required to construct a requested service. 

## Service Types

Every service has a _Service Registration Type_. The type defines the life cycle of the service instance itself. There are only 3 types, _Singleton_, _Scoped_, and _Transient_ . 

### Singleton

Perhaps the most common, the singleton service type is used when there should only ever be a single instance of the service per dependency scope. A single instance will be created when the service is requested, and that instance will be cached inside the dependency scope. Additional calls to get the service will return the cached instance. 

Services that are registered as singletons can safely use internal state to manage business logic, because the same class instance will always be used to handle method invocations. 

If the service scope is forked, the forked scope inherits all existing singletons. A forked scope will not re-create instances of a singleton service. 

### Scoped

A scoped service is similar to a singleton service, except that a new service will be created for children scopes. The term, _scoped_, implies that there is a service instance per scope, and new scopes can only be created by forking a new child scope from the original parent scope. 

Similar to singletons, once a scope has created a scoped instance, the instance will be cached and returned for all subsequent resolutions on the scope.

### Transient

Transient service instances are never cached. Every time a transient service is requested, a new instance will be created.

## Disposing Services

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

## Hierarchical Scopes

A dependency scope represents a group of related services that use each other as internal dependencies. A scope can spawn a new child scope; a process referred to as "scope forking". A child scope inherits all previously configured service registrations. Additionally, all singleton instances from the parent scope are used in the child scope. However, any service registered as a scoped service will instantiate new instances for the child scope. Transient services (as always), result in new instances.

If a parent dependency scope is disposed, then all child scopes will be disposed as well.

When a scope is forked, there is an opportunity to modify service registrations for the child scope. The service registrations could be appended or mutated. In practice, this is used to provide _context_ to a specific scope.

```csharp
var child = scope.Fork(builder =>
{
    builder.AddScoped<ExampleService>();
});
```
