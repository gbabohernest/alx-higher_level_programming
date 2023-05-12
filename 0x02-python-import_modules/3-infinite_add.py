#!/usr/bin/python3

from sys import argv

def add_arg():

    result = 0

    if len(argv) < 2:
        print(int(0))
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print(result)

if __name__ == "__main__":
    add_arg()
