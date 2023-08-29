#!/usr/bin/python3

"""
    list_division - divide elements by elements of 2 lists
    @my_list_1: first list
    @my_list_2: second list
    @list_length: length of new list
    return: new list with all divisions
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    if my_list_1 is not None and my_list_2 is not None and list_length > 0:

        for item in range(list_length):
            try:
                result = my_list_1[item] / my_list_2[item]
                new_list.append(result)

                if my_list_2[item] == 0:
                    raise ZeroDivisionError

            except ZeroDivisionError as error:
                print("division by 0")
                new_list.append(0)

            except TypeError:
                print("wrong type")
                new_list.append(0)

            except IndexError:
                print("out of range")
                new_list.append(0)

            finally:
                pass
        return new_list
