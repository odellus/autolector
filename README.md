# <i class="fas fa-book-open"></i><i class="fas fa-robot"></i>
# Autolector

Hello all! This is a little example of using :hugs: [huggingface transformers](https://github.com/huggingface/transformers) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html) to create a  question answering API.

### Install
The only real requirement is a Linux environment. If you are using Windows I recommend [installing Ubuntu for Windows](https://ubuntu.com/tutorials/ubuntu-on-windows). To install the needed software dependencies run:
```bash
cd /path/to/autolector
bash install_dependencies.sh # This may take a while.
bash fetch_model.sh # So could this, depending on your connection speed.
```

### Usage
1. #### Start the API server  
    Open a terminal window and enter:
    ```bash
    cd /path/to/autolector
    python3 autolector_server.py
    ```
    and let it run while you're playing around with it. To kill the server press `Ctrl-C` while this terminal window is selected and it will close the process.  

2. #### Run the client.
    In a new terminal (_yes you need two open at the same time!_), run the commands:
    ```bash
    cd /path/to/autolector
    python3 autolector_client.py
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
  Follow the instructions [here](https://docs.docker.com/engine/install/) to install docker on your system.  

2. #### Download models  
  To download the models from hugging face open a terminal, navigate to the repository, and run
  ```bash
  bash fetch_model.sh
  ```

3. #### Build the container
  Open a terminal and run:
  ```bash
  cd /path/to/autolector # Optional if you're in repo root already.
  # Build container and name image qa-api with version tag v1.
  docker build -t autolector:v1 . # <-- DON'T FORGET THIS PERIOD!!!
  ```

4. #### Start the container
  In the same terminal, type in:
  ```bash
  docker run \
    -p 5000:5000 \ # binds port host:container
    -v /path/to/autolector/models:/app/models \ # Mounts host:container
    autolector:v1
  ```  

5. #### Run the client
  In a new terminal window (just like before, we need two open), run the following:
  ```bash
  # Make sure you're in repo root!
  python3 autolector_client.py
  ```  

And that's it! If you want to [host your API in the cloud](https://geekflare.com/docker-hosting-platforms/) now it's almost as easy as saying `docker push`.

### Web page
Alternately, you can open up a browser navigate to `./index.html` or open a terminal and enter:
```bash
# Of course...
cd /path/to/autolector

# If you've installed locally.
python3 autolector_server.py & # This will run process in the background

##########
##  OR  ##
##########

# If you've installed with docker.
docker run \
  -p 5000:5000 \ # binds port host:container
  -v /path/to/autolector/models:/app/models \ # Mounts host:container
  autolector:v1 & # Not sure if this is necessary, but whatever.

# You've got to change /path/to -> <the actual path>
firefox file:///path/to/autolector/index.html
```
after getting the API running locally as show above. I recommend this way, as it shows the real value of putting a service behind an API rather than creating a question answering agent on the command line. It should look something like this.
![autolector](./autolector.png)

### Conclusion  
So now you've got a good idea of how to design a website from front to back. You can host your static code on github, put your Flask APIs somewhere in the cloud (that's what docker is good for), and you're in business. Good luck!
