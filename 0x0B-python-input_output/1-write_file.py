#!/usr/bin/python3
'''A function that writes a string to a text file (UTF-8) and returns the
    number of characters written
'''


def write_file(filename='', text=''):
    '''Writes a string to a text file

    Args:
        filename: name of text file
        text: string to write to text file

    Returns:
        Number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
