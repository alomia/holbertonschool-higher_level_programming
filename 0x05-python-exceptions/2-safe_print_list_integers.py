#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        nb = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                nb += 1
        print("")
    except (IndexError, TypeError):
        x = 0
        for i in my_list:
            x += 1
        print("")
    return nb
