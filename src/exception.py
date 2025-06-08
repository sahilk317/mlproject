import sys
from src.logger import logging

def error_message(error,error_detail:sys):
    """
    This function is used to format the error message.
    :param error: Exception object
    :param error_detail: sys module
    :return: formatted error message
    """

    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f'Error occured in script: {file_name} at line number: {line_number} with error message: {str(error)}'

    return error_message





class CustomException(Exception):
    """
    Custom Exception class to handle exceptions in the application.
    """

    def __init__(self,error,error_detail:sys):
        """
        Constructor for CustomException class.
        :param error_message: Error message to be displayed
        :param error_detail: sys module
        """
        super().__init__(str(error))
        self.error_message = error_message(error,error_detail=error_detail)


    def __str__(self):
        """
        String representation of the CustomException class.
        :return: formatted error message
        """
        return self.error_message 



if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys) 
    
