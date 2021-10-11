FROM balenalib/raspberrypi3-node:10.18
MAINTAINER Tamas Eros (tamas.eros1@gmail.com)

RUN apt-get update --allow-unauthenticated --fix-missing
RUN apt-get install -y python3 \
                       python3-pip \
                       curl \
                       wget

RUN python3 -m pip install flask

ADD rpi_control.py /usr/bin/

WORKDIR /

ENTRYPOINT /usr/bin/rpi_control.py
