# Setting Up The Sample Projects

Beamable provides sample projects for Unreal as part of the Beamable Unreal SDK repository. Each sample is tied to a plugin named `BEAMPROJ_<PluginName>` of a shared `BeamableUnreal` project. The sample you see in the editor is determined by which `BEAMPROJ_` plugin is enabled in the BeamableUnreal.uproject file.

## Preparing the Environment
1. Install Dependencies
      - NET 8.0
      - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone the UnrealSDK Repository
      - Clone the [UnrealSDK](https://github.com/Beamable/UnrealSDK) repository if you didn't yet
      - Run the `prepare_repo.sh` Script. (GitBash is recommended, but any similar shell works.)

## Select the Sample to Run

1. Use `dotnet beam unreal select-sample BEAMPROJ_<PluginName>` to switch to the plugin (and thus the sample) you want. During this process all of the content in their `Override` folder will be copied to the `BeamableUnreal` project replacing any previous configuration. This replaces the whole "Context" in which the project is configured, enabling multiple samples in the same project.
2. For example, `dotnet beam unreal select-sample BEAMPROJ_Beamball` switches the repo to the Beamball sample
3. If using Rider as IDE and already in the BeamableUnreal.sln project you can alternatively select and run the `SET BEAMPROJ - <PluginName>` in the Configuration Drop Down (Top Right Corner)

## Build and Run in Editor

1. Open the generated `.sln` file in your IDE (e.g., Visual Studio, Rider...).
2. Perform a Clean build of the Editor target.
3. Run the `BeamableUnreal` Project and in the editor, go to Project Settings → Beamable Core → Beamable Environment and verify it’s set to `BeamProdEnv`.
4. Sign in to your Beamable account in the Beamable Window.
5. Follow Sample-Specific Instructions. Each sample has its own documentation for additional steps or guidance.

!!! warning "I can't find the Beamable Core Content in the Content Browser"
      UE's Content Browser does not show Plugin content folders by default. If you want to see these, you need to turn it on at `Content Browser -> Settings -> Show Plugin Content`.

!!! warning "Clean Up Sample Realms"
      If you are using your own organization (the one you’ll use to ship your game) to test any of these samples, don’t forget to delete the test realms when you’re finished exploring!



## Why a Single Repository?
All Beamable samples live in the main repository for two reasons:

- **QA**: Beamable continuously develops and tests against the samples
- **Up-to-date samples**: Whenever the SDK is updated, the sample projects are updated too. Maintaining samples alongside core features keeps everything stable and consistent

To make this work, the `Config` and `.beamable` folders are kept in sync by:

- A custom `Target.cs` code that makes the `Config` and `.beamable` folders at the root level of the repo exact copies of the folders inside the `Overrides` directory of each `BEAMPROJ_` folder. In other words, the contents of those folders at the root level is defined by the selected `BEAMPROJ`.
- An editor subsystem called `BeamProjSync` that, while the editor is running, file-watches those directories and copies changes made over to the appropriate `BEAMPROJ_` `Overrides` folder.
- Those implementations are only related to the specificity of this sample configuration and it is not related to the samples' content themselves
