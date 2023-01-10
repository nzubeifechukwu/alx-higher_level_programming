#!/usr/bin/python3
'''The function below creates an object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''Creates an object from a JSON file

    Args:
        filename: name of JSON file
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
