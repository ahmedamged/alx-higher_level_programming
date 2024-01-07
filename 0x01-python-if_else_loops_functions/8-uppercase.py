#!/usr/bin/python3


def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            charunicode = ord(str[i])-32
        else:
            charunicode = ord(str[i])
        print("{:c}".format(charunicode), end='')
    print("")
