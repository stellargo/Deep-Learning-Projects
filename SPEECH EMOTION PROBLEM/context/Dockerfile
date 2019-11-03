FROM ubuntu:14.04

# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade
RUN apt-get install -y emacs

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Add sudo
RUN apt-get -y install sudo

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/
#RUN echo `pwd`

# Anaconda installing
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh
RUN bash Anaconda3-2019.10-Linux-x86_64.sh -b
RUN rm Anaconda3-2019.10-Linux-x86_64.sh

# Set path to conda
#ENV PATH /root/anaconda3/bin:$PATH
ENV PATH /home/ubuntu/anaconda3/bin:$PATH

RUN conda init bash

RUN /bin/bash -c "pip install librosa==0.6.3"
RUN /bin/bash -c "pip install tensorflow==1.15.0"

COPY opensmile-2.3.0.tar.gz /home/ubuntu/opensmile-2.3.0.tar.gz
RUN tar -zxvf opensmile-2.3.0.tar.gz

RUN sudo apt-get install autotools-dev -y
RUN sudo apt-get install automake -y
RUN sudo apt-get install build-essential -y

RUN cd opensmile-2.3.0 && ls && bash ./autogen.sh %% ./configure && bash ./buildStandalone.sh

RUN wget -O model.h5 https://dl.dropboxusercontent.com/s/wrpmn5m5xzq59lm/model.h5?dl=0

COPY output.py /home/ubuntu/output.py
COPY model/mean.npy /home/ubuntu/mean.npy
COPY model/std.npy /home/ubuntu/std.npy


ENTRYPOINT ["/bin/bash"]