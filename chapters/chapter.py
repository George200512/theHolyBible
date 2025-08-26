# Author: Ofori George
# Commencement Date: Tuesday 26 August, 2025.
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

import verses

"""
This script creates the chapter class and also chapter array class 
for a group of chapters.
"""

# Create a Chapter class for a single chapter
class Chapter(UserList):
    """A chapter class for a single chapter"""
    
    def __init__(self, connection, book, chapter_no):
        """Initialise the arguments passed to thee constructor """
        
        self.conn = connection
        self.cursor = self.conn.cursor()
        self.book = book 
        self.chapter = chapter_no
        self.verse_array = get_all_verse_in_the_chapter()
        super()__init__(self.verse_array)
        
    def get_all_verse_in_the_chapter(self):
        """Retrieve all verse with that chapter and book number from database """
        
        self.cursor.execute(
        """
        SELECT (text, chapter_no, verse_no, book) FROM verses WHERE 
        book=? AND chapter_no=?
        """, (self.book, self.chapter)
        )
        rows = self.cursor.fetchall()
        verse_array = map(rows, lambda data:verses.Verse(
        self.conn, data[0], data[1], data[2], data[3])
        )
        verse_array = list(verse_array)
        return verses.VerseArray(VerseArray)
        
    def __str__(self):
        """A string representation of of the chapter class """
        
        return f"{self.book} {self.chapter}:1-{len(self.verse_array)}"
        
    def __repr__(self):
        """A representation of the class for instantiating"""
        
        return f"Chapter(connection={self.conn}, book={self.book}, chapter_no={self.chapter})"
        
    def __iter__(self):
        """A dunder method that gets called when the array is being iterated over"""
        
        for verse in self.verse_array:
            yield verse
            
sys.path.remove(str(parent_dir))