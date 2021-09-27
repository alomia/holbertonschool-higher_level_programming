def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(0, x):
            if type(my_list[i]) == type(1):
                print("{:d}".format(my_list[i]), end="")
        print("")
    except IndexError:
        x = 0
        for i in my_list:
            x += 1
        print("")
    return x
