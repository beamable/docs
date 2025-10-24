---
title: "Project New Service"
slug: "cli-project-new-service"
excerpt: "Create a new microservice project"
hidden: false
createdAt: "Fri May 24 2024 19:54:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:19 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project new service <name> [options]
```

## About

Create a new microservice project

## Arguments

| Name | Type        | Description             |
| ---- | ----------- | ----------------------- |
| name | ServiceName | Name of the new project |

## Options

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "--sln",
    "0-1": "String",
    "0-2": "Relative path to the .sln file to use for the new project. If the .sln file does not exist, it will be created. When no option is configured, if this command is executing inside a .beamable folder, then the first .sln found in .beamable/.. will be used. If no .sln is found, the .sln path will be <name>.sln. If no .beamable folder exists, then the <project>/<project>.sln will be used",
    "1-0": "--service-directory",
    "1-1": "String",
    "1-2": "Relative path to directory where project should be created. Defaults to \"SOLUTION_DIR/services\"",
    "2-0": "--link-to",
    "2-1": "List\\`1",
    "2-2": "The name of the storage to link this service to",
    "3-0": "--groups",
    "3-1": "List\\`1",
    "3-2": "Specify BeamableGroups for this service",
    "4-0": "--generate-common",
    "4-1": "Boolean",
    "4-2": "If passed, will create a common library for this project",
    "5-0": "--dryrun",
    "5-1": "Boolean",
    "5-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "6-0": "--cid",
    "6-1": "String",
    "6-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "7-0": "--engine",
    "7-1": "String",
    "7-2": "If passed, sets the engine integration that is calling for the command",
    "8-0": "--engine-sdk-version",
    "8-1": "String",
    "8-2": "The version of the Beamable's SDK running in that Engine",
    "9-0": "--engine-version",
    "9-1": "String",
    "9-2": "The version of the engine that is calling the CLI",
    "10-0": "--pid",
    "10-1": "String",
    "10-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "11-0": "--quiet",
    "11-1": "Boolean",
    "11-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "12-0": "--host",
    "12-1": "String",
    "12-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "13-0": "--access-token",
    "13-1": "String",
    "13-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "14-0": "--refresh-token",
    "14-1": "String",
    "14-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "15-0": "--log",
    "15-1": "String",
    "15-2": "Extra logs gets printed out",
    "16-0": "--no-redirect",
    "16-1": "Boolean",
    "16-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "17-0": "--prefer-remote-federation",
    "17-1": "Boolean",
    "17-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "18-0": "--unmask-logs",
    "18-1": "Boolean",
    "18-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "19-0": "--no-log-file",
    "19-1": "Boolean",
    "19-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "20-0": "--docker-cli-path",
    "20-1": "String",
    "20-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "21-0": "Currently, a docker path has been automatically identified.",
    "22-0": "--emit-log-streams",
    "22-1": "Boolean",
    "22-2": "Out all log messages as data payloads in addition to however they are logged",
    "23-0": "--add-project-path",
    "23-1": "IEnumerable\\`1",
    "23-2": "additional file paths to be included when building a local project manifest.",
    "24-0": "--dir",
    "24-1": "String",
    "24-2": "[DEPRECATED] Path override for the .beamable folder",
    "25-0": "--raw",
    "25-1": "Boolean",
    "25-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "26-0": "--pretty",
    "26-1": "Boolean",
    "26-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "27-0": "--dotnet-path",
    "27-1": "String",
    "27-2": "a custom location for dotnet",
    "28-0": "--version",
    "28-1": "Boolean",
    "28-2": "Show version information",
    "29-0": "--help",
    "29-1": "Boolean",
    "29-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 30,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[project-new](cli-project-new.md)
