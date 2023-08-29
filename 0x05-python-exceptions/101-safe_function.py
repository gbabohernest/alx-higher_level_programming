#!/usr/bin/python3

"""
    safe_function - executes a function safely
    @fct: a pointer to a function
    @*args: fun args
    return: the result of the function
"""


def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as error:
        msg = str(error)
        sys.stderr.write("Exception: " + msg + "\n")
        return None
