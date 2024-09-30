#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0
    for i in my_list:
        y += 1
    try:
        for j in range(0, x):
            print(my_list[j], end="")
        print()
    except IndexError:
        if x > y:
            print()
            return y
    return x
