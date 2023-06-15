#!/bin/bash

docker build . -t pinpoint-message-converter:1.3.0
docker save -o pinpoint-message-converter-1.3.0.tar pinpoint-message-converter:1.3.0
