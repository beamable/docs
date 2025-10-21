---
title: "Project Remote-logs"
slug: "cli-project-remote-logs"
excerpt: "[INTERNAL] get remote logs for a service"
hidden: true
createdAt: "Thu Feb 13 2025 20:04:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:30 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project remote-logs <service-id> [options]
```

## About

[INTERNAL] get remote logs for a service

## Arguments

| Name       | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| service-id | String | The beamo id for the service to get logs for |

## Options

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "--filter",
    "0-1": "String",
    "0-2": "A text filter for log searching",
    "1-0": "--server-log-level",
    "1-1": "String",
    "1-2": "A log level filter for searching",
    "2-0": "--from",
    "2-1": "String",
    "2-2": "A timestamp filter, where logs must be newer than this time. Must be an exact date time string, or a relative time string. Relative time strings are in the format <number><unit>. The unit is either s (seconds), m (minutes), h (hours), or d (days). To represent 5 minutes in the past, use the term '5m'",
    "3-0": "--to",
    "3-1": "String",
    "3-2": "A timestamp filter, where logs must be older than this time. Must be an exact date time string, or a relative time string. Relative time strings are in the format <number><unit>. The unit is either s (seconds), m (minutes), h (hours), or d (days). To represent 5 minutes in the past, use the term '5m'",
    "4-0": "--dryrun",
    "4-1": "Boolean",
    "4-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "5-0": "--cid",
    "5-1": "String",
    "5-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "6-0": "--engine",
    "6-1": "String",
    "6-2": "If passed, sets the engine integration that is calling for the command",
    "7-0": "--engine-sdk-version",
    "7-1": "String",
    "7-2": "The version of the Beamable's SDK running in that Engine",
    "8-0": "--engine-version",
    "8-1": "String",
    "8-2": "The version of the engine that is calling the CLI",
    "9-0": "--pid",
    "9-1": "String",
    "9-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "10-0": "--quiet",
    "10-1": "Boolean",
    "10-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "11-0": "--host",
    "11-1": "String",
    "11-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "12-0": "--access-token",
    "12-1": "String",
    "12-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "13-0": "--refresh-token",
    "13-1": "String",
    "13-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "14-0": "--log",
    "14-1": "String",
    "14-2": "Extra logs gets printed out",
    "15-0": "--no-redirect",
    "15-1": "Boolean",
    "15-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "16-0": "--prefer-remote-federation",
    "16-1": "Boolean",
    "16-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "17-0": "--unmask-logs",
    "17-1": "Boolean",
    "17-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "18-0": "--no-log-file",
    "18-1": "Boolean",
    "18-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "19-0": "--docker-cli-path",
    "19-1": "String",
    "19-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "20-0": "Currently, a docker path has been automatically identified.",
    "21-0": "--emit-log-streams",
    "21-1": "Boolean",
    "21-2": "Out all log messages as data payloads in addition to however they are logged",
    "22-0": "--add-project-path",
    "22-1": "IEnumerable\\`1",
    "22-2": "additional file paths to be included when building a local project manifest.",
    "23-0": "--dir",
    "23-1": "String",
    "23-2": "[DEPRECATED] Path override for the .beamable folder",
    "24-0": "--raw",
    "24-1": "Boolean",
    "24-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "25-0": "--pretty",
    "25-1": "Boolean",
    "25-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "26-0": "--dotnet-path",
    "26-1": "String",
    "26-2": "a custom location for dotnet",
    "27-0": "--version",
    "27-1": "Boolean",
    "27-2": "Show version information",
    "28-0": "--help",
    "28-1": "Boolean",
    "28-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 29,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[project](cli-project.md)
