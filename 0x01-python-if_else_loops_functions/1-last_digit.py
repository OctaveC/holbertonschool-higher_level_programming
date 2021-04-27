#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = abs(number) % 10
else:
    last = number % 10

print("Last digit of", end=" ")
if last > 5:
    print("{} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("{} is {} and is 0".format(number, last))
else:
    print("{} is {} and is less than 6 and not 0".format(number, last))
