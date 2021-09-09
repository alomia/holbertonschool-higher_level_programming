#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    strCount = len(argv) - 1
    if strCount == 0:
        print('{} {}'.format(strCount, "arguments."))
    elif strCount == 1:
        print('{} {}'.format(strCount, "argument:"))
    elif strCount > 2:
        print('{} {}'.format(strCount, "argument:"))
    else:
        print('{} {}'.format(strCount, "arguments:"))
        for i in range(1, strCount):
            print('{}: {}'.format(i, argv[i]))
