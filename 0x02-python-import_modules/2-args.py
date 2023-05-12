#!/usr/bin/python3

import sys


def args():
    output_str = "arguments"
    delim = "."
    
    str_len = len(sys.argv) - 1
    
    if (str_len == 1):
        output_str = "argument"
    if (str_len > 0):
        delim = ":"
    
    print("{} {}{}".format(str_len, output_str, delim))
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        if (i > 0):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    args()
