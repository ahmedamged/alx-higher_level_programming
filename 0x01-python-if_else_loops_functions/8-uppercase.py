#!/usr/bin/python3


def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 123):
            print("{:c}".format(ord(str[i])-32), end='')
            if (i == len(str)-1):
                print("")
        else:
            print("{:c}".format(ord(str[i])), end='')
            if (i == len(str)-1):
                print("")
