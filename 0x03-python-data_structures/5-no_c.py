#!/usr/bin/python3
def no_c(my_string):
    string = ""
    if my_string is None:
        return None
    else:
        for i in my_string:
            if i == "c" or i == "C":
                continue
            string += i
    return string
