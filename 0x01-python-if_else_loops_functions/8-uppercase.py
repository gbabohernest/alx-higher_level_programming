#!/usr/bin/python3

def uppercase(str):
    for single_char in str:
        if ord(single_char) >=97 and ord(single_char) <= 122:
            print("{}".format(chr(ord(single_char) - 32)), end="")
        else:
            print("{}".format(single_char), end="")
    print()
