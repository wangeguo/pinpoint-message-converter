#!/bin/bash

docker build . -t pinpoint-message-converter:2.0.0
docker save -o pinpoint-message-converter-2.0.0.tar pinpoint-message-converter:2.0.0
