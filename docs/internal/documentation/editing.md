# Editing Documents

## Setup your Environment
`TODO: Informations about setup the environment. We need to create a installer for the tools we use to create the documentation.`

## Building the Documentation
We use [MkDocs](https://www.mkdocs.org/) to generate our documentation and [Mike](https://github.com/jimporter/mike) to Deploy multiple versions of it. Here's a list of the most important commands used in the process:

| Command                               | Description                                                                   |
|---------------------------------------|-------------------------------------------------------------------------------|
| `mkdocs serve`                        | Run the the current version of the documentation locally                      |
| `mike serve`                          | Run the complete  documentation with the versions drop down locally           |
| `mike deploy <NameOfTheVersion>`      | Deploy the current branch as a version of the documentation                   |
| `mike set-default <NameOfTheVersion>` | Set a especific version as the Default when running the documentation website |

Here's a list of the most common used use cases:

| Use Case | Action |
|----------|--------|
| I want to get the documentation running as local preview | Run `mkdocs serve` and open your browser at `http://
| I want to see the documentation with all versions | Run `mike serve` and open your browser at `http://localhost:8000`
| I want to deploy a new/updated version of the documentation | Run `mike deploy <NameOfTheVersion>` and check the results at `http://localhost:8000`
| I want to submit the deployied documentation to the repository | Commit the "gh-pages" branch. This folder contains the generated documentation.

## Editing Workflows
Here's a list of the most common used use cases when editing the documentation and what to do in each case:

| Use Case                                                 | Workflow                                                          |
|----------------------------------------------------------|-------------------------------------------------------------------|
| I did fix a internal bug for next Major or Minor release | Edit the release notes document in the Latest SDK version branch. |
| I did fix a internal bug for next Patch release          | Edit the release notes document in the Current SDK version        |
| I did change a function call or semantics that now works differently than before.| Edit the release notes document in the correct SDK version with a migration info. Check the related documentation of this system for inconsistencies, Check all snippets, Check if all samples are compiling correctly|
| I did implement a new Feature that is only related to a single SDK. It will be released at the next Major or Minor version| Edit the release notes document in the Latest SDK version branch and create a specific documentation for this new feature.|
|I did implement a new Feature that touch all SDKs and the CL| IEdit the Core documentation with the new feature, merge this in the Latest SDK versions and add to the release notes in all the Latest SDK versions|
|I do want to forwarding/backport a bug fix to a old/new version|Edit the corresponding version of the documentation you did change, add the change to the release notes of it
| 





