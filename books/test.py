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
from books.book import Book, BookArray 
from chapters.chapter import Chapter, ChapterArray
import utils


"""A script for testing vital methods of the book"""


# A TestBook class
class TestBook(test.TestBase):
    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn)
        verse_list = [
            (
                self.conn,
                "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham.",
                40,
                1,
                1,
            ),
            (
                self.conn,
                "Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers,",
                40,
                1,
                2,
            ),
            (
                self.conn,
                "and Judah the father of Perez and Zerah by Tamar, and Perez the father of Hezron, and Hezron the father of Ram,",
                40,
                1,
                3,
            ),
            (
                self.conn,
                "and Ram the father of Amminadab, and Amminadab the father of Nahshon, and Nahshon the father of Salmon,",
                40,
                1,
                4,
            ),
            (
                self.conn,
                "and Salmon the father of Boaz by Rahab, and Boaz the father of Obed by Ruth, and Obed the father of Jesse,",
                40,
                1,
                5,
            ),
            (
                self.conn,
                "Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the East came to Jerusalem,",
                40,
                2,
                1,
            ),
            (
                self.conn,
                'saying, "Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him."',
                40,
                2,
                2,
            ),
            (
                self.conn,
                "When Herod the king heard this, he was troubled, and all Jerusalem with him;",
                40,
                2,
                3,
            ),
            (
                self.conn,
                "and assembling all the chief priests and scribes of the people, he inquired of them where the Christ was to be born.",
                40,
                2,
                4,
            ),
            (
                self.conn,
                'They told him, "In Bethlehem of Judea, for so it is written by the prophet:',
                40,
                2,
                5,
            ),
                (
        self.conn,
        "In those days John the Baptist came preaching in the wilderness of Judea,",
        40,
        3,
        1,
    ),
    (
        self.conn,
        '“Repent, for the kingdom of heaven is at hand.”',
        40,
        3,
        2,
    ),
    (
        self.conn,
        "For this is he who was spoken of by the prophet Isaiah when he said, 'The voice of one crying in the wilderness: Prepare the way of the Lord; make his paths straight.’",
        40,
        3,
        3,
    ),
    (
        self.conn,
        "Now John wore a garment of camel’s hair and a leather belt around his waist, and his food was locusts and wild honey.",
        40,
        3,
        4,
    ),
    (
        self.conn,
        "Then Jerusalem and all Judea and all the region about the Jordan were going out to him,",
        40,
        3,
        5,
    ),

    # Matthew 4
    (
        self.conn,
        "Then Jesus was led up by the Spirit into the wilderness to be tempted by the devil.",
        40,
        4,
        1,
    ),
    (
        self.conn,
        "And after fasting forty days and forty nights, he was hungry.",
        40,
        4,
        2,
    ),
    (
        self.conn,
        "And the tempter came and said to him, “If you are the Son of God, command these stones to become loaves of bread.”",
        40,
        4,
        3,
    ),
    (
        self.conn,
        "But he answered, “It is written, ‘Man shall not live by bread alone, but by every word that comes from the mouth of God.’”",
        40,
        4,
        4,
    ),
    (
        self.conn,
        "Then the devil took him to the holy city and set him on the pinnacle of the temple",
        40,
        4,
        5,
    ),

    # Matthew 5
    (
        self.conn,
        "Seeing the crowds, he went up on the mountain, and when he sat down, his disciples came to him.",
        40,
        5,
        1,
    ),
    (
        self.conn,
        "And he opened his mouth and taught them, saying:",
        40,
        5,
        2,
    ),
    (
        self.conn,
        "“Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
        40,
        5,
        3,
    ),
    (
        self.conn,
        "“Blessed are those who mourn, for they shall be comforted.",
        40,
        5,
        4,
    ),
    (
        self.conn,
        "“Blessed are the meek, for they shall inherit the earth.",
        40,
        5,
        5,
    ),
        ]

        verse_array = list(
            map(
                lambda data: verse.Verse(data[0], data[1], data[2], data[3], data[4]),
                verse_list,
            )
        )
        self.book = Book(self.conn, 40)
        self.book.number_of_chapters = 5
        self.book.chapter_array = ChapterArray([Chapter (self.conn, 40, num) for num in range(1, 6)])
        self.book.data = self.book.chapter_array

    def tearDown(self):
        """Delete verse table from database"""

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM verses;")

    def test__get__item(self):
        """Check if the right objects are return if it is indexed the right way."""

        self.assertEqual(
            str(self.book[1]), f"{utils.get_book(40)} 1:1-{len(self.book[1])}"
        )
        self.assertEqual(str(self.book[1:2]), "[<ChapterArray:2>]")

    def test_head(self):
        """Test if the the first number verses of a chapter is returned as expected"""

        self.assertEqual(len(self.book.head(2)), 2)
        self.assertEqual(len(self.book.head(6)), 5)
        self.assertEqual(len(self.book.head(5)), 5)
        
    def test_tail(self):
        """Test if the last number of verses a chapter is returned correctly"""

        self.assertEqual(len(self.book.tail(2)), 2)
        self.assertEqual(len(self.book.tail(6)), 5)
        self.assertEqual(len(self.book.tail(5)), 5)

    def test_chapter(self):
        """Test if the verse method returns the right verse number"""
        
        self.assertEqual(str(self.book.chapter(1)), f"{utils.get_book(40)} 1:1-{len(self.book[1])}")
        self.assertIsNone(self.book.chapter(6), f"{utils.get_book(40)} 1:1-{len(self.book[1])}")

    def test_chapters(self):
        """Test if the right verses are generated"""
        
        chapter_array = self.book.chapters(1, 2)
        self.assertEqual(list(str(v) for v in chapter_array), [f"{utils.get_book(40)} 1:1-{len(self.book[1])}",  f"{utils.get_book(40)} 2:1-{len(self.book[2])}"])
        chapter_array = self.book.chapters(1, 2, 2)
        self.assertEqual(list(str(v) for v in chapter_array), [f"{utils.get_book(40)} 1:1-{len(self.book[1])}"])


# Define the test case class to handle BookArray test suite
class TestBookArray(test.TestBase):
    """The test case for BookArray class"""

    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn)
        verse_list = [
            (
                self.conn,
                "The book of the genealogy of Jesus Christ, the son of David, the son of Abraham.",
                40,
                1,
                1,
            ),
            (
                self.conn,
                "Abraham was the father of Isaac, and Isaac the father of Jacob, and Jacob the father of Judah and his brothers,",
                40,
                1,
                2,
            ),
            (
                self.conn,
                "and Judah the father of Perez and Zerah by Tamar, and Perez the father of Hezron, and Hezron the father of Ram,",
                40,
                1,
                3,
            ),
            (
                self.conn,
                "and Ram the father of Amminadab, and Amminadab the father of Nahshon, and Nahshon the father of Salmon,",
                40,
                1,
                4,
            ),
            (
                self.conn,
                "and Salmon the father of Boaz by Rahab, and Boaz the father of Obed by Ruth, and Obed the father of Jesse,",
                40,
                1,
                5,
            ),
            (
                self.conn,
                "Now after Jesus was born in Bethlehem of Judea in the days of Herod the king, behold, wise men from the East came to Jerusalem,",
                40,
                2,
                1,
            ),
            (
                self.conn,
                'saying, "Where is he who has been born king of the Jews? For we saw his star when it rose and have come to worship him."',
                40,
                2,
                2,
            ),
            (
                self.conn,
                "When Herod the king heard this, he was troubled, and all Jerusalem with him;",
                40,
                2,
                3,
            ),
            (
                self.conn,
                "and assembling all the chief priests and scribes of the people, he inquired of them where the Christ was to be born.",
                40,
                2,
                4,
            ),
            (
                self.conn,
                'They told him, "In Bethlehem of Judea, for so it is written by the prophet:',
                40,
                2,
                5,
            ),
                (
        self.conn,
        "In those days John the Baptist came preaching in the wilderness of Judea,",
        40,
        3,
        1,
    ),
    (
        self.conn,
        '“Repent, for the kingdom of heaven is at hand.”',
        40,
        3,
        2,
    ),
    (
        self.conn,
        "For this is he who was spoken of by the prophet Isaiah when he said, 'The voice of one crying in the wilderness: Prepare the way of the Lord; make his paths straight.’",
        40,
        3,
        3,
    ),
    (
        self.conn,
        "Now John wore a garment of camel’s hair and a leather belt around his waist, and his food was locusts and wild honey.",
        40,
        3,
        4,
    ),
    (
        self.conn,
        "Then Jerusalem and all Judea and all the region about the Jordan were going out to him,",
        40,
        3,
        5,
    ),

    # Matthew 4
    (
        self.conn,
        "Then Jesus was led up by the Spirit into the wilderness to be tempted by the devil.",
        40,
        4,
        1,
    ),
    (
        self.conn,
        "And after fasting forty days and forty nights, he was hungry.",
        40,
        4,
        2,
    ),
    (
        self.conn,
        "And the tempter came and said to him, “If you are the Son of God, command these stones to become loaves of bread.”",
        40,
        4,
        3,
    ),
    (
        self.conn,
        "But he answered, “It is written, ‘Man shall not live by bread alone, but by every word that comes from the mouth of God.’”",
        40,
        4,
        4,
    ),
    (
        self.conn,
        "Then the devil took him to the holy city and set him on the pinnacle of the temple",
        40,
        4,
        5,
    ),

    # Matthew 5
    (
        self.conn,
        "Seeing the crowds, he went up on the mountain, and when he sat down, his disciples came to him.",
        40,
        5,
        1,
    ),
    (
        self.conn,
        "And he opened his mouth and taught them, saying:",
        40,
        5,
        2,
    ),
    (
        self.conn,
        "“Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
        40,
        5,
        3,
    ),
    (
        self.conn,
        "“Blessed are those who mourn, for they shall be comforted.",
        40,
        5,
        4,
    ),
    (
        self.conn,
        "“Blessed are the meek, for they shall inherit the earth.",
        40,
        5,
        5,
    ),
        ]

        verse_array = list(
            map(
                lambda data: verse.Verse(data[0], data[1], data[2], data[3], data[4]),
                verse_list,
            )
        )
        self.book = Book(self.conn, 40)
        self.book.number_of_chapters = 5
        self.book.chapter_array = ChapterArray([Chapter (self.conn, 40, num) for num in range(1, 6)])
        self.book.data = self.book.chapter_array
        self.book_array = BookArray([self.book] * 5)

    def tearDown(self):
        """Delete verse table from database"""

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM verses;")

    def test__str__(self):
        """Test if the string representation of the class works as expected"""

        self.assertEqual(str(self.book_array), "[<BookArray:5>]")

    def test__iter__(self):
        """Tests if the iterator dunder methods works well"""

        for book in self.book_array:
            self.assertIsInstance(book, Book)

    def test__getitem__(self):
        """Test if it gives the right item when indexed especially when slice is used."""

        self.assertEqual(type(self.book_array[0]), Book)
        self.assertEqual(type(self.book_array[:3]), BookArray)


if __name__ == "__main__":
    unittest.main()
