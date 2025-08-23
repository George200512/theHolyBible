import unittest
import sqlite3 
import os

from verse import Verse

path = "../test.db"

conn = sqlite3.connect(path)

class TestVerse(unittest.TestCase):
    """Test the methods of the verse object"""
     
    def test_get_id(self):
        """Test the validity of the get_id method of the verse class"""
        
        verse = Verse(conn, text="And Jesus wept.", book="John", verse_no=31, chapter_no=10) 
        self.assertEqual(verse.id, 2)
        
    def test_add_verse_if_not_added(self):
        """Checks if a verse is added to it appropriately"""
        
        verse = Verse(conn, text="The lord shall fight my fight", book="Exodus", verse_no=14, chapter_no=14)
        self.assertEqual(str(verse), "Verse 14")
        
        
if __name__ == "__main__":
    unittest.main()
    os.remove(path)
    