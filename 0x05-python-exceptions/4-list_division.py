def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for item in range(list_length):

        try:
            dividend = my_list_1[item] 
            divisor = my_list_2[item]
            result = dividend / divisor
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            pass
    return (new_list)
