#!/bin/bash

docker build . -t pinpoint-message-converter:1.4.1
docker save -o pinpoint-message-converter-1.4.1.tar pinpoint-message-converter:1.4.1
