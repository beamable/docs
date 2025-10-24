---
title: "Project New Common-lib"
slug: "cli-project-new-common-lib"
excerpt: "Create common library project that later can be connected to the services"
hidden: false
createdAt: "Fri May 24 2024 19:54:23 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:28 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project new common-lib <name> [options]
```

## About

Create common library project that later can be connected to the services

## Arguments

| Name | Type        | Description                         |
| ---- | ----------- | ----------------------------------- |
| name | ServiceName | The name of the new library project |

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
    "1-0": "--output-path",
    "1-1": "String",
    "1-2": "The path where the project is going to be created",
    "2-0": "--dryrun",
    "2-1": "Boolean",
    "2-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "3-0": "--cid",
    "3-1": "String",
    "3-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "4-0": "--engine",
    "4-1": "String",
    "4-2": "If passed, sets the engine integration that is calling for the command",
    "5-0": "--engine-sdk-version",
    "5-1": "String",
    "5-2": "The version of the Beamable's SDK running in that Engine",
    "6-0": "--engine-version",
    "6-1": "String",
    "6-2": "The version of the engine that is calling the CLI",
    "7-0": "--pid",
    "7-1": "String",
    "7-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "8-0": "--quiet",
    "8-1": "Boolean",
    "8-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "9-0": "--host",
    "9-1": "String",
    "9-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "10-0": "--access-token",
    "10-1": "String",
    "10-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "11-0": "--refresh-token",
    "11-1": "String",
    "11-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "12-0": "--log",
    "12-1": "String",
    "12-2": "Extra logs gets printed out",
    "13-0": "--no-redirect",
    "13-1": "Boolean",
    "13-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "14-0": "--prefer-remote-federation",
    "14-1": "Boolean",
    "14-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "15-0": "--unmask-logs",
    "15-1": "Boolean",
    "15-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "16-0": "--no-log-file",
    "16-1": "Boolean",
    "16-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "17-0": "--docker-cli-path",
    "17-1": "String",
    "17-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "18-0": "Currently, a docker path has been automatically identified.",
    "19-0": "--emit-log-streams",
    "19-1": "Boolean",
    "19-2": "Out all log messages as data payloads in addition to however they are logged",
    "20-0": "--add-project-path",
    "20-1": "IEnumerable\\`1",
    "20-2": "additional file paths to be included when building a local project manifest.",
    "21-0": "--dir",
    "21-1": "String",
    "21-2": "[DEPRECATED] Path override for the .beamable folder",
    "22-0": "--raw",
    "22-1": "Boolean",
    "22-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "23-0": "--pretty",
    "23-1": "Boolean",
    "23-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "24-0": "--dotnet-path",
    "24-1": "String",
    "24-2": "a custom location for dotnet",
    "25-0": "--version",
    "25-1": "Boolean",
    "25-2": "Show version information",
    "26-0": "--help",
    "26-1": "Boolean",
    "26-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 27,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[project-new](cli-project-new.md)
