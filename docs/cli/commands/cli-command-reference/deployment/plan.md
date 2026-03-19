```shell
beam deployment plan [options]
```

## About
Plan a deployment for later release

When planning a deployment, the CLI builds Docker images for your services and prepares them for deployment. This process fixes a critical deployment failure scenario where users previously couldn't use non-Alpine base images at all. The build process now automatically configures the appropriate Docker base image based on your service configuration, making Docker overrides work as originally intended.

## Docker base image configuration

During the deployment planning process, the CLI constructs Docker images using base image tags determined by your service's MSBuild properties. This change fixes the previous behavior where the CLI hardcoded Alpine base images regardless of user configuration, causing deployment failures when services required non-Alpine environments.

### Why users care about this change

Previously, the CLI always passed `--build-arg BEAM_DOTNET_VERSION=X.0-alpine` to `docker buildx build`, completely overriding any `ARG BEAM_DOTNET_VERSION` declarations in your Dockerfile. This made it impossible to use Ubuntu-based images or other variants, causing deployment failures when services required packages or tools not available in Alpine Linux.

Error examples that previously occurred even when users tried to override the Dockerfile:
```
/bin/sh: apt-get: not found
Unable to locate package build-essential  
rustc: command not found
node: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.XX' not found
```

These errors happened because Alpine uses different package managers (`apk` instead of `apt-get`) and a different C library (musl instead of glibc). The CLI change now makes Dockerfile overrides work as intended.

### ContainerFamily property

The `ContainerFamily` MSBuild property in your service's `.csproj` file controls which Docker base image variant to use:

- **`alpine`** (default): Uses Alpine Linux base images (smaller, security-focused)
- **`noble`**: Uses Ubuntu Noble base images (more packages available, better for complex dependencies)

To configure the container family, add this property to your service's `.csproj` file:

```xml
<PropertyGroup>
  <TargetFramework>net8.0</TargetFramework>
  <ContainerFamily>noble</ContainerFamily>
</PropertyGroup>
```

### When to use noble instead of alpine

Choose the `noble` container family when your service needs:

- **System packages not available in Alpine**: Many development tools and libraries are only packaged for Ubuntu/Debian
- **glibc compatibility**: Some applications require glibc instead of Alpine's musl libc
- **Complex build dependencies**: Ubuntu's extensive package ecosystem makes it easier to install build tools like Rust, specific compilers, or native libraries
- **Third-party tools during container build**: Tools that expect standard Linux distributions

**Example scenario**: A service that installs Rust during the Docker build would fail with Alpine because `apt-get` commands don't work. The error would look like:
```
/bin/sh: apt-get: not found
```

Switching to `noble` resolves this because Ubuntu Noble provides the `apt-get` package manager.

### Base image tag construction

The CLI automatically constructs the `BEAM_DOTNET_VERSION` Docker build argument by combining:

1. The .NET version extracted from your `TargetFramework` property
2. The `ContainerFamily` value (defaulting to `alpine` if unspecified)

Examples:
- `net8.0` + `alpine` → `8.0-alpine`
- `net10.0` + `noble` → `10.0-noble`
- `net8.0` + (unspecified) → `8.0-alpine`

The version extraction works generically from the Target Framework Moniker (`net10.0` → `10.0`), making it forward-compatible with future .NET versions without requiring hardcoded version lists.

This ensures your Dockerfile receives the correct base image tag via the `BEAM_DOTNET_VERSION` build argument, allowing you to write Dockerfiles that use non-Alpine base images when needed.

### Compatibility with existing setups

**Previous BEAM_DOTNET_VERSION overrides**: If you were previously overriding `BEAM_DOTNET_VERSION` in your Dockerfile, this change now makes that override work as originally intended. Before, the CLI would always pass `--build-arg BEAM_DOTNET_VERSION=X.0-alpine` regardless of your Dockerfile's default value, overriding your customization. Now, the CLI respects your `ContainerFamily` setting and constructs the appropriate tag.

**Migration requirements**: When switching container families:

- **No automatic redeployment**: Services deployed with alpine will continue running alpine until you redeploy them
- **Explicit redeployment needed**: Run `beam deployment plan` followed by `beam deployment release` to deploy with the new base image
- **Dockerfile compatibility**: Your existing Dockerfiles work without modification—the CLI handles base image selection automatically

### Performance and resource implications

| Aspect | Alpine | Noble |
|--------|--------|--------|
| **Image size** | ~80MB smaller | ~240MB larger |
| **Build time** | Faster (fewer layers) | Slower (more system packages) |
| **Security** | Smaller attack surface | Larger attack surface |
| **Package availability** | Limited Alpine packages | Full Ubuntu package ecosystem |
| **glibc compatibility** | Uses musl (compatibility issues) | Standard glibc (broad compatibility) |
| **Development tools** | Minimal, requires apk add | Rich development environment |
| **Resource usage in Beamable Cloud** | Lower memory footprint | Higher memory footprint |
| **Deployment times** | Faster image pulls | Slower image pulls due to size |

The 240MB size difference affects deployment times in the Beamable Cloud environment. Larger images take longer to pull and start, but the impact varies based on your realm's region and current load. Choose Alpine for production services with minimal dependencies. Choose Noble for services requiring extensive build tools, third-party packages, or glibc compatibility.

### Validation behavior

The CLI validates `ContainerFamily` values against supported options (`alpine`, `noble`). If you specify an invalid value:

- **No error is shown**: The CLI silently falls back to `alpine` as the default
- **Build continues normally**: Your deployment will proceed using Alpine Linux base images
- **Log indication**: Check build logs for the actual `BEAM_DOTNET_VERSION` build argument passed to Docker

Users should get a warning about this fallback behavior, but currently the CLI handles validation silently. To verify your container family selection is working, examine the Docker build output for lines like:
```
--build-arg BEAM_DOTNET_VERSION=8.0-noble
```

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