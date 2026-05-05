# Unreal Online Subsystems

!!! warning "Will Be Discontinued"
    After a thorough evaluation conducted with Beamable's closest game-maker partners and their projects, Beamable has decided to discontinue the `OnlineSubsystemBeamable` Plugin extension.

    Beamable has many of unique, useful features that become harder to use when hidden behind the OnlineSubsystem interface. Supporting OnlineSubsystem implementations is costly but does not help developers as much as originally anticipated. OnlineSubsystem upport is being phased out in favor of the `BeamableCore` plugin, docs, samples, and a showcase project that will show how to best use Beamable inside UE for a live-services game project.

    The discontinuation will come into effect at the last release this year but no more updates to it will happen to this documentation or the package from now until then.

To use the Online Subsystem integration to Unreal Online Subsystems, update your `*.Target.cs` 's `Beam.ConfigureGame` method call. As well as re-running, `beam-init-game-maker.sh "Path/To/SDK/Clone" true` with a second argument as true.

The Enabling Online Subsystem would require updating the value of the second argument of that method, `Beam.OssConfig` value, example values for Hathora sample project:

```csharp
var oss = new Beam.OssConfig()
{
    IsEnabled = true,

    HooksEnabled = true,
    HookSubsystemImplementation = "FOnlineSubsystemHathoraDemo",
    HookSubsystemIncludePath = "Customer/OnlineSubsystemHathoraDemo.h",

    AdditionalHookModules = new[] { "HathoraSDK" }
};
```
