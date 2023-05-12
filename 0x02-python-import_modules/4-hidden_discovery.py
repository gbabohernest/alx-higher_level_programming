#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    str = "__"
    for name in dir(hidden_4):
        if (str not in name):
            print("{}".format(name))
