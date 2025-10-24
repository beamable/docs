# this script will generate the CLI command docs
# Note: the commands will be generated from the globally installed CLI
#       (which means you need to have the CLI installed globally)
#       (and also; make sure the VERSION matches your current branch intentions)

# Usage: 
#   Run this from the root of the docs repository
#   ./scripts/generate-cli-commands.sh

rm -rf docs/cli/commands/cli-command-reference
beam mkdocs -o docs/cli/commands/cli-command-reference