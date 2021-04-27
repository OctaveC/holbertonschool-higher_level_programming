#!/usr/bin/python3
def fizzbuzz():
    for ite in range(1, 101):
        if ite % 5 == 0 and ite % 3 == 0:
            print("FizzBuzz", end=" ")
        elif ite % 3 == 0:
            print("Fizz", end=" ")
        elif ite % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(ite, end=" ")
