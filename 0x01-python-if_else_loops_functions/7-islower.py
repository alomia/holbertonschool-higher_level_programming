#!/usr/bin/python3

c = 'b'

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        print('{} is lower'.format(c))
    else:
        print('{} is upper'.format(c))

islower(c)