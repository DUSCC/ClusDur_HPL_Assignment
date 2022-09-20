#!/bin/bash

# get sources
wget https://www.netlib.org/benchmark/hpl/hpl-2.3.tar.gz
tar xpf hpl-2.3.tar.gz

# build them
pushd hpl-2.3
./configure
make -j$(nproc)
echo "xhpl is ready in hpl-2.3/testing"