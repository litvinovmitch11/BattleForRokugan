#!/bin/bash

# if it doesn't work on ubuntu try change python to python3
if ! [ -d ../common ]; then
mkdir '../common'
fi
python -m grpc_tools.protoc -I ../proto --python_out=../common --grpc_python_out=../common ../proto/facade.proto
python -m grpc_tools.protoc -I ../proto --python_out=../common --grpc_python_out=../common ../proto/registration.proto
