#!/usr/bin/python3
def safe_print_division(a, b):
    '''Divides one integer by another and prints the result

    Args:
        a: one integer
        b: another integer

    Return:
        result of a divided by b
    '''
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))

    return result
