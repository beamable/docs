```shell
beam deployment plan [options]
```

## About
Plan a deployment for later release

## Container base image configuration

The CLI automatically determines the Docker base image tag for your microservices by reading MSBuild properties from each service's `.csproj` file during the build phase of deployment:

- **`TargetFramework`**: Extracts the .NET version (e.g., `net8.0` becomes `8.0`)
- **`ContainerFamily`**: Specifies the base image family (defaults to `alpine`)

### Why this matters

Services requiring Ubuntu-specific packages (like `apt-get install git`, `curl`, or system libraries available through `apt`) would fail during deployment when using Alpine Linux base images. Alpine uses `apk` as its package manager and has a different filesystem structure. This configuration resolves compatibility issues by allowing services to use Ubuntu Noble base images that support standard Ubuntu packages and tooling.

### Supported container families

| Family | Description | Package manager | Use case |
|--------|-------------|----------------|----------|
| `alpine` | Alpine Linux-based images (default) | `apk` | Smaller image size, minimal footprint |
| `noble` | Ubuntu Noble-based images | `apt-get` | Ubuntu packages, broader compatibility, system libraries |

### Configuration

Add to your service's `.csproj`:

```xml
<PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <ContainerFamily>noble</ContainerFamily>
</PropertyGroup>
```

This generates the Docker build argument `--build-arg BEAM_DOTNET_VERSION=8.0-noble`, using the base image `mcr.microsoft.com/dotnet/runtime:8.0-noble`.

### Deployment failure scenarios

Without setting `ContainerFamily` to `noble`, services that use Ubuntu packages will fail during the Docker build phase with errors like:

```
/bin/sh: apt-get: not found
```

This occurs because Alpine Linux doesn't include `apt-get` - it uses `apk` instead. The deployment will stop at the Docker build step and never reach the running container phase.

### Migration from hardcoded base images

Before this fix, users had to work around the CLI's hardcoded Alpine tag behavior by manually editing their Dockerfiles to specify exact base images (e.g., `FROM mcr.microsoft.com/dotnet/runtime:8.0-noble`). This prevented the CLI from automatically managing .NET version updates and created maintenance overhead.

If you previously worked around this limitation:

1. Set `<ContainerFamily>noble</ContainerFamily>` in your `.csproj`
2. Change your Dockerfile back to `FROM mcr.microsoft.com/dotnet/runtime:${BEAM_DOTNET_VERSION}`
3. The CLI will automatically pass the correct tag during deployment

### Performance and security considerations

- **Image size**: Alpine images are typically 5-10MB smaller than Ubuntu Noble images
- **Security**: Alpine has a smaller attack surface due to fewer installed packages by default
- **Compatibility**: Noble provides broader package availability and compatibility with Ubuntu-based tooling
- **Build time**: Noble images may have slightly longer pull times due to larger base size

Choose `alpine` for minimal production services with no special dependencies, and `noble` when you need Ubuntu packages or broader system library support.

### Impact on existing services

- **Existing deployed services**: No change. They continue running with their current base images.
- **New deployments**: Only services that explicitly set `ContainerFamily` will use different base images.
- **Default behavior**: Unchanged. Services without `ContainerFamily` still use Alpine images.

## Options

|Name|Type|Description|
|-|-|-|
|--comment|String|Associates this comment along with the published Manifest. You'll be able to read it via the Beamable Portal|
|--service-comments|String[]|Any number of strings in the format BeamoId::Comment<br>Associates each comment to the given Beamo Id if it's among the published services. You'll be able to read it via the Beamable Portal|
|--from-manifest|String|A manifest json file to use to create a plan|
|--from-manifest-id|String|A manifest id to download and use to create a plan|
|--run-health-checks|Boolean|Run health checks on services|
|--redeploy|Boolean|Restart existing deployed services|
|--build-sequentially|Boolean|Build services sequentially instead of all together|
|--merge|Boolean|Create a Release that merges your current local environment to the existing remote services. Existing deployed services will not be removed|
|--replace|Boolean|Create a Release that completely overrides the existing remote services. Existing deployed services that are not present locally will be removed (default)|
|--docker-compose-dir|String|Specify an output path where a new docker-compose project will be created. The compose file can be used to run services locally. (Note, existing files in this folder will be overwritten)|
|--sln|String|Relative path to the .sln file to use for the new project. If the .sln file does not exist, it will be created. When no option is configured, if this command is executing inside a .beamable folder, then the first .sln found in .beamable/.. will be used. If no .sln is found, the .sln path will be <name>.sln. If no .beamable folder exists, then the <project>/<project>.sln will be used|
|--to-file|String|A file path to save the plan|
|--dryrun|Boolean|[DEPRECATED] Run as much of the command as possible without making any network calls|
|--cid|String|CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'|
|--engine|String|If passed, sets the engine integration that is calling for the command|
|--engine-sdk-version|String|The version of the Beamable's SDK running in that Engine|
|--engine-version|String|The version of the engine that is calling the CLI|
|--pid|String|PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'|
|--quiet|Boolean|When true, skip input waiting and use default arguments (or error if no defaults are possible)|
|--host|String|This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'|
|--access-token|String|The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY|
|--refresh-token|String|A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY|
|--log|String|Extra logs gets printed out|
|--no-redirect|Boolean|If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation. |
|--prefer-remote-federation|Boolean|By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services. |
|--unmask-logs|Boolean|By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.|
|--no-log-file|Boolean|By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written. |
|--docker-cli-path|String|a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify. <br>Currently, a docker path has been automatically identified.|
|--emit-log-streams|Boolean|Out all log messages as data payloads in addition to however they are logged|
|--add-project-path|Set[String]|additional file paths to be included when building a local project manifest. |
|--dir|String|[DEPRECATED] Path override for the .beamable folder|
|--raw|Boolean|Output raw JSON to standard out. This happens by default when the command is being piped|
|--pretty|Boolean|Output syntax highlighted box text. This happens by default when the command is not piped|
|--dotnet-path|String|a custom location for dotnet|
|--version|Boolean|Show version information|
|--help|Boolean|Show help and usage information|



### Parent Command
[deployment](./deployment.md)