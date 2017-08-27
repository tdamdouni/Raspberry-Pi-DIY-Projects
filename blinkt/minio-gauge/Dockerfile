FROM resin/rpi-raspbian:jessie

RUN apt-get update -qy && \
   apt-get install --no-install-recommends -qy \
    python \
    python-pip \
    python-rpi.gpio \
    git && \
    pip install flask && \
     git clone https://github.com/pimoroni/blinkt/ /root/blinkt/ && \
     apt-get remove git -qy && \
     rm -rf /var/lib/apt/lists/*

WORKDIR /root/
COPY . .
WORKDIR /root/blinkt/library
RUN python setup.py install
WORKDIR /root/examples/
ENTRYPOINT []
CMD ["python", "larson.py"]
