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

import utils
from chapters.chapter import Chapter, ChapterArray
from chapters.exceptions import ChapterNotFoundError 

# Define a class to represent a book in bible
class Book(UserList):
    """The book class that contains all the chapters of a book"""
    
    def __init__(self, conn, book_id):
        """Initializing routine"""
        
        self.connection = conn
        self.book_id = book_id
        self.book = utils.get_book(self.book_id)
        self.number_of_chapters = utils.get_settings()["BOOKS"][self.book_id - 1]["chapters"]
        self.chapter_array = ChapterArray(list(map(lambda num:Chapter(self.connection, self.book_id - 1, num), range(1, self.number_of_chapters + 1))))
        super().__init__(self.chapter_array)
        
    def __str__(self):
        """A string representation of the book object"""
        
        return f"{self.book}:{self.number_of_chapters}chapters"
        
    def __repr__(self):
        """A string representing how to instiate the class"""
        
        return f"Book(conn={self.connection}, book_id={self.book_id})"
        
    def __iter__(self):
        """A method that gets called automatically when the object is being iterated over"""
        
        for chapter in self.data:
            yield chapter
            
    def __getitem__(self, index):
        """Get the chapter or chapters of a book based on the index
        NB:This index should be used like the normal indexing style
        it should start from 1 not zero.Index or slice less than zero is an error"""

        if isinstance(index, int):
            if (index < 1) or index > (len(self.data)):
                raise ChapterNotFoundError("Chapter number not found")
            return self.data[index - 1]
        elif isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is not None:
                if (start < 1) or start > (len(self.data)):
                    raise ChapterNotFoundError("Chapter number not found")
            else:
                start = 1

            if stop is not None:
                if (stop < 1) or stop > (len(self.data)):
                    raise ChapterNotFoundError("Chapter number not found")

            if step is not None:
                if (step < 1) or step > (len(self.data)):
                    raise ChapterNotFoundError("Chapter number not found")
            else:
                step = 1
            return self.data[start - 1 : stop : step]
        else:
            return self.data[index]
            
    def head(self, quantity=5):
        """Get the first five chapters of a book if it is more than five or all chapters
        quantity:the number of chapters to return.Default is 5.
        Returns:ChapterArray
        """

        return self.data[:quantity]

    def tail(self, quantity=5):
        """Get the last five chapters of a book if it is more than five or all chapters
        quantity:the number of chapters to return.Default is 5.
        Returns:ChapterArray
        """
        
        return self.data[-quantity:]

    def chapter(self, number=1):
        """Get the chapter of the book by providing its number
        number:an integer representing the chapter number
        RETURNS:A chapter instance if no error occurs or none if it occurs
        """

        try:
            return self[number]
        except ChapterNotFoundError:
            return None

    def chapters(self, start=1, stop=1, step=None):
        """Get a list of chapters from the book
        start:where to start slicing the book defaults to 1
        stop:where to stop slicing the chapter defaults to 1
        step:how many steps to take before the next slice defaults to none which is equal to 1
        RETURNS:A chapter array instance
        """

        try:
            return self[start:stop:step]
        except ChapterNotFoundError:
            return ChapterArray([])
            
            
 #Define a class to hold an array of books
class BookArray(UserList):
    """The class representing the book array"""
    
    def __init__(self, array=[]):
        """Initializing routine"""
        
        self.array = array
        if not isinstance(self.array, (tuple, list)):
            raise ValueError("Value must be a list or a tuple.")
        super().__init__(self.array)
        
    def __str__(self):
        """A string representation of the array"""
        
        return f"[<BookArray:{len(self.array)}>]" 
        
    def __repr__(self):
        """A string representing how an object is to be created"""
        
        return f"BookArray(array={self.array})"
        
    def __iter__(self):
        """A dunder method that gets called when an array is being iterated over"""
        
        for data in self.array:
            yield data
            
    def __getitem__(self, index):
        """Get the item in an array based on its index.
        index:the index(integer) of the item or slice.
        return: A book{ instance.
        """
        
        if isinstance(index, slice):
            sub_array = self.array[index]
            return BookArray(sub_array)
        return self.data[index]
            
            