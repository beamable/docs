# Configuration

## What is the .beamable folder?

The Beam CLI uses a hidden `.beamable/` folder to manage state between multiple invocations of `beam` commands. The `.beamable/` folder has information for 1 Beamable project.
Every time you execute a `beam` command, it searches for the nearest `.beamable/` folder in the parent lineage of your current directory. If you run [beam config](../commands/cli-command-reference/config/config.md) in a folder containing `.beamable/`, or any child folder, then that `.beamable/` folder is used for the configuration.

### Example

With given structure:
```

mainFolder
├───.beamable
├───.config
└───childFolder
    ├───.beamable
    └───yetAnotherFolder
someOtherFolder
```

| call directory     | which config would be used         |
| ------------------ | ---------------------------------- |
| `mainFolder`       | `mainFolder/.beamable`             |
| `childFolder`      | `mainFolder/childFolder/.beamable` |
| `yetAnotherFolder` | `mainFolder/childFolder/.beamable` |
| `someOtherFolder`  | no config is available             |


## Validation 

From any folder, you can run the [beam config](../commands/cli-command-reference/config/config.md) command to print information about your current Beamable folder. 

In the example directory structure above, if the `beam config` command was invoked from the `mainFolder`, it would log information about the `mainFolder/.beamable` folder. 
```sh
mainFolder % dotnet beam config
 {                                                             
    "host": "https://api.beamable.com",                        
    "cid": "<redacted>",                                 
    "pid": "<redacted>",                              
    "configPath": "/Users/examples/mainFolder/.beamable" 
 } 
```

However, if the `beam config` command was invoked from the `someOtherFolder` path, you should expect to see an error, because there is no `.beamable` folder within the parent linear. 

```sh
someOtherFolder % dotnet beam config

**Error** [0404]: Could not find any .beamable config folder which is required for this command.

NOTE: Consider calling `beam init` first.

  

Logs at

  /var/folders/ys/949qmfy15r7bl8x36s6wmm000000gn/T/beamCliLog.txt
```

## Dotnet Tool Folder

The Beamable CLI executes as a local dotnet tool installation. That means that there should be a `.config/` folder in your project. There should be a file called `dotnet-tools.json` in the folder, declaring the version of the CLI you are using.

```json
{
  "version": 1,
  "isRoot": true,
  "tools": {
    "beamable.tools": {
      "version": "7.0.0",
      "commands": [
        "beam"
      ]
    }
  }
}
```

!!! info "The folder can exist in a higher folder."

    Normally the `.config/` folder exists as a sibling of the `.beamable/` folder. However, the `.config/` folder _may_ exist in a parent folder. The closest `.config/` folder will be used. See the [dotnet tool documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/local-tools-how-to-use) for more information. 




## Workspace Overview

A Beamable workspace is defined by the existence of a `.beamable/` folder. 

| Path             | Note              |
| ---------------- | ----------------- |
| `config.beam.json` | this file must exist, and contains your project's connection information. | 
| `/temp` | this folder should not be included in version control. It contains information about your current session. The contents of this folder may be discarded at any time |
| `/shared` | this folder contains information that will be shared with other developers in the project |
| `/local` | this folder should not be included in version control. It contains local information specific to your session |
