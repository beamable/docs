---
title: "Server Serve"
slug: "cli-server-serve"
excerpt: "[INTERNAL] Create a local server for the cli"
hidden: true
createdAt: "Fri May 24 2024 19:54:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 14 2025 19:06:20 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam server serve [<owner>] [options]
```

## About

[INTERNAL] Create a local server for the cli

## Arguments

| Name  | Type   | Description                                                                          |
| ----- | ------ | ------------------------------------------------------------------------------------ |
| owner | String | The owner of the server is used to identify the server later with the /info endpoint |

## Options

| Name                    | Type    | Description                                                                                                                           |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| --port                  | Int32   | The port the local server will bind to                                                                                                |
| --auto-inc-port         | Boolean | When true, if the given --port is not available, it will be incremented until an available port is discovered                         |
| --self-destruct-seconds | Int32   | The number of seconds the server will stay alive without receiving any traffic. A value of zero means there is no self destruct timer |
| --require-process-id    | Int32   | Listens to the given process id. Terminates this long-running command when the it no longer is running                                |
| --custom-splitter       | Boolean | When true, will use custom logic to split the command line given to the server via HTTP request.                                      |

The default splitter (from Microsoft) does NOT allow you to pass in JSON blobs as arguments.  
The custom splitter does its best to support all our commands correctly and accept json blobs as arguments|  
|--skip-content-prewarm|Boolean|When true, will NOT pre-warm the content service with the latest content manifest|  
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
|--docker-cli-path|String|a custom location for docker. By default, the CLI will attempt to resolve docker through its usual install locations. You can also use the BEAM_DOCKER_EXE environment variable to specify.  
Currently, a docker path has been automatically identified.|  
|--emit-log-streams|Boolean|Out all log messages as data payloads in addition to however they are logged|  
|--add-project-path|IEnumerable\`1|additional file paths to be included when building a local project manifest. |  
|--dir|String|[DEPRECATED] Path override for the .beamable folder|  
|--raw|Boolean|Output raw JSON to standard out. This happens by default when the command is being piped|  
|--pretty|Boolean|Output syntax highlighted box text. This happens by default when the command is not piped|  
|--dotnet-path|String|a custom location for dotnet|  
|--version|Boolean|Show version information|  
|--help|Boolean|Show help and usage information|

### Parent Command

[server](cli-server.md)
