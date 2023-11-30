#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lim_t = len(sys.argv)
    val = 0
    for i in range(1, lim_t):
        val = val + int(sys.argv[i])
    print(val)
