#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    strCount = (len(argv)) - 1

    print('{} argument{}{}'
        .format(strCount, "" if strCount == 1 else "s", ":" if strCount != 0 else "."))

    for i in range(1, strCount + 1):
        print('{}: {}'.format(i, argv[i]))
