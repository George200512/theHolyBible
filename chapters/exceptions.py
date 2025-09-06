# Author: Ofori George
# Commencement Date: Tuesday 26 August, 2025.
# Telephone / WhatsApp: (+233)04694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/


"""A script that contains the exception classes for the chapter"""

class ChapterNotFoundError(IndexError):
    """An exception class that is raised when slice or index is less than
    or equal to zero, or greater than the length of the chaper"""
    
    def __init__(self, message):
        super().__init__(message)
        super().__init__(messaage)
        self.message = message