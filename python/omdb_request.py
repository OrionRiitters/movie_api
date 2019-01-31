"""This script takes a url from OMDB and converts the GET json into a dictionary."""

import requests
from file_access import access_file

def omdb_get(*args):
    
