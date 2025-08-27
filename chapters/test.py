# Author: Ofori George
# Commencement Date: Tuesday 26 August, 2025.
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

import verses
from verses import test
from chapters.chapter import Chapter 


"""A script for testing vital methods of the chapter"""


# A TestChapter class
class TestChapter(test.TestBase):
    def setUp(self):
        """create verse table in database """
        
        verses.verse.create_verse_table_if_not_exists(self.conn)
        
    def tearDown(self):
        """Delete verse table from database """
        
        cursor = self.conn.cursor()
        cursor.execute(
        "DELETE FROM verses;"
        )
        
    def test_get_all_verse_in_the_chapter(self):
        """Test if the method responsible for getting all chapers of
        a verse is working correctly"""
        
        verse_1 = verses.verse.Verse(
        self.conn, 
        text="And he will turn the hearts of fathers to their children and the hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.\”",
        chapter_no=4,
        verse_no=6,
        book="Malachi"
        )
        verse_2 = verses.verse.Verse(
            self.conn, text="And Jesus wept.", book="John", verse_no=31, chapter_no=10
        )  
        verse_3 = verses.verse.Verse(
        self.conn,
        text="For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
        book="John",
        chapter_no=3,
        verse_no=16
        )
        chapter = Chapter(
            self.conn,
            book="John",
            chapter_no=3
        )
        self.assertIsInstance(chapter.verse_array, verses.verse.VerseArray)
        
    def test__get__item(self):
        verse_list = []
        
if __name__ == "__main__":
    unittest.main()