#!/bin/bash

docker build . -t pinpoint-message-converter:3.1.1
docker save -o pinpoint-message-converter-3.1.1.tar pinpoint-message-converter:3.1.1
