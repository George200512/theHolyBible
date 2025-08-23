# Author: Ofori George
# Commencement Date: Thursday 21 August, 2025.
# Telephone / WhatsApp: 0504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

"""
This scripts provides the necessary classes used for representing a verse in a bible or
a list of verses(verse array).
"""

from collections import UserString, UserList


# Create a verse class to represent a single a verse.
class Verse(UserString):
    """Initialise the arguments passed to the constructor"""

    def __init__(self, connection, text, chapter_no, book, verse_no):
        """
        connection: a connection object for creating the cursor which will be used to
        create database.
        text: the actual text of the verse.
        chapter_no: an integer representing the chapter number.
        book: a string representing the book.
        verse_no: a string representing the verse number.
        """

        self.conn = connection
        self.cursor = self.conn.cursor()  # The cursor object for querying the database.
        self._text = text
        self._chapter = chapter_no
        self._book = book
        self._verse = verse_no
        self.create_verse_table_if_not_exists()
        self._id = self.get_id()
        self.add_verse_if_not_added()
        super().__init__(self._text)

    def get_id(self):
        """Generate the id of the verse if it has none or return the existing one"""

        self.cursor.execute(
            """
            SELECT id FROM verses WHERE text=? AND chapter_no=? AND  verse_no=? AND book=?;
            """,
            (self._text, self._chapter, self._verse, self._book),
        )
        row = self.cursor.fetchone()
        if row:
            return row[0]
        id = self.add_verse_if_not_added()[0]
        return id

    def create_verse_table_if_not_exists(self):
        """Create the verse table in the database if it is not present"""

        self.cursor.execute(
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
        self.conn.commit()

    def add_verse_if_not_added(self):
        """Add a new verse to the database if it has not been added."""

        self.cursor.execute(
            """
            SELECT id FROM verses WHERE text=? AND chapter_no=? AND verse_no=?;
            """,
            (self._text, self._chapter, self._verse),
        )
        row = self.cursor.fetchone()
        if row:
            return row
        self.cursor.execute(
            """
        INSERT INTO verses(text, chapter_no, verse_no,  book) VALUES (?, ?, ?, ?);
        """,
            (self._text, self._chapter, self._verse, self._book),
        )
        self.conn.commit()
        self.cursor.execute(
            """
            SELECT id FROM verses WHERE text=? AND chapter_no=? AND verse_no=?;
            """,
            (self._text, self._chapter, self._verse),
        )
        row = self.cursor.fetchone()
        return row

    def __repr__(self):
        """Return a representation of the verse that can be used to create a verse"""

        return f"Verse(connection={self.conn}, text={self.text}, chapter_no={self.chapter},  book={self.book}, verse_no={self.verse})"

    def __str__(self):
        """A string representation of a verse"""

        return f"Verse {self.verse}"

    @property
    def value(self):
        """Show the actual text"""

        return self._text

    @property
    def chapter(self):
        """Return the chapter number"""

        return self._chapter

    @property
    def book(self):
        """Return the book name"""

        return self._book

    @property
    def verse(self):
        """Return the verse number"""

        return self._verse

    @property
    def id(self):
        """return the id of a verse"""

        return self._id


# Create a VerseArray class to represent a collection of related or not related verses
class VerseArray(UserList):
    """A class representing a group of verses"""

    def __init__(self, array=[]):
        """Initialise the variables needed feo creating the class"""

        self.array = array
        if isinstance(self.array, (list, tuple)):
            super().__init__(self.array)
        raise ValueError("Array must be a tuple or a list")

    def __iter__(self):
        """A dunder method when the array is being iterated over"""

        for verse in self.array:
            yield verse

    def __str__(self):
        """A string representation of the class"""

        return f"[<VerseArray:{len(self.array)}>]"

    def __repr__(self):
        """A string representing how an object of the class should be created"""

        return f"VerseArray(array={self.array})"
