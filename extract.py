#!/usr/bin/python3

import os

def main():
    fnames = []
    ivals = [2, 4, 8, 16, 20]
    for i in ivals:
        filename = f"graph_res/res_{i}.txt"
        fnames.append(filename)
    vals = []
    for fname in fnames:
        with open(fname) as file:
            for line in file.readlines():
                # assume only one result if using our script
                if line.startswith("WR"):
                    words = line.split()
                    val = float(words[-1])
                    vals.append(val)
                    break
    for j in range(len(ivals)):
        with open("graph_results.txt", mode="w") as ofile:
            line = f"{ivals[j]} {vals[j]}"
            ofile.write(line + os.linesep)

if __name__ == "__main__":
    main()