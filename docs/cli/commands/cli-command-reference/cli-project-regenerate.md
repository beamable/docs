---
title: "Project Regenerate"
slug: "cli-project-regenerate"
excerpt: "Regenerate the solution csproj, Dockerfile and Program.cs files"
hidden: false
createdAt: "Fri May 24 2024 19:54:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:31 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project regenerate <name> [<output>] [<copy-path>] [options]
```

## About

Regenerate the solution csproj, Dockerfile and Program.cs files

## Arguments

| Name      | Type        | Description                                   |
| --------- | ----------- | --------------------------------------------- |
| name      | ServiceName | Name of the new project                       |
| output    | String      | Where the temp project will be created        |
| copy-path | String      | The path to where the files will be copied to |

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
    "1-0": "--dryrun",
    "1-1": "Boolean",
    "1-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "2-0": "--cid",
    "2-1": "String",
    "2-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "3-0": "--engine",
    "3-1": "String",
    "3-2": "If passed, sets the engine integration that is calling for the command",
    "4-0": "--engine-sdk-version",
    "4-1": "String",
    "4-2": "The version of the Beamable's SDK running in that Engine",
    "5-0": "--engine-version",
    "5-1": "String",
    "5-2": "The version of the engine that is calling the CLI",
    "6-0": "--pid",
    "6-1": "String",
    "6-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "7-0": "--quiet",
    "7-1": "Boolean",
    "7-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "8-0": "--host",
    "8-1": "String",
    "8-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "9-0": "--access-token",
    "9-1": "String",
    "9-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "10-0": "--refresh-token",
    "10-1": "String",
    "10-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "11-0": "--log",
    "11-1": "String",
    "11-2": "Extra logs gets printed out",
    "12-0": "--no-redirect",
    "12-1": "Boolean",
    "12-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "13-0": "--prefer-remote-federation",
    "13-1": "Boolean",
    "13-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "14-0": "--unmask-logs",
    "14-1": "Boolean",
    "14-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "15-0": "--no-log-file",
    "15-1": "Boolean",
    "15-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "16-0": "--docker-cli-path",
    "16-1": "String",
    "16-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "17-0": "Currently, a docker path has been automatically identified.",
    "18-0": "--emit-log-streams",
    "18-1": "Boolean",
    "18-2": "Out all log messages as data payloads in addition to however they are logged",
    "19-0": "--add-project-path",
    "19-1": "IEnumerable\\`1",
    "19-2": "additional file paths to be included when building a local project manifest.",
    "20-0": "--dir",
    "20-1": "String",
    "20-2": "[DEPRECATED] Path override for the .beamable folder",
    "21-0": "--raw",
    "21-1": "Boolean",
    "21-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "22-0": "--pretty",
    "22-1": "Boolean",
    "22-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "23-0": "--dotnet-path",
    "23-1": "String",
    "23-2": "a custom location for dotnet",
    "24-0": "--version",
    "24-1": "Boolean",
    "24-2": "Show version information",
    "25-0": "--help",
    "25-1": "Boolean",
    "25-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 26,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[project](cli-project.md)
