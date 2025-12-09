# Author: Ofori George
# Commencement Date: Sunday 2 November, 2025.
# Telephone / WhatsApp: (+233)504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

"""
A script that handles testing of the bible class and the compiler class.
"""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime 

from bible import Compiler, Bible


# A class for the compiler unnitest
class TestCompiler(unittest.TestCase):
    """The class for the compiler testcase"""

    @patch("bible.utils")
    @patch("bible.rq.get")
    def test___init__(self, mock_get, mock_utils):
        """A method for testing if the initial routines that are supposed to take place
        when a compiler class is initiated"""

        mock_utils.get_settings.return_value = {"VERSIONS": None}
        fake_data = {
            "data": [
                {
                    "id": "1234abcd5678efgh9012ijkl",
                    "name": "King James Version",
                    "abbreviation": "KJV",
                    "language": {"id": "eng", "name": "English"},
                    "countries": [{"name": "United States"}],
                    "type": "Bible",
                    "updatedAt": "2025-01-01T00:00:00.000Z",
                }
            ]
        }

        mock_response = MagicMock()
        mock_response.json.return_value = fake_data
        mock_get.return_value = mock_response
        compiler = Compiler()
        mock_get.assert_called_once()
        self.assertEqual(mock_utils.set_settings.call_count, 2)
        self.assertTrue(hasattr(compiler, "data"))
        self.assertEqual(compiler.data[0]["id"], "1234abcd5678efgh9012ijkl")

    @patch.object(Compiler, "__init__", lambda self: None)
    @patch("sqlite3.connect")
    def test_compile_chapter(self, mock_connect):
        """
        Test whether the method compiles the chapters into the database.
        """

        compiler = Compiler()
        settings_mock = {"BIBLE_IDS": {"KJV_en": "de4e12af7f28f599-02"}}
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "data":{
                "content": """<p class="p"><span data-number="1" data-sid="GEN 1:1" class="v">1</span>In the beginning God created the heaven and the earth. <span data-number="2" data-sid="GEN 1:2" class="v">2</span>And the earth was without form, and void; and darkness <span class="add">was</span> upon the face of the deep. And the Spirit of God moved upon the face of the waters.</p><p class="p"><span data-number="3" data-sid="GEN 1:3" class="v">3</span>And God said, Let there be light: and there was light. <span data-number="4" data-sid="GEN 1:4" class="v">4</span>And God saw the light, that <span class="add">it was</span> good: and God divided the light from the darkness. <span data-number="5" data-sid="GEN 1:5" class="v">5</span>And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.</p><p class="p"><span data-number="6" data-sid="GEN 1:6" class="v">6</span>¶ And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. <span data-number="7" data-sid="GEN 1:7" class="v">7</span>And God made the firmament, and divided the waters which <span class="add">were</span> under the firmament from the waters which <span class="add">were</span> above the firmament: and it was so. <span data-number="8" data-sid="GEN 1:8" class="v">8</span>And God called the firmament Heaven. And the evening and the morning were the second day.</p><p class="p"><span data-number="9" data-sid="GEN 1:9" class="v">9</span>¶ And God said, Let the waters under the heaven be gathered together unto one place, and let the dry <span class="add">land</span> appear: and it was so. <span data-number="10" data-sid="GEN 1:10" class="v">10</span>And God called the dry <span class="add">land</span> Earth; and the gathering together of the waters called he Seas: and God saw that <span class="add">it was</span> good. <span data-number="11" data-sid="GEN 1:11" class="v">11</span>And God said, Let the earth bring forth grass, the herb yielding seed, <span class="add">and</span> the fruit tree yielding fruit after his kind, whose seed <span class="add">is</span> in itself, upon the earth: and it was so. <span data-number="12" data-sid="GEN 1:12" class="v">12</span>And the earth brought forth grass, <span class="add">and</span> herb yielding seed after his kind, and the tree yielding fruit, whose seed <span class="add">was</span> in itself, after his kind: and God saw that <span class="add">it was</span> good. <span data-number="13" data-sid="GEN 1:13" class="v">13</span>And the evening and the morning were the third day.</p><p class="p"><span data-number="14" data-sid="GEN 1:14" class="v">14</span>¶ And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: <span data-number="15" data-sid="GEN 1:15" class="v">15</span>And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. <span data-number="16" data-sid="GEN 1:16" class="v">16</span>And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: <span class="add">he made</span> the stars also. <span data-number="17" data-sid="GEN 1:17" class="v">17</span>And God set them in the firmament of the heaven to give light upon the earth, <span data-number="18" data-sid="GEN 1:18" class="v">18</span>And to rule over the day and over the night, and to divide the light from the darkness: and God saw that <span class="add">it was</span> good. <span data-number="19" data-sid="GEN 1:19" class="v">19</span>And the evening and the morning were the fourth day.</p><p class="p"><span data-number="20" data-sid="GEN 1:20" class="v">20</span>And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl <span class="add">that</span> may fly above the earth in the open firmament of heaven. <span data-number="21" data-sid="GEN 1:21" class="v">21</span>And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that <span class="add">it was</span> good. <span data-number="22" data-sid="GEN 1:22" class="v">22</span>And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. <span data-number="23" data-sid="GEN 1:23" class="v">23</span>And the evening and the morning were the fifth day.</p><p class="p"><span data-number="24" data-sid="GEN 1:24" class="v">24</span>¶ And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. <span data-number="25" data-sid="GEN 1:25" class="v">25</span>And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that <span class="add">it was</span> good.</p><p class="p"><span data-number="26" data-sid="GEN 1:26" class="v">26</span>¶ And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. <span data-number="27" data-sid="GEN 1:27" class="v">27</span>So God created man in his <span class="add">own</span> image, in the image of God created he him; male and female created he them. <span data-number="28" data-sid="GEN 1:28" class="v">28</span>And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.</p><p class="p"><span data-number="29" data-sid="GEN 1:29" class="v">29</span>¶ And God said, Behold, I have given you every herb bearing seed, which <span class="add">is</span> upon the face of all the earth, and every tree, in the which <span class="add">is</span> the fruit of a tree yielding seed; to you it shall be for meat. <span data-number="30" data-sid="GEN 1:30" class="v">30</span>And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein <span class="add">there is</span> life, <span class="add">I have given</span> every green herb for meat: and it was so. <span data-number="31" data-sid="GEN 1:31" class="v">31</span>And God saw every thing that he had made, and, behold, <span class="add">it was</span> very good. And the evening and the morning were the sixth day.</p>"""
            }
        }
        with patch("utils.get_settings", return_value=settings_mock):
            kwargs = {"VERSION": "KJV", "LANGUAGE": "en", "BOOK": "GEN", "CHAPTER": "1"}
            with patch(
              "bible.rq.get",
                return_value=mock_response,
            ):
                mock_connect.return_value = MagicMock()
                compiler.compile_chapter("DATABASES/good-news/good-news.db", **kwargs)
                
    def test_compile_book(self):
         """
         Test whether the compile book method compiles the bible well.
         """
         
         with patch.object(Compiler, "__init__", lambda self: None):
             with patch.object(Compiler, "compile_chapter", lambda self: None):
                 compiler = Compiler()
                 compiler.compile_book("DATABASES/good-news/good-news.db", **{
                 "VERSION": "KJV", "LANGUAGE": "en", "BOOK_ID":"GEN"
                 })
     
    @patch("sqlite3.connect")                    
    def test_compile_bible(self, mock_connect):
         """
         Test whether the compile_bible method compiles the bible into the database 
         """
         mock_connect.return_value = MagicMock()
         language= "en" 
         version = "KJV"
         with patch.object(Compiler, "__init__", lambda self:None):
             with patch.object(Compiler, "compile_book", lambda self:None):
                 with patch("utils.set_settings", side_effect=lambda key, value:None):
                     Compiler().compile_bible(language=language, version=version)       
    
    @patch.object(Compiler, "__init__", lambda self: None)
    @patch("sqlite3.connect")
    def test_update_chapter(self, mock_connect):
        """
        Test whether the method updates the chapters into the database.
        """

        compiler = Compiler()
        settings_mock = {"BIBLE_IDS": {"KJV_en": "de4e12af7f28f599-02"}}
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "data":{
                "content": """<p class="p"><span data-number="1" data-sid="GEN 1:1" class="v">1</span>In the beginning God created the heaven and the earth. <span data-number="2" data-sid="GEN 1:2" class="v">2</span>And the earth was without form, and void; and darkness <span class="add">was</span> upon the face of the deep. And the Spirit of God moved upon the face of the waters.</p><p class="p"><span data-number="3" data-sid="GEN 1:3" class="v">3</span>And God said, Let there be light: and there was light. <span data-number="4" data-sid="GEN 1:4" class="v">4</span>And God saw the light, that <span class="add">it was</span> good: and God divided the light from the darkness. <span data-number="5" data-sid="GEN 1:5" class="v">5</span>And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.</p><p class="p"><span data-number="6" data-sid="GEN 1:6" class="v">6</span>¶ And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. <span data-number="7" data-sid="GEN 1:7" class="v">7</span>And God made the firmament, and divided the waters which <span class="add">were</span> under the firmament from the waters which <span class="add">were</span> above the firmament: and it was so. <span data-number="8" data-sid="GEN 1:8" class="v">8</span>And God called the firmament Heaven. And the evening and the morning were the second day.</p><p class="p"><span data-number="9" data-sid="GEN 1:9" class="v">9</span>¶ And God said, Let the waters under the heaven be gathered together unto one place, and let the dry <span class="add">land</span> appear: and it was so. <span data-number="10" data-sid="GEN 1:10" class="v">10</span>And God called the dry <span class="add">land</span> Earth; and the gathering together of the waters called he Seas: and God saw that <span class="add">it was</span> good. <span data-number="11" data-sid="GEN 1:11" class="v">11</span>And God said, Let the earth bring forth grass, the herb yielding seed, <span class="add">and</span> the fruit tree yielding fruit after his kind, whose seed <span class="add">is</span> in itself, upon the earth: and it was so. <span data-number="12" data-sid="GEN 1:12" class="v">12</span>And the earth brought forth grass, <span class="add">and</span> herb yielding seed after his kind, and the tree yielding fruit, whose seed <span class="add">was</span> in itself, after his kind: and God saw that <span class="add">it was</span> good. <span data-number="13" data-sid="GEN 1:13" class="v">13</span>And the evening and the morning were the third day.</p><p class="p"><span data-number="14" data-sid="GEN 1:14" class="v">14</span>¶ And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: <span data-number="15" data-sid="GEN 1:15" class="v">15</span>And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. <span data-number="16" data-sid="GEN 1:16" class="v">16</span>And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: <span class="add">he made</span> the stars also. <span data-number="17" data-sid="GEN 1:17" class="v">17</span>And God set them in the firmament of the heaven to give light upon the earth, <span data-number="18" data-sid="GEN 1:18" class="v">18</span>And to rule over the day and over the night, and to divide the light from the darkness: and God saw that <span class="add">it was</span> good. <span data-number="19" data-sid="GEN 1:19" class="v">19</span>And the evening and the morning were the fourth day.</p><p class="p"><span data-number="20" data-sid="GEN 1:20" class="v">20</span>And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl <span class="add">that</span> may fly above the earth in the open firmament of heaven. <span data-number="21" data-sid="GEN 1:21" class="v">21</span>And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that <span class="add">it was</span> good. <span data-number="22" data-sid="GEN 1:22" class="v">22</span>And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. <span data-number="23" data-sid="GEN 1:23" class="v">23</span>And the evening and the morning were the fifth day.</p><p class="p"><span data-number="24" data-sid="GEN 1:24" class="v">24</span>¶ And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. <span data-number="25" data-sid="GEN 1:25" class="v">25</span>And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that <span class="add">it was</span> good.</p><p class="p"><span data-number="26" data-sid="GEN 1:26" class="v">26</span>¶ And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. <span data-number="27" data-sid="GEN 1:27" class="v">27</span>So God created man in his <span class="add">own</span> image, in the image of God created he him; male and female created he them. <span data-number="28" data-sid="GEN 1:28" class="v">28</span>And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.</p><p class="p"><span data-number="29" data-sid="GEN 1:29" class="v">29</span>¶ And God said, Behold, I have given you every herb bearing seed, which <span class="add">is</span> upon the face of all the earth, and every tree, in the which <span class="add">is</span> the fruit of a tree yielding seed; to you it shall be for meat. <span data-number="30" data-sid="GEN 1:30" class="v">30</span>And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein <span class="add">there is</span> life, <span class="add">I have given</span> every green herb for meat: and it was so. <span data-number="31" data-sid="GEN 1:31" class="v">31</span>And God saw every thing that he had made, and, behold, <span class="add">it was</span> very good. And the evening and the morning were the sixth day.</p>"""
            }
        }
        with patch("utils.get_settings", return_value=settings_mock):
            kwargs = {"VERSION": "KJV", "LANGUAGE": "en", "BOOK": "GEN", "CHAPTER": "1"}
            with patch(
              "bible.rq.get",
                return_value=mock_response,
            ):
                mock_connect.return_value = MagicMock()
                compiler.update_chapter("DATABASES/good-news/good-news.db", **kwargs)
  
    def test_update_book(self):
         """
         Test whether the compile book method compiles the bible well.
         """
         
         with patch.object(Compiler, "__init__", lambda self: None):
             with patch.object(Compiler, "update_chapter", lambda self: None):
                 compiler = Compiler()
                 compiler.update_book("DATABASES/good-news/good-news.db", **{
                 "VERSION": "KJV", "LANGUAGE": "en", "BOOK_ID":"GEN"
                 })      

    @patch("sqlite3.connect")  
    @patch("os.path.exists", return_value=True)                  
    def test_update_bible(self, mock_path_exists, mock_connect):
         """
         Test whether the update_bible method compiles the bible into the database 
         """
         mock_connect.return_value = MagicMock()
         with patch.object(Compiler, "__init__", lambda self:None):
             with patch.object(Compiler, "update_book", lambda self:None):
                 with patch("utils.get_settings", return_value={
                 "DATABASES":[
                 {
                 "path": "DATABASES/DEFAULT/DEFAULT.db",
                 "name": "DEFAULT",
                 "version": "KJV",
                 "language": "en",
                 "lastUpdated": f"{datetime.now()}" 
                  }
                 ],
                 "BOOKS":[{
            "name": "Genesis",
            "chapters": 50,
            "description": "Tells of creation, the fall of humanity, the early history of mankind, the patriarchs Abraham, Isaac, Jacob, and Joseph; God\u2019s covenant promises to them upheld even in hardship. \uea010\uea02",
            "id": ["GEN"]
        },
        {
            "name": "Exodus",
            "chapters": 40,
            "description": "Describes Israel\u2019s slavery in Egypt, Moses\u2019 leadership, the plagues, the Exodus from Egypt, covenant at Sinai, and instructions for worship. \uea011\uea02",
            "id": ["EXO"]
        },
        {
            "name": "Leviticus",
            "chapters": 27,
            "description": "Focuses on laws and rituals, holiness codes, priestly duties, and how Israel is to live set apart; emphasizes worship and ethical living. \uea012\uea02",
            "id": ["LEV"]
        },
        {
            "name": "Numbers",
            "chapters": 36,
            "description": "Narrates Israel\u2019s wandering in the wilderness, census data, rebellions, provisions, and God\u2019s guidance amid disobedience. \uea013\uea02",
            "id":["NUM"]
        },
        {
            "name": "Deuteronomy",
            "chapters": 34,
            "description": "Collection of Moses\u2019 speeches reviewing law, covenant obligations, and Israel\u2019s history as they prepare to enter the Promised Land. \uea014\uea02",
            "id":["DEU"]
        },
        {
            "name": "Joshua",
            "chapters": 24,
            "description": "Israel, under Joshua, conquers Canaan, divides the land among the tribes, and renews their covenant with God. \uea015\uea02",
            "id":["JOS"]
        },
        {
            "name": "Judges",
            "chapters": 21,
            "description": "Cycle of Israel sinning, being oppressed, crying out, and being rescued by judges; shows the consequences of turning from covenant faithfulness. \uea016\uea02",
           "id":["JDG"]
        },
        {
            "name": "Ruth",
            "chapters": 4,
            "description": "A story of loyalty, redemption, and God\u2019s providence, focusing on Ruth, a Moabite woman, and her integration into Israel\u2019s story. \uea017\uea02",
            "id":["RUT"]
        },
        {
            "name": "1 Samuel",
            "chapters": 31,
            "description": "Transition of Israel from the period of judges to monarchy; story of Samuel, Saul, and the rise of David. \uea018\uea02",
            "id":[" 1SA"]
        },
        {
            "name": "2 Samuel",
            "chapters": 24,
            "description": "Reign of David: his sins, successes, consolidation of the kingdom, and God\u2019s promises to David\u2019s house. \uea019\uea02",
            "id":["2SA"]
        },
        {
            "name": "1 Kings",
            "chapters": 22,
            "description": "Begins with Solomon\u2019s reign, wisdom, and temple building; then divides kingdom histories of Israel and Judah, decline, idolatry, and prophets. \uea0110\uea02",
            "id":["1KI"]
        },
        {
            "name": "2 Kings",
            "chapters": 25,
            "description": "Further history of Israel and Judah\u2019s kings, fall of Israel to Assyria, Judah to Babylon; prophetic ministries and judgment. \uea0111\uea02",
            "id":["2KI"]
        },
        {
            "name": "1 Chronicles",
            "chapters": 29,
            "description": "Retrospective history emphasizing David and the temple; genealogies; religious reforms in Judah. \uea0112\uea02",
            "id":["1CH"]
        },
        {
            "name": "2 Chronicles",
            "chapters": 36,
            "description": "Continuation of Israel/Judah\u2019s history focusing more on Judah, temple worship, reforms, exile, and hope. \uea0113\uea02",
            "id":["2CH"]
        },
        {
            "name": "Ezra",
            "chapters": 10,
            "description": "Return from exile under Cyrus, rebuilding of the temple, reforms among the returned exiles, leadership of Ezra. \uea0114\uea02",
            "id":["EZR"]
        },
        {
            "name": "Nehemiah",
            "chapters": 13,
            "description": "Nehemiah leads rebuilding of Jerusalem\u2019s walls, community reforms, renewed covenant, and restoration. \uea0115\uea02",
            "id":["NEH"]
        },
        {
            "name": "Esther",
            "chapters": 10,
            "description": "Story of Esther\u2019s courage in Persia, saving the Jewish people from genocide, God\u2019s providence in unexpected ways. \uea0116\uea02",
            "id":["EST"]
        },
        {
            "name": "Job",
            "chapters": 42,
            "description": "Explores suffering, divine justice, integrity; dialogues between Job and his friends; God\u2019s response from the whirlwind. \uea0117\uea02",
            "id":["JOB"]
        },
        {
            "name": "Psalms",
            "chapters": 150,
            "description": "Collection of poems, hymns, praises, laments; used in Israel\u2019s worship life; wide range of emotions and human experience. \uea0118\uea02",
            "id":["PSA"]
        },
        {
            "name": "Proverbs",
            "chapters": 31,
            "description": "Wisdom sayings, advice for life, character, discipline, and fear of the Lord as foundational. \uea0119\uea02",
            "id":["PRO"]
        },
        {
            "name": "Ecclesiastes",
            "chapters": 12,
            "description": "Reflections on meaning, vanity, the fleeting nature of life and human accomplishments; calls to fear God and enjoy life. \uea0120\uea02",
            "id":["ECC"]
        },
        {
            "name": "Song of Solomon",
            "chapters": 8,
            "description": "Poetic love dialogue between lovers; often seen as celebrating human love, marriage, and sometimes allegorical spiritual love. \uea0121\uea02",
            "id":["SNG"]
        },
        {
            "name": "Isaiah",
            "chapters": 66,
            "description": "Prophecies of judgment and hope; visions of God\u2019s holiness; future promises including the suffering servant, restoration, and messianic themes. \uea0122\uea02",
            "id":["ISA"]
        },
        {
            "name": "Jeremiah",
            "chapters": 52,
            "description": "Prophet Jeremiah\u2019s warnings of impending judgment for Judah, calls to repentance, suffering of the prophet, and future restoration. \uea0123\uea02",
            "id":["JER"]
        },
        {
            "name": "Lamentations",
            "chapters": 5,
            "description": "Poetic laments over Jerusalem\u2019s destruction; grief, mourning, confession, and hope. \uea0124\uea02",
            "id":["LAM"]
        },
        {
            "name": "Ezekiel",
            "chapters": 48,
            "description": "Prophecies during exile; visions, symbolic acts; judgment and hope; restoration and new temple vision. \uea0125\uea02",
            "id":["EZK"]
        },
        {
            "name": "Daniel",
            "chapters": 12,
            "description": "Stories and visions; God\u2019s sovereignty over kingdoms; trials of faith; apocalyptic visions about the end times and God\u2019s kingdom. \uea0126\uea02",
            "id":["DAN"]
        },
        {
            "name": "Hosea",
            "chapters": 14,
            "description": "Marriage metaphor for Israel\u2019s unfaithfulness; God\u2019s steadfast love and restoration despite betrayal. \uea0127\uea02",
            "id":["HOS"]
        },
        {
            "name": "Joel",
            "chapters": 3,
            "description": "Prophetic announcements of judgment; call to repentance; promise of outpouring of God\u2019s spirit and restoration. \uea0128\uea02",
            "id":["JOL"]
        },
        {
            "name": "Amos",
            "chapters": 9,
            "description": "Prophet Amos warns Israel of social injustice, hypocrisy; emphasizes justice, righteousness, and warnings before restoration. \uea0129\uea02",
            "id":["AMO"]
        },
        {
            "name": "Obadiah",
            "chapters": 1,
            "description": "Shortest Old Testament book; prophecy against Edom for pride and betrayal, promise of restoration to Israel. \uea0130\uea02",
            "id":["OBA"]
        },
        {
            "name": "Jonah",
            "chapters": 4,
            "description": "Story of a reluctant prophet, God\u2019s mercy to Nineveh; themes of obedience, compassion, and forgiveness. \uea0131\uea02",
            "id":["JON"]
        },
        {
            "name": "Micah",
            "chapters": 7,
            "description": "Prophecies including messages about judgment for social injustice and hope for a ruler from Bethlehem; God\u2019s requirements for justice, mercy, humility. \uea0132\uea02",
            "id":["MIC"]
        },
        {
            "name": "Nahum",
            "chapters": 3,
            "description": "Prophecy against Nineveh; God\u2019s justice and wrath against cruelty. \uea0133\uea02",
            "id":["NAM"]
        },
        {
            "name": "Habakkuk",
            "chapters": 3,
            "description": "Dialogues between prophet and God about injustice; vision, lament, and ultimately trust in God despite unanswered questions. \uea0134\uea02",
            "id":["HAB"]
        },
        {
            "name": "Zephaniah",
            "chapters": 3,
            "description": "Warning of coming Day of the LORD, calls to repentance; promise of restoration for remnant. \uea0135\uea02",
            "id":["ZEP"]
        },
        {
            "name": "Haggai",
            "chapters": 2,
            "description": "Encouragement to rebuild the temple after exile; God\u2019s promise to dwell among His people. \uea0136\uea02",
            "id":["HAG"]
        },
        {
            "name": "Zechariah",
            "chapters": 14,
            "description": "Visions, prophetic oracles, encouragement to return; future hopes including messianic rule. \uea0137\uea02",
            "id":["ZEC"]
        },
        {
            "name": "Malachi",
            "chapters": 4,
            "description": "Final prophetic word of the Old Testament; addresses Israel\u2019s faithlessness, call to righteous living, promise of messenger. \uea0138\uea02",
            "id":["MAL"]
        },
        {
            "name": "Matthew",
            "chapters": 28,
            "description": "One of the Gospels; presents Jesus as Messiah, King of the Jews; includes genealogy, teachings, parables, death and resurrection. \uea0139\uea02",
            "id":["MAT"]
        },
        {
            "name": "Mark",
            "chapters": 16,
            "description": "A fast-paced Gospel emphasizing Jesus\u2019 actions, authority, suffering, and that He came to serve; includes many miracles. \uea0140\uea02",
            "id":["MRK"]
        },
        {
            "name": "Luke",
            "chapters": 24,
            "description": "Gospel giving detailed narrative of Jesus\u2019 life, ministry, compassion, parables; careful ordering and historical detail; bridge between Old Testament and early church. \uea0141\uea02",
            "id":["LUK"]
        },
        {
            "name": "John",
            "chapters": 21,
            "description": "Gospel focusing on Jesus\u2019 identity, signs, \u2018I am\u2019 statements; emphasizes belief, eternal life, love. \uea0142\uea02",
            "id":["JHN"]
        },
        {
            "name": "Acts",
            "chapters": 28,
            "description": "History of the early Christian church after Jesus\u2019 ascension; spread of the Gospel through apostles; key figures include Peter and Paul. \uea0143\uea02",
            "id":["ACT"]
        },
        {
            "name": "Romans",
            "chapters": 16,
            "description": "Paul\u2019s letter to the church in Rome explaining the gospel, justification by faith, relation of Israel and Gentiles. \uea0144\uea02",
            "id":["ROM"]
        },
        {
            "name": "1 Corinthians",
            "chapters": 16,
            "description": "Paul addresses problems in Corinth: division, immorality, spiritual gifts, resurrection; guidance for church life. \uea0145\uea02",
            "id":["1CO"]
        },
        {
            "name": "2 Corinthians",
            "chapters": 13,
            "description": "Paul defends his apostleship, encourages reconciliation, highlights suffering and God\u2019s comfort. \uea0146\uea02",
            "id":["2CO"]
        },
        {
            "name": "Galatians",
            "chapters": 6,
            "description": "Paul refutes legalism, teaches justification by faith in Christ apart from works of the law; Christian freedom. \uea0147\uea02",
            "id":["GAL"]
        },
        {
            "name": "Ephesians",
            "chapters": 6,
            "description": "Paul\u2019s letter about the church as the body of Christ; unity, spiritual blessings, Christian conduct. \uea0148\uea02",
            "id":["EPH"]
        },
        {
            "name": "Philippians",
            "chapters": 4,
            "description": "Letter of encouragement and joy; Christ\u2019s humility and exaltation; contentment in all circumstances. \uea0149\uea02",
            "id":["PHP"]
        },
        {
            "name": "Colossians",
            "chapters": 4,
            "description": "Paul emphasizes Christ\u2019s supremacy and sufficiency; encourages believers to live in Christ and avoid false teachings. \uea0150\uea052",
            "id": ["COL"]
        },
        {
            "name": "1 Thessalonians",
            "chapters": 5,
            "description": "Paul encourages believers, teaches about Christ\u2019s return, holiness, and how to live in light of that coming. \uea0151\uea02",
            "id": ["1TH"]
        },
        {
            "name": "2 Thessalonians",
            "chapters": 3,
            "description": "Addresses misunderstandings about Christ\u2019s return; encourages perseverance; clarifies timing. \uea0152\uea02",
            "id": ["2TH"]
        },
        {
            "name": "1 Timothy",
            "chapters": 6,
            "description": "Paul gives guidance to Timothy on church leadership, dealing with false teaching, and godly conduct. \uea0153\uea02",
            "id": ["1TI"]
        },
        {
            "name": "2 Timothy",
            "chapters": 4,
            "description": "Paul\u2019s final letter; exhortation to remain faithful, endure suffering, storing up treasure in heaven. \uea0154\uea02",
            "id": ["2TI"]
        },
        {
            "name": "Titus",
            "chapters": 3,
            "description": "Instructions for organizing churches, teaching sound doctrine, good works. \uea0155\uea02",
            "id": ["TIT"]
        },
        {
            "name": "Philemon",
            "chapters": 1,
            "description": "Personal appeal from Paul to Philemon to receive back his runaway slave Onesimus as a brother in Christ. \uea0156\uea02",
            "id": ["PHM"]
        },
        {
            "name": "Hebrews",
            "chapters": 13,
            "description": "Anonymous letter encouraging Jewish Christians; shows the superiority of Christ, fulfillment of the old covenant; perseverance in faith. \uea0157\uea02",
            "id": ["HEB"]
        },
        {
            "name": "James",
            "chapters": 5,
            "description": "Faith and works, practical Christian living; emphasis on righteous behavior, patience, and controlling the tongue. \uea0158\uea02",
            "id": ["JAS"]
        },
        {
            "name": "1 Peter",
            "chapters": 5,
            "description": "Encouragement in suffering, hope in Christ, call to holiness and love within the Christian community. \uea0159\uea02",
            "id": ["1PE"]
        },
        {
            "name": "2 Peter",
            "chapters": 3,
            "description": "Warnings against false teachers; reminders of Christ\u2019s return; emphasize knowledge and godly living. \uea0160\uea02",
            "id": ["2PE"]
        },
        {
            "name": "1 John",
            "chapters": 5,
            "description": "Themes of love, truth, fellowship; tests of genuine faith; Christ\u2019s incarnation and victory over evil. \uea0161\uea02",
            "id": ["1JHN"]
        },
        {
            "name": "2 John",
            "chapters": 1,
            "description": "Short letter about walking in truth, love, and obedience; warning against false teaching. \uea0162\uea02",
            "id": ["2JHN"]
        },
        {
            "name": "3 John",
            "chapters": 1,
            "description": "Personal letter emphasizing hospitality, faithfulness; contrasts good and bad leadership. \uea0163\uea02",
            "id": ["3JHN"]
        },
        {
            "name": "Jude",
            "chapters": 1,
            "description": "Letter warning against false teachers, calling believers to contend for the faith, emphasizing mercy and judgement. \uea0164\uea02",
            "id": ["JUD"]
        },
        {
            "name": "Revelation",
            "chapters": 22,
            "description": "Visions, symbolic prophetic imagery about the end times; the final judgment; new heavens and new earth; encouragement for perseverance. \uea0165\uea02",
            "id": ["REV"]
        }
        ]
                 }):
                     Compiler().update_bible()                        
 
                
if __name__ == "__main__":
    unittest.main()
