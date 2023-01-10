#!/usr/bin/python3
'''The following function returns an object (Python data structure)
    represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''Returns an object represented by a JSON string

    Args:
        my_str: JSON string

    Returns:
        Object represented by JSON string
    '''
    return json.loads(my_str)
