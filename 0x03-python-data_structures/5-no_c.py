#!/usr/bin/env python3
def no_c(my_string):
    str1 = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        str1 += i
    return str1
        
