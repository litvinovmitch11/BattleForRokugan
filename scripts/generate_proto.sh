#!/bin/bash

python -m grpc_tools.protoc -I ../proto ./ --python_out=../common --grpc_python_out=../common ./facade.proto
python -m grpc_tools.protoc -I ../proto --python_out=../common --grpc_python_out=../common ./registration.proto
