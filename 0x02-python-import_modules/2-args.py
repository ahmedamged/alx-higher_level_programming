#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
else:
    if len(sys.argv)-1 == 1:
        print("{} argument:".format(len(sys.argv)-1))
        print("1:", sys.argv[0])
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for i, x in enumerate(sys.argv):
            if i != 0: 
                print(str(i) + ": " + x)