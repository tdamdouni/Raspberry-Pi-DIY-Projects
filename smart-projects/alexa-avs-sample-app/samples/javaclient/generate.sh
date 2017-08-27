#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd $SCRIPT_DIR

echo -n "Product ID: "
read productId

echo -n "Serial Number: "
read dsn

echo -n "Password for Keystores (won't echo): "
read -s password

mkdir -p certs/ca/
mkdir -p certs/server/
mkdir -p certs/client/
mkdir -p ../iOSCompanionApp/Resources/App/
mkdir -p ../androidCompanionApp/app/src/main/res/raw/

openssl genrsa -out certs/ca/ca.key 4096
COMMON_NAME="My CA" openssl req -new -x509 -days 365 -key certs/ca/ca.key -out certs/ca/ca.crt -config ssl.cnf -sha256

# Create the Client KeyPair for the Device Code
openssl genrsa -out certs/client/client.key 2048
COMMON_NAME="$productId:$dsn" openssl req -new -key certs/client/client.key -out certs/client/client.csr -config ssl.cnf -sha256
openssl x509 -req -days 365 -in certs/client/client.csr -CA certs/ca/ca.crt -CAkey certs/ca/ca.key -set_serial 01 -out certs/client/client.crt -sha256
openssl pkcs12 -inkey certs/client/client.key -in certs/client/client.crt -export -out certs/client/client.pkcs12 -password pass:$password

# Create the KeyPair for the Node.js Companion Service
openssl genrsa -out certs/server/node.key 2048
COMMON_NAME="localhost" openssl req -new -key certs/server/node.key -out certs/server/node.csr -config ssl.cnf -sha256
openssl x509 -req -days 365 -in certs/server/node.csr -CA certs/ca/ca.crt -CAkey certs/ca/ca.key -set_serial 02 -out certs/server/node.crt -sha256

# Create the KeyPair for the Jetty server running on the Device Code in companionApp mode
openssl genrsa -out certs/server/jetty.key 2048
COMMON_NAME="localhost" openssl req -new -key certs/server/jetty.key -out certs/server/jetty.csr -config ssl.cnf -sha256
COMMON_NAME="localhost" openssl x509 -req -days 365 -in certs/server/jetty.csr -CA certs/ca/ca.crt -CAkey certs/ca/ca.key -set_serial 03 -out certs/server/jetty.crt -extensions v3_req -extfile ssl.cnf -sha256
openssl pkcs12 -inkey certs/server/jetty.key -in certs/server/jetty.crt -export -out certs/server/jetty.pkcs12 -password pass:$password

# Copy the CA certificate to Android
cp certs/ca/ca.crt ../androidCompanionApp/app/src/main/res/raw/

# Copy the CA certificate in the correct format to iOS
openssl x509 -outform der -in certs/ca/ca.crt -out certs/ca/ca.der
cp certs/ca/ca.der ../iOSCompanionApp/Resources/App/
