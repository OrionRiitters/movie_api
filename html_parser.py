from bs4 import BeautifulSoup
from platform import uname
import re

directory_prefix = '/'

if uname()[0] == 'Windows':
    directory_prefix = '\\'

# This function creates a path to a specified file
def access_file(*args):
    file_path = ''
    for arg in args:
        file_path += directory_prefix + arg
    return(file_path.lstrip(directory_prefix))

# Create soup from file
file_read = open(access_file('sample_html_files', 'the_grinch.html'), 'r')
soup = BeautifulSoup(file_read, 'html.parser')

# Parse csv block found in soup using regex to find & format tomatometer score
csv_block = str(soup.find_all(type='application/ld+json'))
re_split = re.compile(r'"ratingValue":.*?,')
tomatometer = (re_split.findall(csv_block)[0]).lstrip('"ratingValue:').rstrip(',') + '%'

# Use that beautiful and delicious soup to find the audience score
audience_score = soup.find(class_='superPageFontColor', style='vertical-align:top').string

# Dictionary containing relevant information from page.
output_dict = {
    'tomatometer': tomatometer,
    'audience_score': audience_score
}




