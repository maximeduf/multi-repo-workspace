# Vision
A multi-repo worksapce is a version controlled folder that works with mrw command to manage the workspace's  development environment. The workspace lists the repositories of its components without the need for git submodules.

The workspace repository becomes the starting point to quickly setup a development environment described by the yml workspace file. 

When initialized, a workspace gets its repositories cloned and overall configurations applied to the system. For example: 
- install system dependencies
- install and package manager dependencies
- configure package managers
- set environment variables
- more

All operations executed on the system are validated, logged and revertable.

## Using the CLI
There are different ways of using mrw in a perfect world
- edit a yml file, use the cli to parse it and apply it
- use the cli to do everything
- either way, use a non-interactive (with commmand arguments) or interactive approach (prompts to get the information)

## Commands
The most important commands are
| Command      | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| mrw create   | Create a workspace folder and file                                            |
| mrw init     | Initialize a workspace from folder and file. Update if workspace exists.      |
| mrw apply    | Update a workspace after manual edits. Initialize if workspace doesn't exist. |
| mrw add repo | Edit workspace file automatically to add a repository.                        |

Other commands eventually
| Command          | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| mrw add config   | Add a configuration to a workspace.                         |
| mrw rm repo      | Remove a repository from a workspace.                       |
| mrw status       | Prints status of workspace configurations and repositories. |
| mrw add script   | Add a workspace script.                                     |
| mrw rm script    | Remove a script.                                            |
| mrw run "script" | Run a workspace script.                                     |
| ...              |                                                             |


## Priority
Priority is on  **non-interactive** approach to create a workspace that can **clone all repositories in one go**, with **only git repository configurations**. Some other configurations are already modeled, but they are not critical for this project to be useful. Incrementally add more prompts and confirmations to be able to use it more interactively.

## Ultimate goal
The ultimate goal is to be able to have :
- other configurations, like aliases, functions or environment variables, available system wide.
- install dependencies by providing commands to execute after repository cloning
- ensure other configurations, for example a etc/hosts line, presence of environment variables or any other requirement for development of a project.
- have the ability to use yaml first or cli first and interactive or non-interactive.

This was thought with linux in mind but being compatible with windows would be best.
