#!/usr/bin/python3

from matplotlib import pyplot as plt

def read_data(filename):
    with open(filename) as file:
        lines = file.readlines()
        ncores, gflops = [], []
        for line in lines:
            words = line.split()
            ncores.append(int(words[0]))
            gflops.append(float(words[1]))
        return ncores, gflops

if __name__ == "__main__":
    ncores, gflops = read_data("plot_vals.txt")
    plt.scatter(ncores, gflops)
    plt.xticks([i for i in range(21)])
    plt.xlabel("number of cores")
    plt.ylabel("GFlops")
    plt.title("GFlops against number of cores")
    plt.show()