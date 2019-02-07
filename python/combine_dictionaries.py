from python import omdb_request, tomatoes_request
import json



def combine_dictionaries(tomatoes_url, omdb_url):
    omdb_raw = omdb_request.omdb_get(omdb_url)
    omdb_dict = omdb_request.condense_response(omdb_raw)

    return str(json.dumps(omdb_dict))
