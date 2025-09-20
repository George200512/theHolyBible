# Author: Ofori George
# Commencement Date: Saturday 20 September, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

import pathlib
import sys
from collections import UserList

# Get the absolute path of the script
script_dir = pathlib.Path(__file__).parent
# Move up two directories.
parent_dir = script_dir.parents[0]
# Add the parent directory to sys.path
sys.path.append(str(parent_dir))

"""
A script that holds  the book and book array class
"""

# Define a class to represent a book in bible
class Book(UserList):
    pass