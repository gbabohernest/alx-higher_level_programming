#!/usr/bin/python3

from sys import argv, exit

def my_calculator():

    from calculator_1 import add, sub, mul, div

    valid_operations = {"+": add, "-": sub, "*": mul, "/": div}
    arg_count = len(argv) - 1

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if (operator not in valid_operations):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        result = valid_operations[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    my_calculator()
