# Author: Ofori George
# Commencement Date: Saturday 4 October, 2025.
# Telephone / WhatsApp: (+233)504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: https://george200512.github.io/george-ofori.com/
# github: https://www.github.com/George200512/

"""
A script to create the bible class and the compiler class
"""
from collections import UserList
import sqlite3
import json
import requests as rq
from requests.exceptions import Timeout, ConnectionError, HTTPError
import re
import os
from dotenv import load_dotenv

from books.book import BookArray, Book
from books import exceptions as exc
import utils
import exceptions as bexc

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)
API_KEY = os.getenv("API_KEY")
URL = "https://api.scripture.api.bible/v1/bibles"


class Bible(UserList):
    """The bible class for getting the bible version in the specified language
    if found in database"""

    def __init__(self, name=None):
        """Initializing routine"""

        self.name = name
        if self.name is None:
            self.path = utils.get_settings()["DATABASES"].get("DEFAULT")
        else:
            self.path = utils.get_settings()["DATABASES"].get(name)
        if self.path is None:
            raise bexc.BibleNotAvailableError(
                "Requested bible not available in database"
            )
        self.connection = sqlite3.connect(self.path)
        self.no_of_books = 66
        self.book_array = BookArray(
            [Book(self.connection, num) for num in range(1, self.no_of_books + 1)]
        )
        super().__int__(self.book_array)

    def close(self):
        """Close the database"""

        self.connection.close()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.close()

    def __str__(self):
        """A string representation of the bible class"""

        self.version = utils.version(self.name)
        self.language = utils.language(self.name)
        return f"{self.version}({self.language})"

    def __repr__(self):
        """A string representation of how the class should be instantiated"""

        return f"Bible(name={self.name})"

    def __iter__(self):
        """An iteration method that is automatically called anytime the bible is being interested over"""

        return iter(self.data)

    def __getitem__(self, index):
        """Get the book or books of a bible     based on the index
        NB:This index should be used like the normal indexing style
        it should start from 1 not zero.Index or slice less than zero is an error"""

        if isinstance(index, int):
            if (index < 1) or index > (len(self.verse_array)):
                raise exc.BookNotFoundError("Book number not found")
            return self.book_array[index - 1]
        elif isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is not None:
                if (start < 1) or start > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")
            else:
                start = 1

            if stop is not None:
                if (stop < 1) or stop > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")

            if step is not None:
                if (step < 1) or step > (len(self.book_array)):
                    raise exc.BookNotFoundError("Book number not found")
            else:
                step = 1
            return self.book_array[start - 1 : stop : step]
        else:
            return self.book_array[index]

    def book(self, num):
        """Get the book of the bible based on the number
        num(integer):The number of a bible
        RETURN:Book class or None
        """

        try:
            return self[num]
        except exc.BookNotFoundError:
            return None

    def head(self, quantity=5):
        """Get the first five books of a bible if it is more than five or all books
        quantity:the number of books to return.Default is 5.
        Returns:BookArray
        """

        return self.book_array[:quantity]

    def tail(self, quantity=5):
        """Get the last five book of a bible if it is more than five or all books
        quantity:the number of books to return.Default is 5.
        Returns: BookArray
        """

        return self.book_array[-quantity:]

    def books(self, start=1, stop=1, step=None):
        """Get a list of book from the bible
        start:where to start slicing the bible defaults to 1
        stop:where to stop slicing the bible defaults to 1
        step:how many steps to take before the next slice defaults to none which is equal to 1
        RETURNS:A book array instance
        """

        try:
            return self[start:stop:step]
        except exc.BookNotFoundError:
            return BookArray([])

    def testament(self, type):
        """
        Get the books of the same type.
        type:(string); whether old or new.
        RETURNS:Book array.
        """

        if not isinstance(type, string):
            raise TypeError("Argument should be of type string.")
        if type == "old":
            return self[:39]
        elif type == "new":
            return self[40:]
        else:
            return None

    def describe(self):
        """
        Returns a json that gives a discription of the bible including version, language,
        number of books, chapters, verses etc.
        """

        no_of_chapters = sum(
            map(lambda book_id: _get_number_of_chapters(book_id), range(1, 66 + 1))
        )
        no_of_verses = 0
        no_of_words = 0
        for book, book_id in enumerate(self, start=1):
            for chapter, chapter_id in enumerate(book, start=1):
                no_of_verses += _get_number_of_verses(book_id, chapter_id)
                no_of_words += _get_number_of_words(book_id, chapter_id)

        data = {
            "name": self.name,
            "version": self.version,
            "language": self.language,
            "number_of_books": self.no_of_books,
            "number_of_chapters": no_of_chapters,
            "number_of_verses": no_of_verses,
            "number_of_words": no_of_words,
        }
        return json.dumps(data)

    def _get_number_of_chapters(self, book_number):
        """
        Get the number of chapters in a book.
        book_number(int):the nth book of the bible. Starts from 1.
        RETURN: an integer
        """

        return len(self[book_number])

    def _get_number_of_verses(self, book_number, chapter_number):
        """
        Get the number of verses in a chapter
        chapter_number(int): the nth chapter of a book. Starts from 1.
        book_number(int): the nth book of the bible. Starts from 1.
        RETURN: an integer.
        """

        return len(self[book_number][chapter_number])

    def _get_number_of_words(self, book_number, chapter_number):
        """
        Get the number of words in each verse.
        book_number(int): The nth book of a bible.Starts from 1
        chapter_number(int): The nth chapter of a book.Starts from 1.
        RETURN: a generator that yields the number of words in each verse of a chapter.
        """

        no_of_words = 0
        no_of_words_in_a_chapter = 0
        pattern = re.compile(r"\w")
        for verse in self[book_number][chapter_number]:
            for word in verse.split():
                if pattern.match(word):
                    no_of_words += 1
            no_of_a_words_in_a_chapter += no_of_words
        yield no_of_words_in_a_chapter


# Define the compiler class
class Compiler:
    """
    A compiler class is responsible for getting the bible with the specified version and language
    from the internet and create a new database for a new bible version or update the existing one.
    """

    def __init__(self):
        """A method that is called immediately an object of the class is created"""

        versions = {}
        bible_ids = {}
        if utils.get_settings().get("VERSIONS") is None:
            try:
                self.response = rq.get(URL, headers={"api-key": API_KEY}, timeout=3.7)
            except (HTTPError, ConnectionError, Timeout) as e:
                raise bexc.NonBiblicalError(e)
            else:
                self.data = self.response.json()
                self.data = self.data["data"]
                for item in self.data:
                    bible = {}
                    bible["id"] = item["id"]
                    bible["name"] = item["name"]
                    bible["abbreviation"] = item["abbreviation"]
                    bible["language_id"] = item["language"]["id"]
                    bible["language_name"] = item["language"]["name"]
                    bible["country_name"] = item["countries"][0]["name"]
                    bible["type"] = item["type"]
                    bible["updatedAt"] = item["updatedAt"]
                    bible_ids[f"{bible['abbreviation']}_{bible['language_id']}"] = (
                        bible["id"]
                    )
                    versions[item["id"]] = bible
                utils.set_settings("VERSIONS", versions)
                utils.set_settings("BIBLE_IDS", bible_ids)

    def compile_chapters(self, conn, **kwargs):
        """
        Get the verses of a chapter of a book and then arrange it in the database.
        conn: an instance of the the sqlite3 connection
        **kwargs: A keyword augmented list that tells you the version, language and chapter of the bible.
        RETURNS: None
        """
        
        version = kwargs["VERSION"]
        language = kwargs["LANGUAGE"]
        book = kwargs["BOOK"]
        chapter_id = kwargs["CHAPTER"]
        bible_ids = utils.get_settings()["BIBLE_IDS"]
        id_key = f"{version}_{language}"
        if id_key in bible_ids.keys():
            bible_id = bible_ids[id_key]
        else:
            raise KeyError("Version or language not found")    