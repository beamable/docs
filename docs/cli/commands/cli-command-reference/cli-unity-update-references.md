---
title: "Unity Update-references"
slug: "cli-unity-update-references"
excerpt: "[INTERNAL] Updates all Unity Assembly Definition references of the specified service"
hidden: true
createdAt: "Wed Dec 04 2024 11:27:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:38 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam unity update-references <service> [options]
```

## About

[INTERNAL] Updates all Unity Assembly Definition references of the specified service

## Arguments

| Name    | Type   | Description                                      |
| ------- | ------ | ------------------------------------------------ |
| service | String | The name of the service to update the references |

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
    "1-0": "--paths",
    "1-1": "List\\`1",
    "1-2": "The path of the project that will be referenced",
    "2-0": "--names",
    "2-1": "List\\`1",
    "2-2": "The name of the Assembly Definition",
    "3-0": "--dryrun",
    "3-1": "Boolean",
    "3-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "4-0": "--cid",
    "4-1": "String",
    "4-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "5-0": "--engine",
    "5-1": "String",
    "5-2": "If passed, sets the engine integration that is calling for the command",
    "6-0": "--engine-sdk-version",
    "6-1": "String",
    "6-2": "The version of the Beamable's SDK running in that Engine",
    "7-0": "--engine-version",
    "7-1": "String",
    "7-2": "The version of the engine that is calling the CLI",
    "8-0": "--pid",
    "8-1": "String",
    "8-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "9-0": "--quiet",
    "9-1": "Boolean",
    "9-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "10-0": "--host",
    "10-1": "String",
    "10-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "11-0": "--access-token",
    "11-1": "String",
    "11-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "12-0": "--refresh-token",
    "12-1": "String",
    "12-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "13-0": "--log",
    "13-1": "String",
    "13-2": "Extra logs gets printed out",
    "14-0": "--no-redirect",
    "14-1": "Boolean",
    "14-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "15-0": "--prefer-remote-federation",
    "15-1": "Boolean",
    "15-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "16-0": "--unmask-logs",
    "16-1": "Boolean",
    "16-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "17-0": "--no-log-file",
    "17-1": "Boolean",
    "17-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "18-0": "--docker-cli-path",
    "18-1": "String",
    "18-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "19-0": "Currently, a docker path has been automatically identified.",
    "20-0": "--emit-log-streams",
    "20-1": "Boolean",
    "20-2": "Out all log messages as data payloads in addition to however they are logged",
    "21-0": "--add-project-path",
    "21-1": "IEnumerable\\`1",
    "21-2": "additional file paths to be included when building a local project manifest.",
    "22-0": "--dir",
    "22-1": "String",
    "22-2": "[DEPRECATED] Path override for the .beamable folder",
    "23-0": "--raw",
    "23-1": "Boolean",
    "23-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "24-0": "--pretty",
    "24-1": "Boolean",
    "24-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "25-0": "--dotnet-path",
    "25-1": "String",
    "25-2": "a custom location for dotnet",
    "26-0": "--version",
    "26-1": "Boolean",
    "26-2": "Show version information",
    "27-0": "--help",
    "27-1": "Boolean",
    "27-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 28,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[unity](cli-unity.md)
