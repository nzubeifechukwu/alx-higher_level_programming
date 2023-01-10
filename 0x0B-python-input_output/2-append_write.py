#!/usr/bin/python3
'''The following function appends a string at the end of a text file (UTF-8)
    and returns the number of characters appended
'''


def append_write(filename='', text=''):
    '''Appends a string at the end of a text file

    Args:
        filename: name of the file to append to
        text: string to append

    Returns:
       number of characters appended 
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        bytes_written = f.write(text)

    return bytes_written
