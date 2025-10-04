# Author: Ofori George
# Commencement Date: Saturday 4 October, 2025.
# Telephone / WhatsApp: (+233)504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

"""
A script to create the bible class and the compiler class
"""
from collections import UserList
import sqlite3

from books.book import BookArray
from books import exceptions 

# Create the bible class
class Bible(UserList):
    """The bible class for getting the bible version in the specified language
    if found in database"""
    
    def __init__(self, name=None):
        """Initializing routine"""
        
        pass