#!/bin/bash

# Run from root directory (change 'python' to 'python3' for linux)
python3 -m grpc_tools.protoc -I ./protos --python_out=./requests --grpc_python_out=./requests ./protos/facade.proto
python3 -m grpc_tools.protoc -I ./protos --python_out=./requests --grpc_python_out=./requests ./protos/starter.proto
