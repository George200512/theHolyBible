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

from verses import verse
from verses import test
from chapters.chapter import Chapter, ChapterArray 
import utils


"""A script for testing vital methods of the chapter"""


# A TestChapter class
class TestChapter(test.TestBase):
    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn)
        verse_list = [
            (
                self.conn,
                "The vision of Obadiah.This is what the sovereign Lord says about Edom--",
                1,
                31,
                1,
            ),
            (
                self.conn,
                "We have heard a message from the Lord: An envoy was sent to the nations to say 'Rise, and let us go against her for battle'",
                1,
                31,
                2,
            ),
            (
                self.conn,
                "The pride of your heart has decieved you, you who live in the clefts of the rock and make your home on heights.",
                1,
                31,
                3,
            ),
            (
                self.conn,
                "Though you soar like the eagle and make your nests among your stars, from there I will bring you down, declares the Lord.",
                1,
                31,
                4,
            ),
            (
                self.conn,
                "If thieves come to you, if robbers in the night-- Oh what a disaster, awaits you--would they not steal only as much as the wanted'",
                1,
                31,
                5,
            ),
        ]

        verse_array = list(
            map(
                lambda data: verse.Verse(data[0], data[1], data[2], data[3], data[4]),
                verse_list,
            )
        )
        self.chapter = Chapter(self.conn, 31, 1)
        

    def tearDown(self):
        """Delete verse table from database"""

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM verses;")

    def test_get_all_verse_in_the_chapter(self):
        """Test if the method responsible for getting all chapers of
        a verse is working correctly"""

        verse_1 = verse.Verse(
            self.conn,
            text="And he will turn the hearts of fathers to their children and the hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.\”",
            chapter_no=4,
            verse_no=6,
            book=39,
        )
        verse_2 = verse.Verse(
            self.conn, text="And Jesus wept.", book="John", verse_no=31, chapter_no=10
        )
        verse_3 = verse.Verse(
            self.conn,
            text="For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
            book=43,
            chapter_no=3,
            verse_no=16,
        )
        chapter = Chapter(self.conn, book=43, chapter_no=3)
        self.assertIsInstance(chapter.verse_array, verse.VerseArray)

    def test__get__item(self):
        """Check if the right objects are return if it is indexed the right way."""
        
        self.assertEqual(str(self.chapter[1]), "Verse 1")
        self.assertEqual(str(self.chapter[:2]), "[<VerseArray:2>]")

    def test_head(self):
        """Test if the the first number verses of a chapter is returned as expected"""
        
        self.assertEqual(len(self.chapter.head(2)), 2)
        self.assertEqual(len(self.chapter.head(6)), 5)
        self.assertEqual(len(self.chapter.head(5)), 5)
        
    def test_tail(self):
        """Test if the last number of verses a chapter is returned correctly"""
        
        self.assertEqual(len(self.chapter.tail(2)), 2)
        self.assertEqual(len(self.chapter.tail(6)), 5)
        self.assertEqual(len(self.chapter.tail(5)), 5)
        
    def test_verse(self):
        """Test if the verse method returns the right verse number"""
        
        self.assertEqual(str(self.chapter.verse(1)), "Verse 1")
        self.assertIsNone(self.chapter.verse(6))
        
    def test_verses(self):
        """Test if the right verses are generated"""
        
        verse_array = self.chapter.verses(1, 3)
        self.assertEqual(list(str(v) for v in verse_array), ["Verse 1", "Verse 2", "Verse 3"])
        verse_array = self.chapter.verses(1, 5, 2)
        self.assertEqual(list(str(v) for v in verse_array), ["Verse 1", "Verse 3", "Verse 5"])
        

#Define the test case class to handle ChapterArray test suite
class TestChapterArray(test.TestBase):
    """The test case for ChapterArray class"""
    
    def setUp(self):
        """create verse table in database"""

        utils.create_verse_table_if_not_exists(self.conn)
        verse_list = [
            (
                self.conn,
                "The vision of Obadiah.This is what the sovereign Lord says about Edom--",
                1,
                31,
                1,
            ),
            (
                self.conn,
                "We have heard a message from the Lord: An envoy was sent to the nations to say 'Rise, and let us go against her for battle'",
                1,
                31,
                2,
            ),
            (
                self.conn,
                "The pride of your heart has decieved you, you who live in the clefts of the rock and make your home on heights.",
                1,
                31,
                3,
            ),
            (
                self.conn,
                "Though you soar like the eagle and make your nests among your stars, from there I will bring you down, declares the Lord.",
                1,
                31,
                4,
            ),
            (
                self.conn,
                "If thieves come to you, if robbers in the night-- Oh what a disaster, awaits you--would they not steal only as much as the wanted'",
                1,
                31,
                5,
            ),
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
