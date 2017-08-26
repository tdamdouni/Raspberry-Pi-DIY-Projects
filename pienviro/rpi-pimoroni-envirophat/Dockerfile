FROM jbrisbin/rpi-python3
MAINTAINER Jon Brisbin <jon@jbrisbin.com>

# Install Enviro pHAT
RUN apt-get install -y python3-envirophat --no-install-recommends

# Clean up APT cache
RUN rm -rf /var/lib/apt/lists/*

VOLUME /data
WORKDIR /data

# Set CMD to python3
ENTRYPOINT ["python3"]