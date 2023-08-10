#!/usr/bin/python3

for num in range(0, 99):
    print("{:02d}".format(num), end=", " if num < 98 else ', {}\n'.format(99))
