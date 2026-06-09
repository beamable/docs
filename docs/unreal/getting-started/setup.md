# Setup: Beamable Unreal SDK

This page walks through the process of downloading and setting up the Beamable SDK in your Unreal Engine project.

## Signup requirement

To start using Beamable in your project you need to have a valid Account in the [Beamable Portal](https://portal.beamable.com/signup/registration). Remember your **Alias**, as it is used to log in to the SDK through your editor or the Beamable CLI.

## Project requirements
Important notes and dependencies:

| Requirement | Version | Notes |
|-------------|---------|-------|
| [Unreal Engine](https://www.unrealengine.com/) | **5.6.X** | The project must be C++ (though there is extensive [Blueprint](../user-reference/runtime-systems/blueprints.md) support for most functionality). |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Latest stable version | Required for **building and deploying Microservices** and for running Microservices locally with MicroStorages without opening the service project. |
| [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | **8.0** | Needed for installing and running Beamable tooling and for running **C# Microservices** through the CLI. |


## Downloading and installing the SDK
- Download the latest version of the Beamable Unreal SDK from the [GitHub Repository](https://github.com/beamable/UnrealSDK/releases)
- Unzip the contents of the downloaded file to a location where you can easily find it

Once you have the repo and dependencies set up, follow the next section to set up the SDK in your project.

## Setting up the SDK in your project
Now that you have the SDK downloaded, you can set it up in your Unreal Project. The steps to do so are slightly different depending on your OS.

### Running initialization script
Run the `beam_init_game_maker.sh` script to set up the SDK in your project. The script copies the necessary files from the UnrealSDK repo to your project and writes the configuration files.

=== "Windows"
    1. Copy the `beam_init_game_maker.sh` script into the root directory of your Unreal Project
    2. From a terminal (on windows, **GitBash**) running in your project directory, run `beam_init_game_maker.sh` passing in the path to the **UnrealSDK** in your machine
        1. `. beam_init_game_maker.sh "E:/Path/To/UnrealSDK"`

=== "macOS"
    1. Copy the `beam_init_game_maker.sh` script into the root directory of your Unreal Project
    2. From a terminal, running in your project directory, run `beam_init_game_maker.sh` passing in the path to the **UnrealSDK** in your machine
        1. Run `chmod +x ./beam_init_game_maker.sh` before running the script
        2. `. beam_init_game_maker.sh "/Users/Me/Path/To/UnrealSDK"`

### Setting up modules
After the script runs, set up your project's `Target.cs` and `Build.cs` files to include Beamable's SDK.

**For each of your `Target.cs` files, add the following lines to their constructor**:

| File                        | Configuration Code |
|-----------------------------|--------------------|
| `MyProject.Target.cs`       | `Beam.ConfigureGame(this, Beam.OssConfig.Disabled())` |
| `MyProjectEditor.Target.cs` | `Beam.ConfigureEditor(this, Beam.OssConfig.Disabled())` |
| `MyProjectServer.Target.cs` | `Beam.ConfigureServer(this, Beam.OssConfig.Disabled())` *(only if you have dedicated server builds)* |

**In each of the Modules you want to use Beamable's SDK, add this to their `Build.cs` files**:

| Module Type                   | Configuration Code |
|-------------------------------|--------------------|
| `RuntimeModule.Build.cs`      | `Beam.AddRuntimeModuleDependencies(this);` |
| `EditorModule.Build.cs`       | `Beam.AddEditorModuleDependencies(this);` |
| `UncookedOnlyModule.Build.cs` | `Beam.AddUncookedOnlyModuleDependencies(this);` |

Call the function that matches the module type — check your `uproject` file to confirm.

### Verifying installation and running
Check that everything is set up correctly by compiling the project.

=== "Windows"
    1. Regenerate project files
        1. Right-click the `.uproject` file and select `Generate Visual Studio project files`
    2. Verify that your project is set up correctly by going to your project's root directory:
        1. Check if there is a `.beamable` folder there
        2. Check if there is a `.config/dotnet-tools.json` file
        3. Run `dotnet beam --version` from inside your project root directory and see that it outputs a valid `X.Y.Z` string
    3. Open your IDE and compile your editor

=== "macOS"
    1. Regenerate project files
        1. From a terminal, run `sh "/Users/Shared/Epic Games/UE_5.5/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh" "/Users/Path/To/Your/Project/YourProject.uproject" -game`
    2. Verify that your project is set up correctly by going to your project's root directory:
        1. Check there is a `.beamable` folder there
        2. Check there is a `.config/dotnet-tools.json` file
        3. Run `dotnet beam --version` from inside your project root directory and see that it outputs a valid `X.Y.Z` string
    3. Open your IDE and compile your editor

You are now ready to make your [first request](../getting-started/first-request.md) with Beamable.

## Upgrading the SDK
Upgrading the SDK follows the same steps as the initial setup, with one difference: re-apply any custom changes you made to the SDK after the upgrade.

1. Download the latest [tagged release version](https://github.com/beamable/UnrealSDK/releases)
2. Run through the steps in the [Setup SDK](#setting-up-the-sdk-in-your-project) section
3. If you made any custom changes to the SDK, use Git to re-apply them. Flag custom changes with a comment when you make them, so they are easy to find during this step
4. Fix any compilation errors caused by breaking changes. Also fix any blueprints after the editor compiles
5. Run `dotnet tool restore` from your project root
6. Verify that the CLI was updated to the proper version by running `dotnet beam version` and seeing that it matches the version in `E:/Path/To/UnrealSDK/.config/dotnet-tools.json`
7. If you have microservices:
    1. From your microservice project's directory, run `dotnet restore`
    2. Verify that the CLI was updated to the proper version by running `dotnet beam version` from the microservice directory
    3. Run `dotnet beam checks scan --fix all`
        1. The CLI can fix _some_ breaking changes automatically with this command
