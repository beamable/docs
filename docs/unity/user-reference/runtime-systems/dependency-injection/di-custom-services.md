# Custom Services

One benefit of a dependency injection system is the ability to override existing service implementations, or provide new services for custom use cases. 

## Adding Services

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

## Modifying Services

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
