#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            k = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            k = 0
        except IndexError:
            print("out of range")
            k = 0
        except ZeroDivisionError:
            print("division by 0")
            k = 0
        finally:
            new_list.append(k)

    return new_list
