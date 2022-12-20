#!/usr/bin/python3
def safe_print_integer(value):
    '''Prints an integer

    Arg:
        value: integer to print

    Return:
        True if value successfully printed, False otherwise
    '''
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
        return False
