#!/bin/env bash

cd ..
docker build -t grpctmp:v0.7 -f docker/Dockerfile.grpc .