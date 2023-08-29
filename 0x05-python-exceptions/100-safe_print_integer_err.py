#!/usr/bin/python3

"""
    safe_print_integer_err - Prints an integer
    @value: any type (int, string etc)
    return: True if value has printed correctly
            otherwise false & prints in stderr
            the error preceded by Exception:
"""


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as error:
        msg = str(error)
        sys.stderr.write("Exception: " + msg + "\n")
        return False
    return True
