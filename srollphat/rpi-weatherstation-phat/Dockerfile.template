# Dockerfile templates infomation: http://docs.resin.io/deployment/docker-templates/
# Resin base images infomation: http://docs.resin.io/runtime/resin-base-images/
FROM resin/%%RESIN_MACHINE_NAME%%-debian:latest

# Add library dependencies
RUN apt-get update && apt-get install -y \
  python \
  python-envirophat \
  python-microdotphat

# Set our working directory
WORKDIR /usr/src/app

# This will copy all files in our root to the working directory in the container
COPY . ./

# Switch on systemd init system in container
ENV INITSYSTEM on

CMD ["bash","start.sh"]
