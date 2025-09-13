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
import json

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

# Get content of the settings.json file
def get_settings():
    """Retrieve the content of the settings.json file and it it a dictionary"""
    
    with open(
        "../settings.json", 
        mode="r", 
        encoding="utf-8"
    ) as file:
        data = json.load(file)
        return data 

# Create a Chapter class for a single chapter
class Chapter(UserList):
    """A chapter class for a single chapter"""
    
    def __init__(self, connection, book, chapter_no):
        """Initialise the arguments passed to thee constructor """
        
        self.conn = connection
        self.cursor = self.conn.cursor()
        self.book = book 
        self.chapter = chapter_no
        self.verse_array = self.get_all_verse_in_the_chapter()
        super().__init__(self.verse_array)
        
    def get_all_verse_in_the_chapter(self):
        """Retrieve all verse with that chapter and book number from database """
        
        self.cursor.execute(
        """
        SELECT text, chapter_no, book, verse_no FROM verses WHERE 
        book=? AND chapter_no=?
        """, (self.book, self.chapter)
        )
        rows = self.cursor.fetchall()
        verse_array = map(lambda data:verses.verse.Verse(
        self.conn, text=data[0], chapter_no=data[1], book=data[2], verse_no=data[3]), rows
        )
        verse_array = list(verse_array)
        return verses.verse.VerseArray(verse_array)
                
    def __str__(self):
        """A string representation of of the chapter class """
        
        data = get_settings()
        book = data["BOOKS"][self.book - 1]
        return f"{book} {self.chapter}:1-{len(self.verse_array)}"
        
    def __repr__(self):
        """A representation of the class for instantiating"""
        
        return f"Chapter(connection={self.conn}, book={self.book}, chapter_no={self.chapter})"
        
    def __iter__(self):
        """A dunder method that gets called when the array is being iterated over"""
        
        for verse in self.verse_array:
            yield verse
            
    def __getitem__(self, index):
            """Get the verse or verses of a Chapter based on the index
            NB:This index should be used like the normal indexing style
            it should start from 1 not zero.Index or slice less than zero is an error"""
            
            if isinstance(index, int):
                if (index < 1 ) or index > (len(self.verse_array)):
                    raise verse.exceptions.VerseNotFound('Verse number not found')
                return self.verse_array[index-1]
            elif isinstance(index, slice):
                start = index.start
                stop = index.stop
                step = index.step
                if start is not None:
                    if (start < 1 ) or start > (len(self.verse_array)):
                        raise verse.exceptions.VerseNotFound('Verse number not found')
                else:
                    start = 1
                    
                if stop is not None:
                    if (stop < 1 ) or stop > (len(self.verse_array)):
                        raise verse.exceptions.VerseNotFound('Verse number not found')
                    
                if step is not None:
                    if (step< 1 ) or step > (len(self.verse_array)):
                        raise verse.exceptions.VerseNotFound('Verse number not found')
                else:
                 return self.verse_array[start - 1:stop:step]
            else:
                return self.data[index]
                
    def head(self, quantity=5):
            """Get the first five verses of a chapter is it is more than five or all verses
            quantity:the number of verses to return.Default is 5.
            Returns:VerseArray
            """
            
            if quantity > len(self.data):
                return self.data[:]
            if len(self.data) <= quantity:
                return self.data[:]
            return self.data[: quantity]