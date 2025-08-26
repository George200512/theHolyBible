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

PATH = "../test.db"

"""A script for testing vital methods of the chapter"""


# A TestChapter class
class TestChapter(TestBase):
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
        
        pass
        
if __name__ == "__main__":
    unittest.main()