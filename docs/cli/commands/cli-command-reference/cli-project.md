---
title: "Project"
slug: "cli-project"
excerpt: "Commands that relate to a standalone Beamable project"
hidden: false
createdAt: "Wed Jun 14 2023 17:20:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:07 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project [options]
```

## About

Commands that relate to a standalone Beamable project

## Options

| Name                                                        | Type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --dryrun                                                    | Boolean        | [DEPRECATED] Run as much of the command as possible without making any network calls                                                                                                                                                                                                                                                                                                                                         |
| --cid                                                       | String         | CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'                                                                                                                                                                                                                                                                                                     |
| --engine                                                    | String         | If passed, sets the engine integration that is calling for the command                                                                                                                                                                                                                                                                                                                                                       |
| --engine-sdk-version                                        | String         | The version of the Beamable's SDK running in that Engine                                                                                                                                                                                                                                                                                                                                                                     |
| --engine-version                                            | String         | The version of the engine that is calling the CLI                                                                                                                                                                                                                                                                                                                                                                            |
| --pid                                                       | String         | PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'                                                                                                                                                                                                                                                                                |
| --quiet                                                     | Boolean        | When true, skip input waiting and use default arguments (or error if no defaults are possible)                                                                                                                                                                                                                                                                                                                               |
| --host                                                      | String         | This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'                                                                                                                                                                                                      |
| --access-token                                              | String         | The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY                                                                                                                                                                                                                                                                                           |
| --refresh-token                                             | String         | A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY                                                                                                                                                                                                                                                                                            |
| --log                                                       | String         | Extra logs gets printed out                                                                                                                                                                                                                                                                                                                                                                                                  |
| --no-redirect                                               | Boolean        | If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation. |
| --prefer-remote-federation                                  | Boolean        | By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.                                                                                                                                                                     |
| --unmask-logs                                               | Boolean        | By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.                                                                                                                                                                                                                                                                   |
| --no-log-file                                               | Boolean        | By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.                                                                                                                                                                 |
| --docker-cli-path                                           | String         | a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.                                                                                                                                                                                                                                  |
| Currently, a docker path has been automatically identified. |                |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --emit-log-streams                                          | Boolean        | Out all log messages as data payloads in addition to however they are logged                                                                                                                                                                                                                                                                                                                                                 |
| --add-project-path                                          | IEnumerable\`1 | additional file paths to be included when building a local project manifest.                                                                                                                                                                                                                                                                                                                                                 |
| --dir                                                       | String         | [DEPRECATED] Path override for the .beamable folder                                                                                                                                                                                                                                                                                                                                                                          |
| --raw                                                       | Boolean        | Output raw JSON to standard out. This happens by default when the command is being piped                                                                                                                                                                                                                                                                                                                                     |
| --pretty                                                    | Boolean        | Output syntax highlighted box text. This happens by default when the command is not piped                                                                                                                                                                                                                                                                                                                                    |
| --dotnet-path                                               | String         | a custom location for dotnet                                                                                                                                                                                                                                                                                                                                                                                                 |
| --version                                                   | Boolean        | Show version information                                                                                                                                                                                                                                                                                                                                                                                                     |
| --help                                                      | Boolean        | Show help and usage information                                                                                                                                                                                                                                                                                                                                                                                              |

### Sub Commands

[project-add-paths](cli-project-add-paths.md)  
[project-add-unity-project](cli-project-add-unity-project.md)  
[project-add-unreal-project](cli-project-add-unreal-project.md)  
[project-build](cli-project-build.md)  
[project-dependencies](cli-project-dependencies.md)  
[project-deps](cli-project-deps.md)  
[project-disable](cli-project-disable.md)  
[project-enable](cli-project-enable.md)  
[project-generate](cli-project-generate.md)  
[project-generate-client-oapi](cli-project-generate-client-oapi.md)  
[project-generate-ignore-file](cli-project-generate-ignore-file.md)  
[project-generate-properties](cli-project-generate-properties.md)  
[project-group](cli-project-group.md)  
[project-list](cli-project-list.md)  
[project-logs](cli-project-logs.md)  
[project-new](cli-project-new.md)  
[project-oapi](cli-project-oapi.md)  
[project-open](cli-project-open.md)  
[project-open-mongo](cli-project-open-mongo.md)  
[project-open-swagger](cli-project-open-swagger.md)  
[project-ps](cli-project-ps.md)  
[project-regenerate](cli-project-regenerate.md)  
[project-remove](cli-project-remove.md)  
[project-run](cli-project-run.md)  
[project-share-code](cli-project-share-code.md)  
[project-stop](cli-project-stop.md)  
[project-storage](cli-project-storage.md)  
[project-update-unity-beam-package](cli-project-update-unity-beam-package.md)  
[project-build-sln](cli-project-build-sln.md)  
[project-generate-client](cli-project-generate-client.md)  
[project-generate-env](cli-project-generate-env.md)  
[project-read-settings](cli-project-read-settings.md)  
[project-remote-logs](cli-project-remote-logs.md)  
[project-remote-manifest](cli-project-remote-manifest.md)  
[project-write-setting](cli-project-write-setting.md)
