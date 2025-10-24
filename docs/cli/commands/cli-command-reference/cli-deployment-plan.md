---
title: "Deployment Plan"
slug: "cli-deployment-plan"
excerpt: "Plan a deployment for later release"
hidden: false
createdAt: "Wed Dec 04 2024 11:27:32 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:28 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam deployment plan [options]
```

## About

Plan a deployment for later release

## Options

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "--comment",
    "0-1": "String",
    "0-2": "Associates this comment along with the published Manifest. You'll be able to read it via the Beamable Portal",
    "1-0": "--service-comments",
    "1-1": "String\\[]",
    "1-2": "Any number of strings in the format BeamoId::Comment",
    "2-0": "Associates each comment to the given Beamo Id if it's among the published services. You'll be able to read it via the Beamable Portal",
    "3-0": "--from-manifest",
    "3-1": "String",
    "3-2": "A manifest json file to use to create a plan",
    "4-0": "--from-manifest-id",
    "4-1": "String",
    "4-2": "A manifest id to download and use to create a plan",
    "5-0": "--run-health-checks",
    "5-1": "Boolean",
    "5-2": "Run health checks on services",
    "6-0": "--redeploy",
    "6-1": "Boolean",
    "6-2": "Restart existing deployed services",
    "7-0": "--build-sequentially",
    "7-1": "Boolean",
    "7-2": "Build services sequentially instead of all together",
    "8-0": "--merge",
    "8-1": "Boolean",
    "8-2": "Create a Release that merges your current local environment to the existing remote services. Existing deployed services will not be removed",
    "9-0": "--replace",
    "9-1": "Boolean",
    "9-2": "Create a Release that completely overrides the existing remote services. Existing deployed services that are not present locally will be removed (default)",
    "10-0": "--docker-compose-dir",
    "10-1": "String",
    "10-2": "Specify an output path where a new docker-compose project will be created. The compose file can be used to run services locally. (Note, existing files in this folder will be overwritten)",
    "11-0": "--sln",
    "11-1": "String",
    "11-2": "Relative path to the .sln file to use for the new project. If the .sln file does not exist, it will be created. When no option is configured, if this command is executing inside a .beamable folder, then the first .sln found in .beamable/.. will be used. If no .sln is found, the .sln path will be <name>.sln. If no .beamable folder exists, then the <project>/<project>.sln will be used",
    "12-0": "--to-file",
    "12-1": "String",
    "12-2": "A file path to save the plan",
    "13-0": "--dryrun",
    "13-1": "Boolean",
    "13-2": "[DEPRECATED] Run as much of the command as possible without making any network calls",
    "14-0": "--cid",
    "14-1": "String",
    "14-2": "CID (CustomerId) to use (found in Portal->Account); defaults to whatever is in '.beamable/connection-configuration.json'",
    "15-0": "--engine",
    "15-1": "String",
    "15-2": "If passed, sets the engine integration that is calling for the command",
    "16-0": "--engine-sdk-version",
    "16-1": "String",
    "16-2": "The version of the Beamable's SDK running in that Engine",
    "17-0": "--engine-version",
    "17-1": "String",
    "17-2": "The version of the engine that is calling the CLI",
    "18-0": "--pid",
    "18-1": "String",
    "18-2": "PID (Realm ID) to use (found in Portal -> Games -> Any Realm's details); defaults to whatever is in '.beamable/connection-configuration.json'",
    "19-0": "--quiet",
    "19-1": "Boolean",
    "19-2": "When true, skip input waiting and use default arguments (or error if no defaults are possible)",
    "20-0": "--host",
    "20-1": "String",
    "20-2": "This option defines the target Beamable environment. Needed for private cloud customers to target their exclusive Beamable environment. Ignorable by everyone else. Stored in '.beamable/connection-configuration.json'",
    "21-0": "--access-token",
    "21-1": "String",
    "21-2": "The access token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "22-0": "--refresh-token",
    "22-1": "String",
    "22-2": "A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY",
    "23-0": "--log",
    "23-1": "String",
    "23-2": "Extra logs gets printed out",
    "24-0": "--no-redirect",
    "24-1": "Boolean",
    "24-2": "If there is a local dotnet tool installation (with a ./config/dotnet-tools.json file) for the beam tool, then any global invocation of the beam tool will automatically redirect and call the local version. However, there will be a performance penalty due to the extra process invocation. This option flag will cause an error to occur instead of automatically redirecting the execution to a new process invocation.",
    "25-0": "--prefer-remote-federation",
    "25-1": "Boolean",
    "25-2": "By default, any local CLI invocation that should trigger a Federation of any type will prefer locally running Microservices. However, if you need the CLI to use the remotely running Microservices, use this option to ignore locally running services.",
    "26-0": "--unmask-logs",
    "26-1": "Boolean",
    "26-2": "By default, logs will automatically mask tokens. However, when this option is enabled, tokens will be visible in their full text. This is a security risk.",
    "27-0": "--no-log-file",
    "27-1": "Boolean",
    "27-2": "By default, logs are automatically written to a temp file so that they can be used in an error case. However, when this option is enabled, logs are not written. Also, if the BEAM_CLI_NO_FILE_LOG environment variable is set, no log file will be written.",
    "28-0": "--docker-cli-path",
    "28-1": "String",
    "28-2": "a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.",
    "29-0": "Currently, a docker path has been automatically identified.",
    "30-0": "--emit-log-streams",
    "30-1": "Boolean",
    "30-2": "Out all log messages as data payloads in addition to however they are logged",
    "31-0": "--add-project-path",
    "31-1": "IEnumerable\\`1",
    "31-2": "additional file paths to be included when building a local project manifest.",
    "32-0": "--dir",
    "32-1": "String",
    "32-2": "[DEPRECATED] Path override for the .beamable folder",
    "33-0": "--raw",
    "33-1": "Boolean",
    "33-2": "Output raw JSON to standard out. This happens by default when the command is being piped",
    "34-0": "--pretty",
    "34-1": "Boolean",
    "34-2": "Output syntax highlighted box text. This happens by default when the command is not piped",
    "35-0": "--dotnet-path",
    "35-1": "String",
    "35-2": "a custom location for dotnet",
    "36-0": "--version",
    "36-1": "Boolean",
    "36-2": "Show version information",
    "37-0": "--help",
    "37-1": "Boolean",
    "37-2": "Show help and usage information"
  },
  "cols": 3,
  "rows": 38,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Parent Command

[deployment](cli-deployment.md)
