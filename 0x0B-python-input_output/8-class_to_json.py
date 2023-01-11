#!/usr/bin/python3
'''The class_to_json function returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
'''


def class_to_json(obj):
    '''See module description above

    Args:
        obj: the object to serialize

    Returns:
        Dictionary description of the serialized object
    '''
    obj_desc = {}

    for attr in dir(obj):
        if not attr.startswith('__'):
            if type(getattr(obj, attr)) in [list, dict, str, int, bool]:
                obj_desc[attr] = getattr(obj, attr)

    return obj_desc
