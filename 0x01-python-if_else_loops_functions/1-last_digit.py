#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number_abs = -1 * number
    last_dig = -1 * (number_abs % 10)
else:
    last_dig = number % 10

print("Last digit of", number, "is", end=" ")

if last_dig > 5:
    print(last_dig, "and is greater than 5")
elif last_dig == 0:
    print(last_dig, "and is 0")
else:
    print(last_dig, "and is less than 6 and not 0")
