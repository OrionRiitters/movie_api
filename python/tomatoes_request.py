"""This script takes a URL from Rotten Tomatoes and writes its HTML contents to a file."""

#TODO Instead of taking a static URL below, this script must take a url from another part
# of the application.



import requests
import os
import re
from file_access import access_file
from bs4 import BeautifulSoup
from time import time


#TODO Error handling for requests.get(), put this into a function.

clock = time()

request_url = "https://www.rottentomatoes.com/m/the_matrix"
get_request = requests.get(request_url)
html_text = get_request.text

soup = BeautifulSoup(html_text, 'html.parser')
json_block = str(soup.find_all(type='application/ld+json'))
re_split = re.compile(r'"ratingValue":.*?,')
tomatometer = (re_split.findall(json_block)[0]).lstrip('"ratingValue:').rstrip(',') + '%'

audience_score = soup.find(class_='superPageFontColor', style='vertical-align:top').string

output_dict = {
    'tomatometer': tomatometer,
    'audience_score': audience_score
}

print(output_dict)

new_clock = time() - clock

print(new_clock)

#
# This ain't it 
#
#write_file = "tmp_tomatoes_file.txt"
#
#if os.path.exists(write_file):
#    os.remove("tmp_tomatoes_file.txt")
#else:
#    print(f'"{write_file}" does not exist..\nWriting new "{write_file}"..')
#
#f = open(write_file, 'xt')
#f.write(html_text)
#
#
#TODO Just consolidate this with html_parser
#
