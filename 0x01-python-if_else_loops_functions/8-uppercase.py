#!/usr/bin/python3
def uppercase(str):
    """Prints a str in uppercase"""
    for i in range(len(str)):
        islow = ord(str[i]) >= 97 and ord(str[i]) <= 122
        if islow:
            up = chr(ord(str[i]) - 32)
        if i != len(str) - 1:
            print('{}'.format(up if islow else str[i]), end='')
        else:
            print('{}'.format(up if islow else str[i]))
