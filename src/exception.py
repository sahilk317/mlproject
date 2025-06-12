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
        super().__init__(error)
        self.error_message = error_message(error,error_detail=error_detail)


    def __str__(self):
        """
        String representation of the CustomException class.
        :return: formatted error message
        """
        return self.error_message 


# import sys
# from src.logger import logging

# def get_error_message_detail(error, error_detail: sys):
#     """
#     Formats a detailed error message with filename and line number.
#     """
#     _, _, exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     line_number = exc_tb.tb_lineno
#     return f"Error occurred in script: {file_name} at line number: {line_number} with error message: {str(error)}"


# class CustomException(Exception):
#     """
#     Custom Exception class to provide detailed error information.
#     """

#     def __init__(self, error, error_detail: sys):
#         super().__init__(error)
#         self.message = get_error_message_detail(error, error_detail)

#     def __str__(self):
#         return self.message
