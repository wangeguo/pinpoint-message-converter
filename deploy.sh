#!/bin/bash

kind load docker-image pinpoint-message-converter:2.1.1
kubectl delete --ignore-not-found=true -f k8s-dev.yaml
kubectl apply -f k8s-dev.yaml
