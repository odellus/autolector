#! /bin/bash

echo "Installing software dependencies"
echo "Requires sudo..."
sudo apt-get update -y
sudo apt-get install -y \
  git-lfs \
  python3-pip \
  python3-dev
pip3 install -r requirements.txt

echo "Fetching huggginface question answering model..."
mkdir models
cd models

echo "It complains that git lfs clone is the same as git clone"
echo "but it isn't"
MODEL_NAME=distilbert-base-cased-distilled-squad
git lfs clone https://huggingface.co/$MODEL_NAME
echo "Model and tokenizer have been downloaded to models/${MODEL_NAME}!"
echo "Have a great day!"
# Move back into the repo root
cd -
