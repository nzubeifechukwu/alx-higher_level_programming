#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''Executes a function safely

    Args:
        fct: Points to the function
        *args: One or more arguments

    Returns:
        The functions return value on successful execution
        None on failure
    '''
    try:
        return fct(*args)
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
