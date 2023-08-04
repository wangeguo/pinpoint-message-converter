#!/bin/bash

docker build . -t pinpoint-message-converter:3.1.0
docker save -o pinpoint-message-converter-3.1.0.tar pinpoint-message-converter:3.1.0
