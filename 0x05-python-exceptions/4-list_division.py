#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''Divides two lists element by element

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of new list with division results

    Return:
        new list of length list_length holding the division results
    '''
    results = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            div = 0
            print('out of range')
        except TypeError:
            div = 0
            print('wrong type')
        except ZeroDivisionError:
            div = 0
            print('division by 0')
        finally:
            results.append(div)

    return results
