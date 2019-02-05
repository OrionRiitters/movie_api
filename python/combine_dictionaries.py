from omdb_request import omdb_get, condense_response
from tomatoes_request import scrape_scores

def combine_dictionaries(tomatoes_url, omdb_url):
    omdb_raw = omdb_get(omdb_url)
    omdb_dict = condense_response(omdb_raw)
    tom_dict = scrape_scores(tomatoes_url)

    omdb_dict.update(tom_dict)
    return omdb_dict

#print(combine_dictionaries('https://www.rottentomatoes.com/m/matrix', 'http://www.omdbapi.com/?apikey=c346dee9&t=the+matrix'))
