from email_validator import validate_email,EmailNotValidError

""""
Description: Client Class.
Author: {Tong Xu}
Date: {2024.9.10}
"""

from utility.file_utils import simulate_send_email
from datetime import datetime

class Client:
    """
    Client: For containing client dat
    Attributes:
        __client_number(int): An integer value representing the client number
        __first_name(str): A string value the client's first name
        __last_name(str): A string value the client's last name
        __email_address(str):  A string value the client's email address
    """

    def __init__(self,client_number:int,first_name:str,last_name:str,email_address:str):
        """
        init: Initialize a class of attribute with args value
        Args:
            client_number(int): An integer value representing the client number
            first_name(str): A string value the client's first name
            last_name(str): A string value the client's last name
            email_address(str): A string value the client's email address
        """
        # Validate if client number is not integer
        if not isinstance(client_number,int):
            raise ValueError("Client number is not an integer")
        self.__client_number = client_number

        # Validate the first name is not blank
        if len(first_name.strip()) == 0:
            raise ValueError("First name can not be blank")
        self.__first_name = first_name
        
        # Validate the last name is not blank
        if len(last_name.strip()) == 0:
            raise ValueError("Last name can not be blank")
        self.__last_name = last_name

        # Validate the deliverability of email address
        try:
            email_Validation = validate_email(email_address,check_deliverability =  False)
            self.email_address = email_Validation.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    # Add property for client number
    @property
    def client_number(self):
        """
        Accessor for client number
        """
        return self.__client_number
    
    # Add property for first name
    @property
    def first_name(self):
        """
        Accessor for the first name
        """
        return self.__first_name
    
    # Add property for last name
    @property
    def last_name(self):
        """
        Accessor for the last name
        """
        return self.__last_name
    
    # Add property for email address
    @property
    def email_address(self):
        """
        Accessor for the email address
        """
        return self.__email_address
    
    # Add setter for email address
    @email_address.setter
    def email_address(self,value):
        self.__email_address = value
    
    # def a _str_ method that returns to a str format
    def __str__(self):
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
    
    
    def update(self, message: str):
        """
        send a message to the client's email address 

        Args:
            message(str): The message notofication that sent to the clients
        """
        #
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        #
        email_message = f"Notification for {self.__client_number}: {self.__first_name} {self.__last_name}: {message}"
        #
        simulate_send_email(self.__email_address, subject, email_message)
    

    