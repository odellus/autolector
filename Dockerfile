# Pull an image of Ubuntu 20.04 as the base for this container.
FROM ubuntu:20.04

# Set /app to be the root directory of the container.
WORKDIR /app

# Let's go ahead and copy requirements.txt into container.
COPY ./requirements.txt /app/requirements.txt

# Now we install our dependencies. Don't need sudo. We're root.
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install -r requirements.txt

# Copy the rest of the code in after we've downloaded
# and installed the dependencies. That way code changes
# will not require reinstalling PyTorch for every typo.
COPY . /app

# This is the program that is run as an entrypoint to container
# I often comment this part out when testing so I can run:
#   docker run -it image_name:version_tag /bin/bash
# and take a look around inside the container.
ENTRYPOINT ["python3"]

# We're going to execute python3 question_answering_api.py
# like we are in the /app directory whenever we use this container.
# This also needs to be commented out to run:
#   docker run -it image_name:version_tag /bin/bash
# for debugging purposes. Uncommenting and running:
#    docker build -t image_name:version_tag .
# will not take long at all unless you change requirements.txt.
CMD ["question_answering_api.py"]
