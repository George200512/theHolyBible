# Author: Ofori George
# Commencement Date: Saturday 4 October, 2025.
# Telephone / WhatsApp: (+233)504694485
# Facebook: Street Python
# Email: georgeofori2005@gmail.com
# website: not ready yet
# github: https://www.github.com/George200512/

"""A script to define the exception classes for the bible class"""

import requests.exceptions as rexc

# The bible error class
class BibleNotAvailableError(Exception):
    """An error to be raised if the bible name is not found in the database"""
    
    def __init__(self, message):
        self. message = message
        super().__init__(message)
        
        
#The class for internet errors
class NonBiblicalError(rexc.RequestException):
    """An errors that is thrown for errors that doesn't concern fetching the bible from database"""
    
    def __init__(self, message):
        self.message = message 
        super().__init__(message)