#! /bin/bash
echo "Fetching huggginface question answering model..."
mkdir models
cd models

echo "It complains that git lfs clone is the same as git clone"
echo "but it isn't"
MODEL_NAME=distilbert-base-cased-distilled-squad
git lfs clone https://huggingface.co/$MODEL_NAME
echo "Model and tokenizer have been downloaded to models/${MODEL_NAME}!"
# Move back into the repo root
cd -
echo "Have a great day!"
