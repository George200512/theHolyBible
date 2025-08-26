# Author: Ofori George
# Commencement Date: Thursday 21 August, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/


import unittest
import sqlite3
import os

from verse import Verse, VerseArray

PATH = "../test.db"


class TestBase(unittest.TestCase):
    """A base class setup database and tear it down"""
    
    @classmethod
    def setUpClass(cls):
        """Connect to database"""
        
        cls.conn = sqlite3.connect(PATH)
        
    @classmethod
    def tearDownClass(cls):
        """Close database and delete file"""

        cls.conn.close()
        os.remove(PATH)
        
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
class TestVerse(TestBase):
    """Test the methods of the verse object"""  
    
    @classmethod
    def setUpClass(cls):
         """Create database before Test begins """
         
         super().setUpClass()
         cursor = cls.conn.cursor()
         cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS verses (
            id INTEGER PRIMARY KEY,
            text TEXT,
            chapter_no INTEGER,
            verse_no INTEGER,
            book TEXT,
            FOREIGN KEY (chapter_no) REFERENCES chapters (chapter_no)
            );
            """
        )
         cls.conn.commit()
    
    def setUp(self):
        """Clean the verses table each Test to ensure fresh IDs"""
        
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS verses (
            id INTEGER PRIMARY KEY,
            text TEXT,
            chapter_no INTEGER,
            verse_no INTEGER,
            book TEXT,
            FOREIGN KEY (chapter_no) REFERENCES chapters (chapter_no)
            );
            """
        )
        cursor.execute("DELETE FROM verses;")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='verses';")
        self.conn.commit()
        
    def test_get_id(self):
        """Test the validity of the get_id method of the verse class"""
        
        print("            test_get_id")
        verse = Verse(
            self.conn, text="And Jesus wept.", book="John", verse_no=31, chapter_no=10
        )
        self.assertEqual(verse.id, 1)

    def test_add_verse_if_not_added(self):
        """Checks if a verse is added to it appropriately"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(str(verse), "Verse 14")

    def test_create_verse_table_if_not_exists(self):
        """Check if table if created correctly"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(isinstance(verse, Verse), True)

    def test_value(self):
        """Test if my value property return the text of the verse"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.value, "The lord shall fight my fight")

    def test_chapter(self):
        """Test if the chapter property returns the right chapter number"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.chapter, 14)

    def test_book(self):
        """Test if the book property returns the right book name"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.book, "Exodus")

    def test_verse(self):
        """Test if the verse property returns the right verse number"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.verse, 14)

    def test_id(self):
        """Test if the id property returns the right id"""

        verse = Verse(
            self.conn,
            text="The lord shall fight my fight",
            book="Exodus",
            verse_no=14,
            chapter_no=14,
        )
        self.assertEqual(verse.id, 1)


# A VerseArray testCase class
class TestVerseArray(TestBase):
    """A unittest testcase class for the verse array class"""
        
    def test__init__(self):
        """Check if the VerseArray is being initialised correctly"""
        
        verse = Verse(
        self.conn, 
        text="And he will turn the hearts of fathers to their children and the hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.\”",
        chapter_no=4,
        verse_no=6,
        book="Malachi"
        )
        array = VerseArray([verse])
        self.assertEqual(str(array), "[<VerseArray:1>]")
    
if __name__ == "__main__":
    unittest.main()
