#!/usr/bin/python3
'''A function that reads a text file (UTF-8) and prints it to stdout
'''


def read_file(filename=''):
    '''Reads a text file and prints it to stdout

    Args:
        filename: name of the text file
    '''
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
    print(read_data, end='')
