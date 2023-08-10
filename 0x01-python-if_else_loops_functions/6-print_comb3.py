#!/usr/bin/python3

for first_num in range(0, 10):
    for second_num in range(first_num+1, 10):
        print("{}{}".format(first_num, second_num), end="")
        if first_num < 8:
            print(", ", end="")
print()
