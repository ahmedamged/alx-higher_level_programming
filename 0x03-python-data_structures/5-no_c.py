#!/usr/bin/python3


def no_c(my_string):
    capitalCounts = my_string.count('C')
    counts = my_string.count('c')
    my_string = list(my_string)
    while (counts):
        my_string.remove('c')
        counts -= 1
    while (capitalCounts):
        my_string.remove('C')
        capitalCounts -= 1
    my_string = ''.join(my_string)
    return my_string
