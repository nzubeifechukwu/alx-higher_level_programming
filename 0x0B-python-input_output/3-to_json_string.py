#!/usr/bin/python3
'''The following function returns the JSON representation of a string object
'''
import json


def to_json_string(my_obj):
    '''Represents a string object in JSON

    Args:
        my_obj: string object

    Returns: JSON representation of the string
    '''
    return json.dumps(my_obj)
