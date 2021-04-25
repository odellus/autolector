# Question Answering API

Hello all! This is a little example of using :hugs: [huggingface transformers](https://github.com/huggingface/transformers) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html) to create a  question answering API.

### Install
The only real requirement is a Linux environment. If you are using Windows I recommend [installing Ubuntu for Windows](https://ubuntu.com/tutorials/ubuntu-on-windows). To install the needed software dependencies run:
```bash
cd /path/to/question_answering_api
bash install_dependencies.sh
```

### Usage
1. #### Start the API server  
    Open a terminal window and enter:
    ```bash
    cd /path/to/question_answering_api
    python3 question_answering_api.py
    ```
    and let it run while you're playing around with it. To kill the server press `Ctrl-C` while this terminal window is selected and it will close the process.  
    _Note_: The first time this runs `transformers` will need to download [the model](https://huggingface.co/distilbert-base-cased-distilled-squad).
2. #### Run the client.
    In a new terminal (_yes you need two open at the same time!_), run the commands:
    ```bash
    cd /path/to/question_answering_api
    python3 question_answering_client.py
    ```

    You should see something like this.
```
Context:
    The Amazon rainforest (Portuguese: Floresta Amazônica or
    Amazônia; Spanish: Selva Amazónica, Amazonía or usually
    Amazonia; French: Forêt amazonienne; Dutch:
    Amazoneregenwoud), also known in English as Amazonia or
    the Amazon Jungle, is a moist broadleaf forest that
    covers most of the Amazon basin of South America. This
    basin encompasses 7,000,000 square kilometres (2,700,000
    sq mi), of which 5,500,000 square kilometres (2,100,000
    sq mi) are covered by the rainforest. This region
    includes territory belonging to nine nations. The
    majority of the forest is contained within Brazil, with
    60% of the rainforest, followed by Peru with 13%,
    Colombia with 10%, and with minor amounts in Venezuela,
    Ecuador, Bolivia, Guyana, Suriname and French Guiana.
    States or departments in four nations contain "Amazonas"
    in their names. The Amazon represents over half of the
    "planets remaining rainforests, and comprises the "
    largest and most biodiverse tract of tropical rainforest
    in the world, with an estimated 390 billion individual
    trees divided into 16,000 species.
Question:
  Which name is also used to describe the Amazon rainforest in English?
Answer:
  Amazonia.
```  

### Docker

To run the API inside a container you need to take the following steps:
1. #### Install docker
  Follow the instructions [here](https://docs.docker.com/engine/install/) to install docker on your system. You still need to have run `install_dependencies.sh` and have a `models` directory in repository root directory.  

2. #### Build the container
  Open a terminal and run:
  ```bash
  cd /path/to/question_answering_api # Optional if you're in repo root already.
  # Build container and name image qa-api with version tag v1.
  docker build -t qa-api:v1
  ```

3. #### Start the container
  In the same terminal, type in:
  ```bash
  docker run \
    -p 5000:5000 \ # Map port 5000 in container to port localhost:5000
    -v /path/to/question_answering_api/models:/app/models \ # Use abspath!
    qa-api:v1
  ```  

4. #### Run the client
  In a new terminal window (just like before, we need two open), run the following:
  ```bash
  # Make sure you're in repo root!
  python3 question_answering_api.py
  ```  
  
And that's it! If you want to host your API in the cloud now it's almost as easy as saying `docker push`.
