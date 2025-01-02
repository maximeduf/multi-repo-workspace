# Install for development
## Python, pip and dependencies
`sudo add-apt-repository ppa:deadsnakes/ppa`
`sudo apt-get install python3.13`
`sudo apt-get install python3.13-dev`
`sudo apt-get install build-essential`
`sudo apt-get install python3.13-venv`
**Installs PIP globally**
`curl https://bootstrap.pypa.io/get-pip.py | python3.13`

## Virtual environment

### creates a virtualenv
`python3.13 -m venv venv`

### activates the virtualenv
`source venv/bin/activate`
**to deactivate**
`deactivate`

## Install multi-repo-workspace
in venv activated, editable install of the code with testing dependencies
`python -m pip install -e ."[test]"`

## Run tests
```
PYTHONPATH=src pytest --cov-config .coveragerc --cov-report term-missing --cov=multi_repo_workspace tests
```
or
```
./run_tests.sh
```

## Use mrw
`mrw -v`

## Next
See [Quick Start Guide](quick-start.md).
See [Contributing](./contributing.md).
