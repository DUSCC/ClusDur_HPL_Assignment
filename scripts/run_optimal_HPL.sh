cp HPL_best.dat hpl-2.3/testing/HPL.dat
cd hpl-2.3/testing

mpirun -np 20 ./xhpl > res_best.txt
cp res_best.txt ../../