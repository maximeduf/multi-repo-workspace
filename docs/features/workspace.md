# Workspace
A workspace is a version controlled folder that contains a workspace.yml file that define the workspace. The file lists the git repositories that compose the workspace.

When a developer wants to work on a project with mrw, they clone the workspace repo, install mrw and run `mrw init` to get all the repositories listed cloned.

The workspace folder is where the folders of the repositories listed in workspace.yml live. These folders are ignored in the workspace's repository to ensure git does not think we are using submodules.

For the full vision, [read this document](../getting-started/vision.md).

## Creating workspaces
With mrw installed, we can create a workspace either with the command line, or by creating the folder and file manually.

The result is a bare bones workspace that is not yet initialized, from which we can continue to use mrw commands or edit the workspace definition file before executing the command `mrw init` or `mrw apply`.

**Bare bone workspace**
```
# workspace.yml
name: workspace
```
[Full specification](./workspace-yml.md).

### Create with mrw
With mrw installed, we can create a workspace with the command `mrw create` to get prompted for the workspace-name and location. The workspace folder and file are created.

### Create manually
1. Create workspace folder named `[workspace-name]`
2. In the workspace folder, create a workspace file names `[workspace-name].yml`
3. Edit the file with at least a name
```
# workspace.yml
name: [workspace-name]
```

## Add repositories to a workspace
Mrw does not *create* repositories, it adds existing repositories to be cloned from a remote url.
To add a repository **to be cloned from an existing remote url**, use the command `mrw repo add` to get prompted for the remote url and, optionaly (default suggested), a pretty_folder_name for the repository.
