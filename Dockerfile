FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3 git python3-pip

RUN pip3 install flask

RUN git clone https://github.com/SolKuczala/Docker-python-practiceProject.git

WORKDIR /Docker-python-practiceProject

CMD python3 ./web.py
