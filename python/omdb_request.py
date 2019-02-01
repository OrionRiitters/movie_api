"""This script takes a url from OMDB and converts the GET json into a dictionary."""

import requests
import json
import tomatoes_request


def omdb_get(*args):
    get_res = requests.get('http://www.omdbapi.com/?apikey=c346dee9&y=1999&t=matrix')
    json_res = get_res.text
    return json.loads(json_res)
omdb_get()

def condense_response(json_res):
    dict_condensed = {
        'Title': '',
        'Year': '',
        'Rated': '',
        'Released': '',
        'Runtime': '',
        'Genre': '',
        'Director': '',
        'Writer': '',
        'Actors': '',
        'Plot': '',
        'Production': '',
        'Type': ''
    }

# TODO I receive a syntax error when trying to turn this into a list comprehension.
    for key in json_res.keys():
        if key in dict_condensed:
            dict_condensed[key] = json_res[key]

    return dict_condensed
