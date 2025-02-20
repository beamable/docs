# Setup Beamable SDK
This guide will walk you through the process of setting up Beamable in your Unreal Engine project

## Signing Up Account
To start using Beamable in your project you need to have a valid Account in our Platform. you can sign-up an account in [our portal](https://portal.beamable.com/login/).

## Cloning and Installing Dependencies
Start by getting our repo, then installing .NET and Docker Dekstop.

 1. Clone [UnrealSDK](https://github.com/beamable/UnrealSDK) repo (make sure you have `git-lfs` installed).
 2. Check out the a [tagged release version](https://github.com/beamable/UnrealSDK/releases) (in the form `X.X.X`).
	 1. Most `git` clients will allow you to checkout a specific tagged commit via their UI.
	 2. At Beamable, we're partial to [Fork](https://git-fork.com/).
 3. Run the `prepare_repo.sh` script.
	 1. On Windows, use the **GitBash** that your `git` install contains.
 4. Generating Project Files.
	 1. On Windows, you can right-click the `.uproject` file and select `Generate Visual Studio project files`.
 5. Optional - Verify things are working by compiling the editor of our SDK project.

Next up, install our dependencies.

 - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - [.NET](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)

Once you have our repo and dependencies set up in your machine, follow along one of the next section to set up the SDK in your project.

## Set up the Beamable SDK - Fast Path
Setting up the SDK in your project is done by manually copying over a set of files from our **Unreal SDK** repo to your project. 

!!! note "Unreal Project Requirements"
	Beamable requires your Unreal project to be a C++ project. That being said, we do provide an entire suite of Blueprint nodes that can be used to achieve *most* of the same functionality.

Please, follow along these instructions:

1. Copy the `beam_init_game_maker.sh` script into the root of your Unreal Project.
2. From a terminal running in your project directory, run the copied script passing in the path to the **UnrealSDK** in your machine.
	1. `. beam_init_game_maker.sh "E:/Path/To/UnrealSDK"`
	2. `. beam_init_game_maker.sh "E:/Path/To/UnrealSDK" true`, if you're planning to use the `OnlineSubsystemBeamable`.
3. For each of your `Target.cs` files, add the following lines to their constructor:
	1. `MyProject.Target.cs => Beam.ConfigureGame(this, Beam.OssConfig.Disabled())`.
	2. `MyProjectEditor.Target.cs => Beam.ConfigureEditor(this, Beam.OssConfig.Disabled())`.
	3. `MyProjectServer.Target.cs => Beam.ConfigureServer(this, Beam.OssConfig.Disabled())`, if you have dedicated server builds.
4. In each of the Modules you want to use Beamable's SDK, add this to their `Build.cs` files:
	1. `RuntimeModule.Build.cs => Beam.AddRuntimeModuleDependencies(this);`
	2. `EditorModule.Build.cs => Beam.AddEditorModuleDependencies(this);`
	3. `UncookedOnlyModule.Build.cs => Beam.AddUncookedOnlyModuleDependencies(this);`
	4. Pay attention to the type of module you're adding the SDK to and call the proper function. (You can see the module type in your `uproject` file)
5. Some OS-specific things:
	1. On MacOS, you'll have to manually regenerate project files. 
	2. On Windows, this was done by `beam_init_game_maker.sh` script.
6. Verify that your project is set up correctly:
	1. Check there is a `.beamable` folder in your project root directory.
	2. Check there is a `.config/dotnet-tools.json` file in your project directory.
	3. Run `dotnet beam --version` from inside your project root directory and see that it outputs a valid `X.Y.Z` string.
7. Open Rider/VS and compile your editor.


