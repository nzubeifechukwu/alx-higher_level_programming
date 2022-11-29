#!/usr/bin/python3
# 97 to 122 is the integer equivalents of a to z in ASCII
for i in range(97, 123):
    # chr gives the ASCII char equivalent of a number
    print('{}'.format(chr(i)), end='')
