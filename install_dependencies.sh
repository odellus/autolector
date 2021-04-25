#! /bin/bash

echo "Installing software dependencies"
echo "Requires sudo..."
sudo apt-get update -y
sudo apt-get install -y \
  git-lfs \
  python3-pip \
  python3-dev
pip3 install -r requirements.txt
