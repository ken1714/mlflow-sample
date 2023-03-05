FROM nvidia/cuda:11.3.0-cudnn8-devel-ubuntu20.04

# Essentials
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y python3-pip git

# Dependencies
ADD requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

# Clean caches (reduce docker image size)
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
