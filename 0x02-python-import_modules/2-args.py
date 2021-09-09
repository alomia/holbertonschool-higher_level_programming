#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg1, arg2 = 's', ':'
    strCount = (len(argv)) - 1
    if strCount == 0:
        arg2 = '.'
    if strCount == 1:
        arg1 = ""
    print('{} argument{}{}'.format(strCount, arg1, arg2))
    for i in range(1, strCount + 1):
        print('{}: {}'.format(i, argv[i]))
