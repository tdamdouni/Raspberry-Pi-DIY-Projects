FROM resin/rpi-raspbian:jessie
ENTRYPOINT []

RUN apt-get update -qy && apt-get -qy install \
  build-essential git
WORKDIR /root/
RUN git clone https://github.com/FFmpeg/FFmpeg.git
workdir /root/FFmpeg
RUN apt-get install -qy libomxil-bellagio-dev

RUN ./configure --arch=armel --target-os=linux --enable-gpl --enable-omx --enable-omx-rpi --enable-nonfree
RUN make
RUN make install

CMD ["/bin/bash"]
