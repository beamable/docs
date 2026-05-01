# Unreal Online Subsystems

!!! warning "Will Be Discontinued"
    After a thorough evaluation conducted with Beamable's closest game-maker partners and their projects, Beamable has decided to discontinue the `OnlineSubsystemBeamable` Plugin extension.

    Beamable has a lot of unique features that are very useful but become a lot harder to leverage if you're keeping it behind the OnlineSubsystem interface. In other words, supporting it is costly but doesn't generate as much value to customers and partners as originally anticipated. As such, support is being phased out in favor of focusing efforts on the `BeamableCore` plugin, docs, samples and a showcase project that will show how to leverage Beamable inside UE for a live-services game project.

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
