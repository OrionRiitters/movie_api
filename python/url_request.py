"""This script takes a URL and writes its HTML contents to a file."""
#TODO Instead of taking a static URL below, this script must take a url from another part
# of the application.

import requests
from bs4 import BeautifulSoup
import os

#TODO Error handling for requests.get()
http_request = requests.get("https://www.rottentomatoes.com/m/they_shall_not_grow_old")
request_text = http_request.text

if os.path.exists("tmp_html_file.txt"):
    os.remove("tmp_html_file.txt")
else:
    print("The file does not exist")

f = open('tmp_html_file.txt', 'xt')
f.write(request_text)


