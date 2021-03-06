""" This script can be used to access files without having to worry about the OS. """

from platform import uname

directory_prefix = '/'

if uname()[0] == 'Windows':
    directory_prefix = '\\'

""" This function creates a path to a specified file. In order, its arguments are the parent
    folder, followed by any number of children, followed by the desired file. """
def access_file(*args):
    file_path = ''
    for arg in args:
        file_path += directory_prefix + arg
    return(file_path.lstrip(directory_prefix))
