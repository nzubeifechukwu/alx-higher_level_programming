#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number"""
    if number < 0:
        number = -number
    last_digit = number % 10
    print(last_digit, end='')
    return last_digit
