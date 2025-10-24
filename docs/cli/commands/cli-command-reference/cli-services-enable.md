---
title: "Services Enable"
slug: "cli-services-enable"
excerpt: "Enables/Disables existing services"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jun 14 2023 17:20:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 25 2023 20:56:56 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam services enable [options]
```

## About

Enables/Disables existing services

## Options

| Name            | Type        | Description                                                                                 |
| --------------- | ----------- | ------------------------------------------------------------------------------------------- |
| --id            | String      | The Unique Id for this service within this Beamable CLI context                             |
| --enabled       | Boolean     | Whether or not we should try and run the service when we deploy remotely                    |
| --no-deps       | Nullable\`1 | Propagates the change to the services dependencies. When disabling, this is true by default |
| --dryrun        | Boolean     | Should any networking happen?                                                               |
| --cid           | String      | Cid to use; will default to whatever is in the file system                                  |
| --pid           | String      | Pid to use; will default to whatever is in the file system                                  |
| --host          | String      | The host endpoint for beamable                                                              |
| --refresh-token | String      | Refresh token to use for the requests                                                       |
| --log           | String      | Extra logs gets printed out                                                                 |
| --dir           | String      | Directory to use for configuration                                                          |
| --version       | Boolean     | Show version information                                                                    |
| --help          | Boolean     | Show help and usage information                                                             |

### Parent Command

[services](cli-services.md)
