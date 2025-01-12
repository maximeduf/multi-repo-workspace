# multi-repo-workspace (mrw)
`mrw` is a tool for managing multiple Git repositories in one workspace. It uses a yml file that lists the repositories and configurations of the workspace, allowing developers to clone and manage all repos with a single command. New contributors can start quickly by cloning the workspace and running `mrw init`.

## Docs
For full documentation see [mrw documentation](./docs/README.md).

## Prerequisites
for python prerequisites see [installation documentation](./docs/getting-started/installation.md).

## Install and Run for development
in venv activated
```
python -m pip install -e ."[test]"
```

### CLI
```
mrw
```

### Tests
```
PYTHONPATH=src pytest --cov-config .coveragerc --cov-report term-missing --cov=multi_repo_workspace tests
```
or
```
./run_tests.sh
```

## Usage
for usage, look at [quick-start.md](./docs/getting-started/quick-start.md).
