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
# keras & tensorflow
RUN pip3 install keras regex progress setproctitle h5py tensorflow  

# maca
RUN echo 'krnnt\nkrnnt\n' | adduser krnnt --home /home/krnnt --ingroup sudo
USER krnnt
RUN cd &&\
    git clone http://github.com/apohllo/corpus2.git &&\
    cd /home/krnnt/corpus2 &&\
    mkdir bin &&\
    cd bin &&\
    cmake .. &&\
    make -j4 &&\
    echo 'krnnt' | sudo -S make install &&\
    rm -rf /home/krnnt/corpus2
RUN cd &&\ 
    git clone http://github.com/apohllo/toki.git &&\
    cd /home/krnnt/toki &&\
    mkdir bin &&\
    cd bin &&\
    cmake .. &&\
    make -j4 &&\
    echo 'krnnt' | sudo -S make install &&\
    rm -rf /home/krnnt/toki
RUN cd &&\
    mkdir morfeusz &&\
    cd morfeusz &&\
    wget https://launchpad.net/~bartosz-zaborowski/+archive/ubuntu/nlp/+files/morfeusz-sgjp_0.81-1_amd64.deb &&\
    echo 'krnnt' | sudo dpkg -i morfeusz-sgjp_0.81-1_amd64.deb &&\
    rm -rf /home/krnnt/morfeusz
RUN cd &&\ 
    git clone http://github.com/apohllo/maca.git &&\
    cd /home/krnnt/maca/third_party/SFST-1.2/SFST/src/ &&\
    make &&\
    echo 'krnnt' | sudo -S make install &&\
    cd /home/krnnt/maca &&\
    mkdir bin &&\
    cd bin &&\
    cmake .. &&\
    make -j4 &&\
    echo 'krnnt' | sudo -S make install &&\
    echo 'krnnt' | sudo -S ldconfig &&\
    rm -rf /home/krnnt/maca

# krnnt
RUN cd &&\
    git clone https://github.com/apohllo/krnnt &&\
    cd krnnt &&\
    sudo -S pip3 install -e . &&\
    wget https://github.com/kwrobel-nlp/krnnt/releases/download/poleval/reana.zip &&\
    unzip reana.zip -d ./reana/ &&\
    rm reana.zip 
    
ENV PYTHONIOENCODING utf-8
ENV PYTHONPATH=$HOME/krnnt/:$PYTHONPATH
