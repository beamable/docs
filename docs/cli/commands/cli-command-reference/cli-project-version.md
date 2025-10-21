---
title: "Project Version"
slug: "cli-project-version"
excerpt: "Commands that lists Beamable package versions of a SAMS projects"
hidden: false
createdAt: "Fri May 24 2024 19:54:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 24 2024 19:54:22 GMT+0000 (Coordinated Universal Time)"
---
```shell
beam project version [options]
```

## About

Commands that lists Beamable package versions of a SAMS projects

## Options

| Name                | Type    | Description                                                                               |
| ------------------- | ------- | ----------------------------------------------------------------------------------------- |
| --requested-version | String  | Request specific version of Beamable packages                                             |
| --dryrun            | Boolean | Should any networking happen?                                                             |
| --cid               | String  | Cid to use; will default to whatever is in the file system                                |
| --pid               | String  | Pid to use; will default to whatever is in the file system                                |
| --quiet             | Boolean | When true, skip input waiting and use defaults                                            |
| --host              | String  | The host endpoint for beamable                                                            |
| --refresh-token     | String  | Refresh token to use for the requests                                                     |
| --log               | String  | Extra logs gets printed out                                                               |
| --dir               | String  | Directory to use for configuration                                                        |
| --raw               | Boolean | Output raw JSON to standard out. This happens by default when the command is being piped  |
| --pretty            | Boolean | Output syntax highlighted box text. This happens by default when the command is not piped |
| --dotnet-path       | String  | a custom location for dotnet                                                              |
| --version           | Boolean | Show version information                                                                  |
| --help              | Boolean | Show help and usage information                                                           |

### Parent Command

[project](cli-project.md)
