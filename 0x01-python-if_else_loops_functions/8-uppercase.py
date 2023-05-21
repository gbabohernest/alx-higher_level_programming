#!/usr/bin/python3

def uppercase(str):
    for single_char in str:
        print("{}".format(chr(ord(single_char) - 32)
                          if (ord(single_char) >= 97
                              and ord(single_char) <= 122)
                          else single_char), end="")
    print()
