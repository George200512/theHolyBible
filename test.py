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

from bible import Compiler, Bible

#A class for the compiler unnitest 
class TestCompiler(unittest.TestCase):
    """The class for the compiler testcase""" 
    
    @patch("bible.utils")
    @patch("bible.rq.get")
    def test___init__(self, mock_get, mock_utils):
        """A method for testing if the initial routines that are supposed to take place
        when a compiler class is initiated"""
        
        mock_utils.get_settings.return_value = {"VERSIONS": None}
        fake_data = {
        "data": [ {
            "id": "1234abcd5678efgh9012ijkl",
            "name": "King James Version",
            "abbreviation": "KJV",
            "language": {
                "id": "eng",
                "name": "English"
            },
            "countries": [
                {"name": "United States"}
            ],
            "type": "Bible",
            "updatedAt": "2025-01-01T00:00:00.000Z"
        }]
        }
        
        mock_response = MagicMock()
        mock_response.json.return_value = fake_data
        mock_get.return_value = mock_response
        compiler = Compiler()
        mock_get.assert_called_once()
        self.assertEqual(mock_utils.set_settings.call_count, 2)
        self.assertTrue(hasattr(compiler, "data"))
        self.assertEqual(compiler.data[0]["id"], "1234abcd5678efgh9012ijkl")
        
        
if __name__ == "__main__" :
    unittest.main()