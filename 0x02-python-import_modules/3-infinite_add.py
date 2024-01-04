#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for i, x in enumerate(sys.argv):
            if i != 0:
                x = int(x)
                total += x
        print(str(total))
