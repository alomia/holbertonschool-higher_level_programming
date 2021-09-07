#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = number % 10;
if lastnumber > 5:
    print('Last digit of {:d} is {:d} and is greater tha 5'.format(number, number % 10))
elif lastnumber == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, number % 10))
elif lastnumber < 6 and lastnumber != 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(number,number % 10))