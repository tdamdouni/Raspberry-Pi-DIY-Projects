#!/bin/bash

docker build \
--build-arg http_proxy=http://10.97.113.4:3128 \
--build-arg https_proxy=http://10.97.113.4:3128 \
-t stats .
