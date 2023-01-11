#!/usr/bin/python3
'''This module adds all arguments to a Python list and saves them to a file
'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    arguments = load_from_json_file(filename)
except FileNotFoundError:
    arguments = []

# for each time this module is run with command line arguments,
# append the arguments to the existing arguments list.
# Then create new JSON representation of the updated arguments list
# and save it in filename
for arg in sys.argv[1:]:
    arguments.append(arg)

save_to_json_file(arguments, filename)
