#! /bin/bash

# install tools
sudo apt-get install -y git make python3 python3-pip python3-setuptools python3-wheel

# install dependencies
sudo pip3 install -r requirements.txt

# publish to github pages
sudo make github