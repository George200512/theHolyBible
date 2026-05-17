# Author: Ofori George
# Commencement Date: Saturday 20 September, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

"""
A script that contains the frequently used functions for easy accessibility 
"""

import json
from pathlib import Path
import threading 
from bs4 import Tag, NavigableString

SETTINGS_PATH = Path(__file__).parent / "settings.json"
lock = threading.Lock()

CANONICAL_BOOKS = {
    "GEN", "EXO", "LEV", "NUM", "DEU",
    "JOS", "JDG", "RUT",
    "1SA", "2SA", "1KI", "2KI",
    "1CH", "2CH", "EZR", "NEH", "EST",
    "JOB", "PSA", "PRO", "ECC", "SNG",
    "ISA", "JER", "LAM", "EZK", "DAN",
    "HOS", "JOL", "AMO", "OBA", "JON",
    "MIC", "NAM", "HAB", "ZEP", "HAG",
    "ZEC", "MAL",
    "MAT", "MRK", "LUK", "JHN", "ACT",
    "ROM", "1CO", "2CO", "GAL", "EPH",
    "PHP", "COL", "1TH", "2TH",
    "1TI", "2TI", "TIT", "PHM",
    "HEB", "JAS", "1PE", "2PE",
    "1JN", "2JN", "3JN", "JUD", "REV"
}

def create_verse_table_if_not_exists(conn):
    """Create the verse table in the database if it is not present"""

    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS verses (
            id INTEGER PRIMARY KEY,
            text TEXT,
            chapter_no INTEGER,
            verse_no INTEGER,
            book TEXT,
            favorite INTEGER DEFAULT 0,
            UNIQUE(chapter_no, verse_no, book)
            );
            """
    )
    conn.commit()
    
# Get content of the settings.json file
def get_settings():
    """Retrieve the content of the settings.json file and it is a dictionary"""
    with lock:
        with open(SETTINGS_PATH, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            return data.copy()
    
# Define a function to get the book name based on the number of the book                
def get_book(number):
  """Return the name of the book of the bible based on the number
  number:the number of the book in the bible (Int)
  RETURNS:string
  """
   
  data = get_settings()
  return data["BOOKS"][number - 1]["name"]
  
# Get the version of the name of a bible in the database """
def version(name:str)->str:
     """Get the version of the valid name of a bible in a database
     name(string):A valid name in the database representing a bible
     RETURN:string
     """
     
     bible = get_settings()["DATABASES"].get(name)
     if bible is None:
         raise ValueError("Name not found in database")
     return bible["version"]

 # Get the language of the name of a bible in the database """
def language(name:str)->str:
     """Get the language of the valid name of a bible in a database
     name(string):A valid name in the database representing a bible
     RETURN:string
     """
     
     bible = get_settings()["DATABASES"].get(name)
     if bible is None:
         raise ValueError("Name not found in database")
     return bible["language"]
     
#A function to set or change values in the settings file
def set_settings(key, value):
       """
       Change or set the value of a key in the settings file.
       key(str): the key of the value you want to change or set.
       value(dict): the new value of the key.
       RETURNS: None.
       """
       
       with lock:      
           settings = get_settings() 
           with open(SETTINGS_PATH, mode="w", encoding="utf-8") as file:
               settings[key] = value
               json.dump(settings, file, indent=4)
               
def extract_verse_text(verse_node:Tag)->str:
    """Extract the verse text from an HTML beautiful soup object""" 
    
    verse_node = verse_node.next_sibling
    text_parts = []
    while verse_node is not None:
        if isinstance(verse_node, Tag) and "v" in verse_node.get("class", []):
            break
        elif isinstance(verse_node, Tag):
            text_parts.append(verse_node.get_text(" ", strip=True))
        elif isinstance(verse_node, NavigableString):
            text_parts.append(verse_node.strip())
        verse_node = verse_node.next_sibling
    return " ".join(text_parts)
                   
       
if __name__ == "__main__":
    pass