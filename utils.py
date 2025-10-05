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
            book INTEGER,
            favorite INTEGER DEFAULT 0,
            FOREIGN KEY (chapter_no) REFERENCES chapters (chapter_no)
            );
            """
    )
    conn.commit()
    
# Get content of the settings.json file
def get_settings():
    """Retrieve the content of the settings.json file and it is a dictionary"""
    
    settings_path = Path(__file__).parent / "settings.json"
    with open(settings_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
        return data

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
     
     bible = get_settings()[" DATABASES"].get(name)
     if bible is None:
         raise ValueError("Name not found in database")
     return bible["version"]

 # Get the language of the name of a bible in the database """
def language(name:str)->str:
     """Get the language of the valid name of a bible in a database
     name(string):A valid name in the database representing a bible
     RETURN:string
     """
     
     bible = get_settings()[" DATABASES"].get(name)
     if bible is None:
         raise ValueError("Name not found in database")
     return bible["language"]
     
       
if __name__ == "__main__":
    pass