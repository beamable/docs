---
title: "Project Add"
slug: "cli-project-add"
excerpt: "Add new project to an existing solution in current working directory"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jun 14 2023 17:20:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 25 2023 20:56:57 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project add <name> [options]
```

## About

Add new project to an existing solution in current working directory

## Arguments

| Name | Type        | Description             |
| ---- | ----------- | ----------------------- |
| name | ServiceName | Name of the new project |

## Options

| Name            | Type        | Description                                                |
| --------------- | ----------- | ---------------------------------------------------------- |
| --solution-name | ServiceName | Name of the existing solution                              |
| --skip-common   | Boolean     | If you should create a common library                      |
| --dryrun        | Boolean     | Should any networking happen?                              |
| --cid           | String      | Cid to use; will default to whatever is in the file system |
| --pid           | String      | Pid to use; will default to whatever is in the file system |
| --host          | String      | The host endpoint for beamable                             |
| --refresh-token | String      | Refresh token to use for the requests                      |
| --log           | String      | Extra logs gets printed out                                |
| --dir           | String      | Directory to use for configuration                         |
| --version       | Boolean     | Show version information                                   |
| --help          | Boolean     | Show help and usage information                            |

### Parent Command

[project](cli-project.md)
