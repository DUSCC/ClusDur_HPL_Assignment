#!/bin/bash

NCORES=(2 4 8 16 20)

cd hpl-2.3/testing
mkdir graph_res

for NCORE in "${NCORES[@]}"; do
    cp ../../HPL_$NCORE.dat HPL.dat
    mpirun -np $NCORE ./xhpl > raw_$NCORE.txt
    cp res_$NCORE.txt ../../graph_res
done

