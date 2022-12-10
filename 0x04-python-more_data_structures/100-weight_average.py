#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Computes weighted average of list of tuples of the form (score, weight)

    Arg:
        my_list: list of tuples

    Return:
        weighted average or 0 if list is empty
    '''
    num = 0
    den = 0

    if my_list == []:
        return 0

    for tup in my_list:
        num = num + (tup[0] * tup[1])
        den = den + tup[1]

    return (num / den)
