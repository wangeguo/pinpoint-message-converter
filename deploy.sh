#!/bin/bash

kind load docker-image pinpoint-message-converter:2.0.0
kubectl delete --ignore-not-found=true -f k8s-dev.yaml
kubectl apply -f k8s-dev.yaml
