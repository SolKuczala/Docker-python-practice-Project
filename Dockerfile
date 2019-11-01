FROM ubuntu:16.04

RUN apt-get update -y; \
    apt-get install -y python3\
    git; git clone https://github.com/SolKuczala/Docker-python-practiceProject.git

CMD grsed
