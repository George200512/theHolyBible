# Author: Ofori George
# Commencement Date: Sunday September 21st, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

import pathlib
import sys
import unittest
import sqlite3

# Get the absolute path of the script
script_dir = pathlib.Path(__file__).parent
# Move up two directories.
parent_dir = script_dir.parents[0]
# Add the parent directory to sys.path
sys.path.append(str(parent_dir))

from verses import verse
from verses import test
from books.book import Book
from chapters.chapter import Chapter, ChapterArray 
import utils


"""A script for testing vital methods of the book"""


# A TestBook class
class TestBook(test.TestBase):
    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn)
        verse_list = [
            (self.conn, "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham.", 40, 1, 1),
    (self.conn, "Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers,", 40, 1, 2),
    (self.conn, "and Judah the father of Perez and Zerah by Tamar, and Perez the father of Hezron, and Hezron the father of Ram,", 40, 1, 3),
    (self.conn, "and Ram the father of Amminadab, and Amminadab the father of Nahshon, and Nahshon the father of Salmon,", 40, 1, 4),
    (self.conn, "and Salmon the father of Boaz by Rahab, and Boaz the father of Obed by Ruth, and Obed the father of Jesse,", 40, 1, 5),
    (self.conn, "Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the East came to Jerusalem,", 40, 2, 1),
    (self.conn, "saying, \"Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him.\"", 40, 2, 2),
    (self.conn, "When Herod the king heard this, he was troubled, and all Jerusalem with him;", 40, 2, 3),
    (self.conn, "and assembling all the chief priests and scribes of the people, he inquired of them where the Christ was to be born.", 40, 2, 4),
    (self.conn, "They told him, \"In Bethlehem of Judea, for so it is written by the prophet:", 40, 2, 5),
]
    
        verse_array = list(
            map(
                lambda data: verse.Verse(data[0], data[1], data[2], data[3], data[4]),
                verse_list,
            )
        )
        self.book = Book(self.conn, 40)
        

    def tearDown(self):
        """Delete verse table from database"""

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM verses;")
        
    def test__get__item(self):
        """Check if the right objects are return if it is indexed the right way."""
        
        self.assertEqual(str(self.book[1]), f"{utils.get_book(40)} 1:1-{len(self.book[1])}")
        self.assertEqual(str(self.book[:2]), "[<ChapterArray:2>]")

    def test_head(self):
        """Test if the the first number verses of a chapter is returned as expected"""
        
        #self.assertEqual(len(self.book.head(2)), 2)
#        self.assertEqual(len(self.book.head(6)), 5)
#        self.assertEqual(len(self.book.head(5)), 5)
#        
    def test_tail(self):
        """Test if the last number of verses a chapter is returned correctly"""
        
        #self.assertEqual(len(self.book.tail(2)), 2)
#        self.assertEqual(len(self.book.tail(6)), 5)
#        self.assertEqual(len(self.book.tail(5)), 5)
        
    def test_chapter(self):
        """Test if the verse method returns the right verse number"""
        
        #self.assertEqual(str(self.book.chapter(1)), f"{utils.get_book(40)} 1:1-{len(self.book[1])}")
#        self.assertIsNone(self.book.chapter(6), f"{utils.get_book(40)} 1:1-{len(self.book[1])}")
        
    def test_chapters(self):
        """Test if the right verses are generated"""
        
        #chapter_array = self.book.chapters(1, 2)
#        self.assertEqual(list(str(v) for v in chapter_array), [f"{utils.get_book(40)} 1:1-{len(self.book[1])}",  f"{utils.get_book(40)} 1:1-{len(self.book[2])}"])
#        verse_array = self.chapter.verses(1, 2, 2)
#        self.assertEqual(list(str(v) for v in chapter_array), [f"{utils.get_book(40)} 1:1-{len(self.book[1])}"])
        

#Define the test case class to handle ChapterArray test suite
class TestChapterArray(test.TestBase):
    """The test case for ChapterArray class"""
    
    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn) 
        verse_list = [
    (self.conn, "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham.", 40, 1, 1),
    (self.conn, "Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers,", 40, 1, 2),
    (self.conn, "and Judah the father of Perez and Zerah by Tamar, and Perez the father of Hezron, and Hezron the father of Ram,", 40, 1, 3),
    (self.conn, "and Ram the father of Amminadab, and Amminadab the father of Nahshon, and Nahshon the father of Salmon,", 40, 1, 4),
    (self.conn, "and Salmon the father of Boaz by Rahab, and Boaz the father of Obed by Ruth, and Obed the father of Jesse,", 40, 1, 5),

    (self.conn, "Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the East came to Jerusalem,", 40, 2, 1),
    (self.conn, "saying, \"Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him.\"", 40, 2, 2),
    (self.conn, "When Herod the king heard this, he was troubled, and all Jerusalem with him;", 40, 2, 3),
    (self.conn, "and assembling all the chief priests and scribes of the people, he inquired of them where the Christ was to be born.", 40, 2, 4),
    (self.conn, "They told him, \"In Bethlehem of Judea, for so it is written by the prophet:", 40, 2, 5),
]

        verse_array = list(
            map(
                lambda data: verse.Verse(data[0], data[1], data[2], data[3], data[4]),
                verse_list,
            )
        )
        self.chapter_array = [Chapter(self.conn, 31, 1)] * 5
        self.chapter_array = ChapterArray(self.chapter_array)
        
    def tearDown(self):
        """Delete verse table from database"""

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM verses;")
        
    def test__str__(self):
        """Test if the string representation of the class works as expected"""
        
        self.assertEqual(str(self.chapter_array), "[<ChapterArray:5>]")
        
    def test__iter__(self):
        """Tests if the iterator dunder methods works well"""
        
        for chapter in self.chapter_array:
            self.assertIsInstance(chapter, Chapter)
            
    def test__getitem__(self):
        """Test if it gives the right item when indexed especially when slice is used."""
        
        self.assertEqual(type(self.chapter_array[0]), Chapter)
        self.assertEqual(type(self.chapter_array[:3]), ChapterArray)
    
if __name__ == "__main__":
    unittest.main()
    