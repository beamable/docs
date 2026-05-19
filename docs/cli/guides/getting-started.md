# Get up and running with the Beamable CLI

The Beamable CLI is a dotnet tool that allows developers to interact with Beamable. It can manage a variety of Beamable technologies, including Microservices, Content, and other services.

## Dependencies
You'll need to install [.NET 10](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) before you can get started.
Verify it is installed by running `dotnet --version` from a terminal.

!!! info ".NET 8 is also supported."

    If you are using the Beamable CLI before version 7.0, then you should be using [.NET 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0). Starting with CLI 7.0 and beyond, both versions of dotnet are supported, but `net10.0` is recommended.

## Installing
To install the Beamable CLI, run the following command in a shell.
```shell
dotnet tool install --global Beamable.Tools
```
It is also possible to install a specific version instead of the latest one using the `--version` parameter
```shell
dotnet tool install --global Beamable.Tools --version X.Y.Z
```
If you are using the Beamable CLI on Unity, please check if the installed version matches the Unity SDK version that you are using, you can use [this](https://beamable.github.io/docs/unity/getting-started/installing-beamable/#beam-cli-dependency) table to check the version.
And verify your installation with `beam version`.

### Updating
As of 1.16.2, a globally installed CLI can manage its own updates through the use of the beam version install command.

The following command will install the latest CLI. The "latest" string can be any valid CLI version
```shell
beam version install latest
```

!!! info "Check Versions on NuGet"

    Remember, Beamable.Tools is a dotnet tool available through NuGet. As such, you can find all available versions at [nuget.org](https://www.nuget.org/packages/Beamable.Tools)

There may be updates you are required to do, so please check the [migration guide](upgrading.md).

## Getting started

Now that Beamable is installed, you can connect to an existing Beamable organization. If you haven't setup an organization yet, [create a Beamable organization](https://portal.beamable.com/signup/registration/) first.

You can connect the CLI to your Beamable organization with the [beam init](../commands/cli-command-reference/init.md) command.

```shell
mkdir MyProject
beam init
```

This command will prompt you for your organization's alias, your credentials, and which realm to use. When it is complete, you should see a `./beamable` folder in the current directory. See the [Configuration](configuration.md) for details about this folder. Now, you can run a [beam config](../commands/cli-command-reference/config/config.md) command to verify your project is set up.

```shell
dotnet beam config
```
You should expect to see your CID/PID printed out.

As of CLI 3.0.0, anytime you create a Beamable workspace, the CLI will be installed as a local tool next to the workspace's `.beamable/` folder. This means that you can run the local tool with `dotnet beam`. If you continue to use `beam` in the workspace, the global installation will automatically forward your command to the local tool. This will be inefficient and lead to poor performance. Use `dotnet beam` wherever possible.

To check that everything is working correctly, you can use the beam me command. Now you have a configured CLI project!

!!! info "Finding Help"

    You can pass the `--help` flag to any command to print out detailed information about the arguments and options for the given command. Also, the `--help-all` flag will include additional information used by internal Beamable developers. You are welcome to use the internal facing commands, but they are not officially supported.

## Try a microservice locally

If you want to evaluate a Beamable microservice without integrating an engine SDK, you can scaffold an isolated C# workspace in a few commands. This path uses a local [dotnet tool manifest](https://learn.microsoft.com/en-us/dotnet/core/tools/local-tools-how-to-use), so the CLI version is pinned to the workspace and nothing is installed globally.

### Create an isolated workspace

```shell
mkdir MyService
cd MyService
dotnet new tool-manifest
dotnet tool install Beamable.Tools
```

The first three commands create the folder and register a `.config/dotnet-tools.json` manifest. The fourth installs the Beam CLI into that manifest. From this folder, `dotnet beam` runs the locally installed CLI.

### Initialize Beamable and log in

```shell
dotnet beam init
```

`dotnet beam init` prompts for your organization's alias, your credentials, and the realm to use, then writes a `.beamable/` folder alongside the tool manifest. See [`beam init`](../commands/cli-command-reference/init.md) for the full list of arguments and the [Configuration](configuration.md) guide for the layout of `.beamable/`.

### Scaffold and run a microservice

```shell
dotnet beam project new service NewService
```

This command generates a `BeamableServices.sln` solution and a `services/NewService/` project containing `NewService.cs`, `Program.cs`, `NewService.csproj`, and a `Dockerfile`. See [`beam project new service`](../commands/cli-command-reference/project/new/service.md) for the available options.

Run the new service through your IDE, with `dotnet run` from the project folder, or with:

```shell
dotnet beam project run
```

You should see a log line ending in `Service ready for traffic` — at that point the service is reachable over HTTP. The [Microservices guide](microservices.md) covers the next steps: opening the local OpenAPI page with `dotnet beam project open-swagger`, calling the generated `Add` endpoint, and adding your own `[ClientCallable]` methods.

## Next steps

From here, you can:

- Setup [Standalone Microservices](microservices.md)
- Manage Content,
- Listen to server events,
- [learn how the CLI handles data output](ms-command-line.md).
