#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for num in range(len(my_list)-1, 0, -1):
            for i in range(num):
                if my_list[i] > my_list[i + 1]:
                    temp = my_list[i]
                    my_list[i] = my_list[i + 1]
                    my_list[i + 1] = temp
        return my_list[-1]
