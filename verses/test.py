# Author: Ofori George
# Commencement Date: Thursday 21 August, 2025.
# Telephone / WhatsApp: 0504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/


import unittest
import sqlite3
import os

from verse import Verse, VerseArray

PATH = "../test.db"

conn = sqlite3.connect(PATH)


class TestVerse(unittest.TestCase):
    """Test the methods of the verse object"""

    @classmethod
    def tearDownClass(cls):
        """Close database and delete file"""

        conn.close()
        os.remove(PATH)

    def test_get_id(self):
        """Test the validity of the get_id method of the verse class"""

        verse = Verse(
            conn, text="And Jesus wept.", book="John", verse_no=31, chapter_no=10
        )
        self.assertEqual(verse.id, 2)

    def test_add_verse_if_not_added(self):
        """Checks if a verse is added to it appropriately"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(str(verse), "Verse 14")

    def test_create_verse_table_if_not_exists(self):
        """Check if table if created correctly"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(isinstance(verse, Verse), True)

    def test_value(self):
        """Test if my value property return the text of the verse"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.value, "The lord shall fight my fight")

    def test_chapter(self):
        """Test if the chapter property returns the right chapter number"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.chapter, 14)

    def test_book(self):
        """Test if the book property returns the right book name"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.book, "Exodus")

    def test_verse(self):
        """Test if the verse property returns the right verse number"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.verse, 14)

    def test_id(self):
        """Test if the id property returns the right id"""

        verse = Verse(
            conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.id, 1)


# A VerseArray testCase class
class TestVerseArray(unittest.TestCase):
    """A unittest testcase class for the verse array class"""
    
    pass
    
    
if __name__ == "__main__":
    unittest.main()
