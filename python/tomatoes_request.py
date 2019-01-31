"""This script takes a URL from Rotten Tomatoes and writes its HTML contents to a file."""

#TODO Instead of taking a static URL below, this script must take a url from another part
# of the application. 
import requests
import os

#TODO Error handling for requests.get(), put this into a function.

request_url = "https://www.rottentomatoes.com/m/the_matrix"
get_request = requests.get(request_url)
html_text = get_request.text

write_file = "tmp_tomatoes_file.txt"

if os.path.exists(write_file):
    os.remove("tmp_tomatoes_file.txt")
else:
    print(f'"{write_file}" does not exist..\nWriting new "{write_file}"..')

f = open(write_file, 'xt')
f.write(html_text)


#TODO Just consolidate this with html_parser
