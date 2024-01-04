#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv)-1 == 1:
            print("{} argument:".format(len(sys.argv)-1) +
                  "\n" + "1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv)-1))
            for i, x in enumerate(sys.argv):
                if i != 0:
                    print(str(i) + ": " + x)
