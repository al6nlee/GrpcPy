#!/bin/env bash

cd ..
docker build -t grpctmp:v0.5 -f docker/Dockerfile.grpc .