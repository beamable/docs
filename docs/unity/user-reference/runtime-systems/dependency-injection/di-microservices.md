# Microservices

The Beamable Unity SDK uses `IDependencyBuilder` and `IDependencyProvider` to manage dependencies. Beamable Microservices use the same structures to manage their dependencies as well. The same concepts from the SDK apply in the Microservices, but some minor details change. 

## Life Cycle

When a Microservice starts, there is one main `IDependencyBuilder` . In order to initialize and connect to Beamable, the `IDependencyBuilder` creates a main `IDependencyProvider`. However, every request sent to a Microservice will get a unique `IDependencyProvider`. The main scope is forked and modified with the `RequestContext` information for the request. When the request terminates, the child scope is disposed. 

### Scoped vs Singleton

In a Microservice, a service registered as a singleton will be the only instance of that service between all requests. It can be used to store a limited amount of state between service requests. 

!!! warning "Do not store critical state in memory"
    Remember that a Microservice may be running multiple instances when deployed. This means that you should not assume that a singleton's class variables are stable across _all_ requests. They are only stable for requests sent to the given instance of the Microservice.

A scoped service will be re-instantiated for each request.

## Service Registration

In order to add or modify service registrations, the `Microservice` class must have a static method that is tagged with the `ConfigureServices` attribute, and accepts an `IServiceBuilder` instance. The `IServiceBuilder` has a `.Builder` accessor that exposes a `IDependencyBuilder`. 

```csharp
[ConfigureServices]
public static void Configure(IServiceBuilder builder)
{
  builder.Builder.AddScoped<ExampleService>();
}
```

## Service Resolution

In a Microservice, you can access the request's `IDependencyProvider` through the internal class members of the `Microservice` class. 

```csharp
[ClientCallable]
public void Test()
{
    var service = Provider.GetService<ExampleService>();
}
```
