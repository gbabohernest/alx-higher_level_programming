#!/usr/bin/python3
for ch in range(ord('z'), ord('a') - 1, - 1):
    print("{}".format(chr(ch).lower()
                      if ch % 2 == 0
                      else chr(ch).upper()), end="")
