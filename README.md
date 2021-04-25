# Question Answering API

Hello all! This is a little example of a question answering API for using :hugs: [huggingface](https://huggingface.co/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html) to create a RESTful natural language processing API with minimal amounts of coding.

### Install
1. The only requirements are [Git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04) and [Python3](https://docs.python-guide.org/starting/install3/linux/) with [pip](https://pip.pypa.io/en/stable/installing/) installed in a Linux environment. If you are using Windows I recommend [installing Ubuntu for Windows](https://ubuntu.com/tutorials/ubuntu-on-windows). If you don't have pip installed, you can open a terminal and enter:
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  ```
2. In the same or a new terminal enter:
  ```bash
  cd /path/to/question_answering_api # Where ever you forked it to. I don't know!
  python3 -m pip install requirements.txt
  ```
  and that should install the requirements for the Question Answering API.

### Usage
1. #### Start the API server  
    Open a terminal window and enter:
    ```bash
    cd /path/to/question_answering_api
    python3 question_answering_api.py
    ```
    and let it run while you're playing around with it. To kill the server press `Ctrl-C` while this terminal window is selected and it will close the process.
2. #### Run the client.
    In a new terminal (_yes you need two open at the same time!_), run the commands:
    ```bash
    cd /path/to/question_answering_api
    python3 question_answering_client.py
    ```

    You should see something like this
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
