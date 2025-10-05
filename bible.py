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

from books.book import BookArray, Book
from books import exceptions as exc
import utils
import exceptions as bexc

# Create the bible class
class Bible(UserList):
    """The bible class for getting the bible version in the specified language
    if found in database"""
    
    def __init__(self, name=None):
        """Initializing routine"""
        
        self.name = name
        if self. name is None:
            self. path = utils.get_settings()["DATABASES"].get("DEFAULT")
        self.path = utils. get_settings()["DATABASES"].get(name)
        if self. path is None:
            raise bexc. BibleNotAvailableError("Requested bible not available in database")
        self. connection = sqlite3. connect(self.path)
        self.nof_of_books = 66
        self. book_array = BookArray([Book(self.connection, num) for num in range(1, self.no_of_books + 1)])
        super().__int__(self. book_array)
        
    def close(self):
        """Close the database""" 
        
        self. connection. close()
        
    def __enter__(self):
        
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self. close()
        
    def __str__(self):
        """A string representation of the bible class"""
        
        version = utils. version(self.name)
        language = utils.language(self. name)
        return f"{version}({language})"
        
    def __repr__(self):
        """A string representation of how the class should be instantiated"""
        
        return f"Bible(name={self.name})"
        
    def __iter__(self):
        """An iteration method that is automatically called anytime the bible is being interested over"""
        
        return iter(self.data)
        
    def __getitem__(self, index):
        """Get the book or books of a bible     based on the index
        NB:This index should be used like the normal indexing style
        it should start from 1 not zero.Index or slice less than zero is an error"""

        if isinstance(index, int):
            if (index < 1) or index > (len(self.verse_array)):
                raise exc.BookNotFoundError("Book number not found")
            return self.book_array[index - 1]
        elif isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is not None:
                if (start < 1) or start > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")
            else:
                start = 1

            if stop is not None:
                if (stop < 1) or stop > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")

            if step is not None:
                if (step < 1) or step > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")
            else:
                step = 1
            return self.book_array[start - 1 : stop : step]
        else:
            return self.data[index]
            
    def book(self, num):
        """Get the book of the bible based on the number
        num(integer):The number of a bible
        RETURN:Book class or None
        """
        
        try :
            return self[num]
        except exc.BookNotFoundError:
            return None
            