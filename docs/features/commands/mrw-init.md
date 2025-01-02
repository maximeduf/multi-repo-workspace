# mrw init
Initialize a workspace. It will apply the workspace if it is already initialized.
More precisely, ensure that:
- repositories listed are cloned.
- the workspace folder is version controlled with git.

## synopsis
**in the same folder as a workspace file**
```bash
mrw init
```
**to apply a specified workspace file in its current directory**
```bash
mrw init --file ../tests/test-workspace.yml
``` 
