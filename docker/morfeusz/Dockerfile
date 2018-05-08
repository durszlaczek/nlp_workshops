FROM ubuntu:xenial

# encoding & main libs
RUN apt-get update &&\
    apt-get install --reinstall -y locales  &&\
    sed -i 's/# pl_PL.UTF-8 UTF-8/pl_PL.UTF-8 UTF-8/' /etc/locale.gen &&\
    sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&\
    locale-gen pl_PL.UTF-8 &&\
    locale-gen en_US.UTF-8 &&\
    apt-get install -y build-essential cmake bison flex python-dev swig git subversion &&\
    apt-get install -y libicu-dev libboost1.58-all-dev libloki-dev libxml++2.6-dev libedit-dev libreadline-dev &&\
    apt-get install -y wget software-properties-common python-software-properties &&\
    apt-get install -y sudo libncurses-dev python3-pip unzip &&\
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip3 install --upgrade pip
RUN pip3 install jupyter notebook 
RUN pip3 install pandas keras tensorflow

# morfeusz
RUN apt-get install wget -y
RUN wget -O - http://sgjp.pl/apt/sgjp.gpg.key| apt-key add -
RUN apt-get install software-properties-common python-software-properties -y
RUN add-apt-repository 'deb http://sgjp.pl/apt/ubuntu trusty main'
RUN apt-get update
RUN apt-get install python-morfeusz2 -y
