

```shell
beam login [options]
```

## About
The login command will perform a login action and acquire Beamable authorization tokens. There are two main ways Beamable handles authorization, access tokens, and JWTs. JWTs are still being developed. Access tokens are the primary way to handle authorization. Any API request sent to Beamable needs an `Authorization` header with a bearer token using the Beamable _access token_. These tokens are short lived and will need to be refreshed periodically. The login command also issues a _refresh token_ which can be used to fetch a new _access token_ if the need arises. 

By default, the login command will not _save_ your access tokens. You should pass the `--save-to-file` option to commit the _access token_ and _refresh token_ to your `./beamable` folder.



## Options

|Name|Type|Description|
|-|-|-|
|--email|String|Specify user email address|
|--password|String|User password|
|--save-to-environment|Boolean|Save login refresh token to environment variable|
|--no-token-save|Boolean|Prevent auth tokens from being saved to disk. This replaces the legacy --save-to-file option|
|--realm-scoped|Boolean|Makes the resulting access/refresh token pair be realm scoped instead of the default customer scoped one|
|--refresh-token|String|A Refresh Token to use for the requests. It overwrites the logged in user stored in connection-auth.json for THIS INVOCATION ONLY|
|--print-to-console|Boolean|Prints out login request response to console|
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






