"""This script takes a URL specifying a film on Rotten Tomatoes and returns a dictionary containing two film ratings."""

import requests
import os
import re
from bs4 import BeautifulSoup


def scrape_scores(request_url):
    html_text = ''

    try:
        get_request = requests.get(request_url)
        html_text = get_request.text
    except:
        print('Unable to perform GET request on argument. Please check the URL supplied.')

    soup = BeautifulSoup(html_text, 'html.parser')
    json_block = str(soup.find_all(type='application/ld+json'))
    reg_ex = re.compile(r'"ratingValue":.*?,')

    try:
        tomatometer = (reg_ex.findall(json_block)[0]).lstrip('"ratingValue:').rstrip(',') + '%'
        audience_score = soup.find(class_='superPageFontColor', style='vertical-align:top').string

        return {
            'tomatometer': tomatometer,
            'audience_score': audience_score
        }
    except IndexError:
        print('Error parsing JSON. Either there is a problem with the URL supplied, or Rotten Tomatoes updated their HTML in a way that broke this.')

#TODO Fix error handling to correctly raise errors
