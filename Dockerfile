FROM ubuntu

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:git-core/ppa
RUN apt-get update
RUN apt-get install -y build-essential git git-annex

ADD sync.py /sync.py
RUN chmod +x /sync.py

VOLUME /data
