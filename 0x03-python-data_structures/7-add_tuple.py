#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''adds two tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        (x, y) where x & y are sums of corresponding elems in given tuples
    '''
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
