---
title: "Project Remove"
slug: "cli-project-remove"
excerpt: "Removes the local source code for a service or storage"
hidden: false
createdAt: "Wed Dec 04 2024 11:27:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:13 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project remove [options]
```

## About

Removes the local source code for a service or storage

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
    "2-0": "--ids",
    "2-1": "List\\`1",
    "2-2": "The list of services to include, defaults to all local services (separated by whitespace). To use NO services, use the --exact-ids flag",
    "3-0": "--exact-ids",
    "3-1": "Boolean",
    "3-2": "By default, a blank --ids option maps to ALL available ids. When the --exact-ids flag is given, a blank --ids option maps to NO ids",
    "4-0": "--without-group",
    "4-1": "List\\`1",
    "4-2": "A set of BeamServiceGroup tags that will exclude the associated services. Exclusion takes precedence over inclusion",
    "5-0": "--with-group",
    "5-1": "List\\`1",
    "5-2": "A set of BeamServiceGroup tags that will include the associated services",
    "6-0": "--dryrun",
    "6-1": "Boolean",
    "6-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "7-0": "--cid",
    "7-1": "String",
    "7-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "8-0": "--engine",
    "8-1": "String",
    "8-2": "If passed, sets the engine integration that is calling for the command",
    "9-0": "--engine-sdk-version",
    "9-1": "String",
    "9-2": "The version of the Beamable's SDK running in that Engine",
    "10-0": "--engine-version",
    "10-1": "String",
    "10-2": "The version of the engine that is calling the CLI",
    "11-0": "--pid",
    "11-1": "String",
    "11-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "12-0": "--quiet",
    "12-1": "Boolean",
    "12-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "13-0": "--host",
    "13-1": "String",
    "13-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "14-0": "--access-token",
    "14-1": "String",
    "14-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "15-0": "--refresh-token",
    "15-1": "String",
    "15-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "16-0": "--log",
    "16-1": "String",
    "16-2": "Extra logs gets printed out",
    "17-0": "--no-redirect",
    "17-1": "Boolean",
    "17-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "18-0": "--prefer-remote-federation",
    "18-1": "Boolean",
    "18-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "19-0": "--unmask-logs",
    "19-1": "Boolean",
    "19-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "20-0": "--no-log-file",
    "20-1": "Boolean",
    "20-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "21-0": "--docker-cli-path",
    "21-1": "String",
    "21-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "22-0": "Currently, a docker path has been automatically identified.",
    "23-0": "--emit-log-streams",
    "23-1": "Boolean",
    "23-2": "Out all log messages as data payloads in addition to however they are logged",
    "24-0": "--add-project-path",
    "24-1": "IEnumerable\\`1",
    "24-2": "additional file paths to be included when building a local project manifest.",
    "25-0": "--dir",
    "25-1": "String",
    "25-2": "[DEPRECATED] Path override for the .beamable folder",
    "26-0": "--raw",
    "26-1": "Boolean",
    "26-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "27-0": "--pretty",
    "27-1": "Boolean",
    "27-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "28-0": "--dotnet-path",
    "28-1": "String",
    "28-2": "a custom location for dotnet",
    "29-0": "--version",
    "29-1": "Boolean",
    "29-2": "Show version information",
    "30-0": "--help",
    "30-1": "Boolean",
    "30-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 31,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[project](cli-project.md)
