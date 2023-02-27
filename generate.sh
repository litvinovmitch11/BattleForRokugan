#!/bin/bash

# Run from root directory
python -m grpc_tools.protoc -I ./protos --python_out=./basic --grpc_python_out=./basic ./protos/basic.proto
