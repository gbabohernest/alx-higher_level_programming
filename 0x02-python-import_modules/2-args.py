#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num_of_args = len(argv) - 1
    arg_placeholder = "arguments"
    deliminator = "."

    if (num_of_args == 1):
        arg_placeholder = "argument"

    if (num_of_args - 1 >= 0):
        deliminator = ":"

    print("{} {}{}".format(num_of_args, arg_placeholder, deliminator))

    for count, args in enumerate(argv):
        if (count > 0):
            print("{}: {}".format(count, args))
