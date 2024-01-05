#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])

print(f"Last digit of {number:d} is {lastdigit:d} and is ", end="")
if lastdigit > 5:
    print("greater than 5")
elif lastdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")