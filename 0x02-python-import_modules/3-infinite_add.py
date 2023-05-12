#!/usr/bin/python3

import sys

def add_arg():

    result = 0

    if len(sys.argv) < 2:
        print(int(0))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print(result)

if __name__ == "__main__":
    add_arg()
