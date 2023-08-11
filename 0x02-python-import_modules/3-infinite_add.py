#!/usr/bin/python3

from sys import argv


def add_args():
    result = 0

    if len(argv) < 2:
        print(int(0))

    else:
        for count in range(1, len(argv)):
            result += int(argv[count])

        print("{:d}".format(result))


if __name__ == "__main__":
    add_args()
