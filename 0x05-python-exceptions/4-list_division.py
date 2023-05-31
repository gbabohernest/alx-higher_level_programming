def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for item in range(list_length):

        try:
            new_list.append(my_list_1[item] / my_list_2[item])
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            pass
    return (new_list)
