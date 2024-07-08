#!/bin/env bash

cd ..

build_image(){
    if [[ $# != 3 ]]; then
        echo "Usage : build_image image_name dockerfile context_path"
        exit 0
    fi
    image_name=$1
    dockerfile=$2
    context_path=$3
    docker build -t "${image_name}" -f "${dockerfile}" "${context_path}"
    build_success=$?
    if [[ ${build_success} -eq 0 ]]; then
        echo "Build ### ${image_name} ### success!"
    else
        echo "Build ### ${image_name} ### failed!"
        exit 1
    fi
}

push_image(){
    local_image=$1
    if [[ $2 ]];then
	    remote_image=$2
	    docker tag "${local_image}" "${remote_image}"
        docker push "${remote_image}"
    else
        docker push "${local_image}"
    fi
}

CI_COMMIT_SHA=$(git log -1 --abbrev-commit --pretty=oneline | awk '{print $1}')
commit_info_string=$(git log --pretty=format:"%H%cd" --date=format:'%Y%m%d' | grep ${CI_COMMIT_SHA})
DATE=${commit_info_string:40:48}
TAG=$1

image=al6nlee/grpcpy:py3_${DATE}_${CI_COMMIT_SHA:0:7}_${TAG}
# remote_image=""
build_image "${image}" docker/Dockerfile.grpc .
push_image "${image}"

# sh build.sh v0.3