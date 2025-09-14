# Author: Ofori George
# Commencement Date: Saturday 13 September,, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/


"""A script that contains the exception classes for the verse"""

import sys
import pathlib

script_dir = pathlib.Path(__file__).parent
sys.path.append(str(script_dir))


class VerseNotFoundError(IndexError):
    """An exception class that is raised when slice or index is less than
    or equal to zero, or greater than the length of the verse"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message
