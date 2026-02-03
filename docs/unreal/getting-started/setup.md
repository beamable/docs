# Setup: Beamable Unreal SDK

Here, we will guide you through the process of downloading and setting up the Beamable SDK in your Unreal Engine project!

## Signup Requirement

To start using Beamable in your project you need to have a valid Account in the [Beamable Portal](https://portal.beamable.com/signup/registration). Please remember your **Alias** as it'll be used to log into the SDK in your editor or via the Beamable CLI.

## Project Requirements
Important notes and dependencies:

| Requirement | Version | Notes |
|-------------|---------|-------|
| [Unreal Engine](https://www.unrealengine.com/) | **5.6.X** | The project must be C++ (though there is extensive [Blueprint](../user-reference/runtime-systems/blueprints.md) support for most functionality). |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Latest stable version | Required for **building and deploying Microservices** and for running Microservices locally with MicroStorages without opening the service project. |
| [.NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | **8.0** | Needed for installing and running Beamable tooling and for running **C# Microservices** through the CLI. |


## Downloading and Installing the SDK
- Download the Latest Version of the Unreal SDK from our [Github Repository](https://github.com/beamable/UnrealSDK/releases)
- Unzip the contents of the downloaded file to a location where you can easily find it.

Once you have our repo and dependencies set up, follow along with the next section to set up the SDK in your project.

## Setting Up the SDK in your Project
Now that you have the SDK downloaded, you can set it up in your Unreal Project. The steps to do so are slightly different depending on your OS.

### Running Initialization Script
Run the `beam_init_game_maker.sh` script to set up the SDK in your project. The script will copy over the necessary files from the UnrealSDK repo to your project and set up some configuration files.

=== "Windows"
    1. Copy the `beam_init_game_maker.sh` script into the root directory of your Unreal Project.
    2. From a terminal (on windows, **GitBash**) running in your project directory, run `beam_init_game_maker.sh` passing in the path to the **UnrealSDK** in your machine.
        1. `. beam_init_game_maker.sh "E:/Path/To/UnrealSDK"`

=== "MacOS"
    1. Copy the `beam_init_game_maker.sh` script into the root directory of your Unreal Project.
    2. From a terminal, running in your project directory, run `beam_init_game_maker.sh` passing in the path to the **UnrealSDK** in your machine.
        1. Run `chmod +x ./beam_init_game_maker.sh` before running the script.
        2. `. beam_init_game_maker.sh "/Users/Me/Path/To/UnrealSDK"`

### Setting Up Modules
Now that the script has run, you need to set up your project's `Target.cs` and `Build.cs` files to include Beamable's SDK.

**For each of your `Target.cs` files, add the following lines to their constructor:**

| File                        | Configuration Code |
|-----------------------------|--------------------|
| `MyProject.Target.cs`       | `Beam.ConfigureGame(this, Beam.OssConfig.Disabled())` |
| `MyProjectEditor.Target.cs` | `Beam.ConfigureEditor(this, Beam.OssConfig.Disabled())` |
| `MyProjectServer.Target.cs` | `Beam.ConfigureServer(this, Beam.OssConfig.Disabled())` *(only if you have dedicated server builds)* |

**In each of the Modules you want to use Beamable's SDK, add this to their `Build.cs` files:**

| Module Type                   | Configuration Code |
|-------------------------------|--------------------|
| `RuntimeModule.Build.cs`      | `Beam.AddRuntimeModuleDependencies(this);` |
| `EditorModule.Build.cs`       | `Beam.AddEditorModuleDependencies(this);` |
| `UncookedOnlyModule.Build.cs` | `Beam.AddUncookedOnlyModuleDependencies(this);` |

Pay attention to the type of module you're adding the SDK to and be sure to call the proper function (you can see the module type in your `uproject` file).

### Verifying Installation and Running
Let's Check that everything is set up correctly be sure you can compile your project.

=== "Windows"
    1. Regenerate project files.
        1. Right-click the `.uproject` file and select `Generate Visual Studio project files`. <!-- TODO(@drewbleam): Add a note for users that DON'T see this option (need to route to UE files or run a command in terminal) -->
    2. Verify that your project is set up correctly by going to your project's root directory:
        1. Check if there is a `.beamable` folder there.
        2. Check if there is a `.config/dotnet-tools.json` file.
        3. Run `dotnet beam --version` from inside your project root directory and see that it outputs a valid `X.Y.Z` string.
    3. Open your IDE and compile your editor.

=== "MacOS"
    1. Regenerate project files.
        1. From a terminal, run `sh "/Users/Shared/Epic Games/UE_5.5/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh" "/Users/Path/To/Your/Project/YourProject.uproject" -game`.
    2. Verify that your project is set up correctly by going to your project's root directory:
        1. Check there is a `.beamable` folder there.
        2. Check there is a `.config/dotnet-tools.json` file.
        3. Run `dotnet beam --version` from inside your project root directory and see that it outputs a valid `X.Y.Z` string.
    3. Open your IDE and compile your editor.

**Now you're ready to do your [First Request](../getting-started/first-request.md) with Beamable!**

## Upgrading the SDK
The Process to upgrade the SDK is similar to the initial setup. The main difference is that you need to be sure to re-apply any custom changes you made to the SDK after upgrading.

1. Download the latest [tagged release version](https://github.com/beamable/UnrealSDK/releases).
2. Run through the steps in the [Setup SDK](#setup-the-beamable-sdk-in-your-project) section.
3. If you made any custom changes to the SDK, leverage Git to re-apply them as needed. When making custom changes to the SDK, it's beneficial to flag them with a comment to make searching for them easier in this step.
4. Fix any compilation errors that happened due to breaking changes. Don't forget to fix any blueprints as well, after you get the editor to compile.
5. Run `dotnet tool restore` from your project root. 
6. Verify that the CLI was updated to the proper version by running `dotnet beam version` and seeing that it matches the version in `E:/Path/To/UnrealSDK/.config/dotnet-tools.json`.
7. If you have microservices:
    1. From your microservice project's directory, run `dotnet restore`.
    2. Verify that the CLI was updated to the proper version by running `dotnet beam version` from the microservice directory.
    3. Run `dotnet beam checks scan --fix all`.
        1. Our CLI can fix _some_ breaking changes automatically with this command.
