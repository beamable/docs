See the [Getting Started](../guides/getting-started.md) guide for information on how to get setup with the Beamable CLI.

All of the Beam CLI commands are available in the left navigation bar. This table links directly to some of the most common commands.

| Command                      | Description                                                             |
| :--------------------------- | :---------------------------------------------------------------------- |
| [Init](cli-command-reference/init.md)         | `beam init` will create a Beamable project in the CLI                   |
| [Config](cli-command-reference/config/config.md)     | `beam config` helps you verify your current Beamable project in the CLI |
| [Login](cli-command-reference/login.md)       | `beam login` helps you manage access tokens for use in the CLI          |
| [Project](cli-command-reference/project/project.md)   | `beam project` helps you create and use Standalone Microservices        |
| [Local](cli-command-reference/local/local.md) | `beam local` commands for managing local backend development             |

## Global Options

The following options are available for all Beam CLI commands:

### Java Path
The `--java-path` option allows you to specify a custom location for Java 8, which is required for local backend development commands.

- **Flag**: `--java-path`
- **Default**: The CLI attempts to resolve Java through common install locations
- **Environment Variable**: `BEAM_JAVA_EXE` 
- **Description**: Points to the Java 8 executable needed to run backend tools and utilities

Example: