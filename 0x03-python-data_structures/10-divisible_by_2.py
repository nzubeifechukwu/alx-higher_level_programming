#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''checks if list elements are divisible by 2

    Arg:
        my_list: list

    Returns:
        list of Trues & Falses depending on if elems in my_list are divis by 2
    '''
    return [n % 2 == 0 for n in my_list]
