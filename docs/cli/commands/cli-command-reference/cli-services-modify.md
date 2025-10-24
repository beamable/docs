---
title: "Services Modify"
slug: "cli-services-modify"
excerpt: "Modifies a new service into the local manifest"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jun 14 2023 17:20:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 25 2023 20:56:56 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam services modify [options]
```

## About

Modifies a new service into the local manifest

## Options

| Name                                         | Type        | Description                                                                                                                        |
| -------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| --id                                         | String      | The Unique Id for this service within this Beamable CLI context                                                                    |
| --deps                                       | String\[]   | The ','-separated list of existing Beam-O Ids that this service depends on                                                         |
| --local-build-context                        | String      | The path to a valid docker build context with a Dockerfile in it                                                                   |
| --local-dockerfile                           | String      | The relative file path, from the given build-context, to a valid Dockerfile inside that context                                    |
| --local-log                                  | Nullable\`1 | The log level this service should be deployed locally with                                                                         |
| --local-health-endpoint                      | String\[]   | The health check endpoint and port, with no trailing or heading '/', that determines if application is up.                         |
| Example: --local-health-endpoint health 6565 |             |                                                                                                                                    |
| --local-hot-reloading                        | String\[]   | In order, (1, 2) an endpoint and port, with no trailing or heading '/', that determines if the server is set up for hot-reloading. |

(3) the relative path, with no trailing or heading '/', to where the source files to watch are.  
(4) the in-container path where the container expects the source files to be in order to support hot-reloading.  
Example: --local-hot-reloading hot_reloading_enabled 6565 Local\\Path\\To\\Files\\My\\Image\\Expects Path\\In\\Container\\Where\\Files\\Need\\To\\Be|  
|--local-custom-ports|String\[]|Any number of arguments representing pairs of ports in the format LocalPort:InContainerPort.  
Leaving local port empty, as in ':InContainerPort', will expose the container port at the next available local port (this changes every container creation)  
\|  
|--local-custom-bind-mounts|String\[]|Any number of arguments in the format LOCAL_PATH:IN_CONTAINER_PATH to bind between your machine and the docker container|  
|--local-custom-volumes|String\[]|Any number of arguments in the format VOLUME_NAME:IN_CONTAINER_PATH to create and bind named volumes into the docker container|  
|--local-env-vars|String\[]|Any number of arguments in the format NAME=VALUE representing environment variables to set into the local container|  
|--remote-health-endpoint|String\[]|The health check endpoint and port, with no trailing or heading '/', that Beam-O should call on the deployed container to see if application is up.  
Example: --local-health-endpoint health 6565|  
|--remote-env-vars|String\[]|Any number of arguments in the format 'NAME=VALUE' representing environment variables Beam-O should set on the container it runs in AWS|  
|--dryrun|Boolean|Should any networking happen?|  
|--cid|String|Cid to use; will default to whatever is in the file system|  
|--pid|String|Pid to use; will default to whatever is in the file system|  
|--host|String|The host endpoint for beamable|  
|--refresh-token|String|Refresh token to use for the requests|  
|--log|String|Extra logs gets printed out|  
|--dir|String|Directory to use for configuration|  
|--version|Boolean|Show version information|  
|--help|Boolean|Show help and usage information|

### Parent Command

[services](cli-services.md)
