#!/bin/bash

# assume CentOS - install necessary libraries
sudo yum install -y openblas openblas-devel
sudo yum install -y openmpi openmpi-devel


# make sure openmpi executables are on the PATH.
touch ~/.bashrc
cat "PATH=\"/usr/lib64/openmpi/bin:$PATH\"" >> .bashrc

touch ~/.zshrc
cat "PATH=\"/usr/lib64/openmpi/bin:$PATH\"" >> .zshrc