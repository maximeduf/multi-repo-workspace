# mrw apply
Apply a workspace definition. It will initialize the workspace before if not already done.
More precisely, ensure that:
- repositories listed are cloned.
- the workspace folder is version controlled with git.

## synopsis
**in the same folder as a workspace file**
```bash
mrw apply
```
**to apply a specified workspace file in its current directory**
```bash
mrw apply --file ../tests/test-workspace.yml
``` 
