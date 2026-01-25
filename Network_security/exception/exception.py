import sys
from types import ModuleType
from Network_security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        
        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = 0
            self.file_name = "Unknown" 
    
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))