https://aaronlelevier.github.io/virtualenv-cheatsheet/

# install python
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.11

# installs PIP globally
curl https://bootstrap.pypa.io/get-pip.py | python3.11

# install python virtual environment
sudo apt-get install python3.11-venv

# creates a virtualenv
python3.11 -m venv venv

# activates the virtualenv
source venv/bin/activate

pip install -r requirements.txt
