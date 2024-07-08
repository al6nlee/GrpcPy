#!/bin/bash

declare -a services=("hello" "user")

for SERVICE in "${services[@]}"; do
    echo "Compiling service: $SERVICE"

    # 设置目标目录
    DESTDIR="../generated/$SERVICE"

    # 确保目标目录存在，如果不存在则创建它
    mkdir -p $DESTDIR

    # 使用 grpc_tools.protoc 编译 .proto 文件
    python3 -m grpc_tools.protoc \
        --proto_path=$SERVICE/ \
        --python_out=$DESTDIR \
        --grpc_python_out=$DESTDIR \
        $SERVICE/*.proto

    # 修正生成的 helloworld_pb2_grpc.py 文件中的导入路径
    grpc_file="$DESTDIR/${SERVICE}_pb2_grpc.py"
    if [[ -f $grpc_file ]]; then
        sed -i.bak "s/import ${SERVICE}_pb2 as ${SERVICE}__pb2/from . import ${SERVICE}_pb2 as ${SERVICE}__pb2/" $grpc_file
        rm "$grpc_file.bak"
    fi

    echo "Generated and fixed imports for $SERVICE"
done
