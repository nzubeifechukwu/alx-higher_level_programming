#!/usr/bin/python3
'''The function below writes object to a text file using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a text file using JSON representation

    Args:
        my_obj: object to write
        filename: text file to write to
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(my_obj, f)
