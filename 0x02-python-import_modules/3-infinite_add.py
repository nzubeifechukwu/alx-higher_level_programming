#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum_av = 0
    for i in range(1, len(argv)):
        sum_av = sum_av + int(argv[i])
    print(sum_av)
