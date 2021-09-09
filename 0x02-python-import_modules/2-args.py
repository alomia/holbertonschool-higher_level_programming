#!/usr/bin/python3
from sys import argv

strCount = len(argv)

if strCount < 2:
    print('{} {}'.format(strCount - 1, "argument."))
else:
    print('{} {}'.format(strCount - 1, "argument:"))
    for i in range(1, strCount):
        print('{}: {}'.format(i, argv[i]))
