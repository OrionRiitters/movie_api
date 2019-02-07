from python import omdb_request, tomatoes_request
import json



def combine_dictionaries(tomatoes_url, omdb_url):
    omdb_raw = omdb_request.omdb_get(omdb_url)
    omdb_dict = omdb_request.condense_response(omdb_raw)
    tom_dict = tomatoes_request.scrape_scores(tomatoes_url)

    omdb_dict.update(tom_dict)
    return str(json.dumps(omdb_dict))

#print(combine_dictionaries('https://www.rottentomatoes.com/m/matrix', 'http://www.omdbapi.com/?apikey=c346dee9&t=the+matrix'))
