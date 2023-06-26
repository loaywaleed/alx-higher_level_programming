#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for el in range(list_length):
        try:
            new_el = my_list_1[el] / my_list_2[el]
        except (ValueError, TypeError):
            new_el = 0
            print("wrong type")
        except ZeroDivisionError:
            new_el = 0
            print("division by 0")
            pass
        except IndexError:
            new_el = 0
            print("out of range")
        finally:
            new_list.append(new_el)
    return new_list
