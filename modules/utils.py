# utils.py in the modules package
import os
import sys
import json
import logging

def get_base_path():
    '''Function to get the base path of the project.'''
    if getattr(sys, 'frozen', False):
        # Running in a bundle (compiled binary)
        return os.path.dirname(sys.executable)
    else:
        # Running in a normal Python environment
        return os.path.dirname(os.path.abspath(__file__))

def setup_logging(level=logging.INFO):
    '''Set up basic logging configuration.'''
    logging.basicConfig(level=level)

def read_json_file(file_path):
    '''Read and return the content of a JSON file.'''
    with open(file_path, 'r') as file:
        return json.load(file)
