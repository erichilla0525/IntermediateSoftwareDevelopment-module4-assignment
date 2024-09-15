"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Tong Xu}
Date: {2024.9.11}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from email_validator import validate_email,EmailNotValidError
from client.client import client

class TestClient(unittest.TestCase):
    
    # test invalid input
    def test_invalid_input(self):
        client1 = client(525,"Daniel","Chinchilla","erichilla0525@gmail.com")

        self.assertEqual(525,client1.client_number)
        self.assertEqual("Daniel",client1.first_name)
        self.assertEqual("Chinchilla",client1.last_name)
        self.assertEqual("erichilla0525@gmail.com",client1.email_address)

    # test invalid client number
    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            client("abc","Daniel","Chinchilla","erichilla0525@gmail.com")
        
    # test first name is blank
    def test_first_name_is_blank(self):
        with self.assertRaises(ValueError):
            client("525","","Chinchilla","erichilla0525@gmail.com")

    # test last name is blank
    def test_last_name_is_blank(self):
        with self.assertRaises(ValueError):
            client("525","Daniel","","erichilla0525@gmail.com")

    # test email address is valid
    def test_email_address_is_invalid(self):
        with self.assertRaises(ValueError):
            client("525","Daniel","Chinchilla","invalid email address")

    # test str medthod that returns to the right format
    def test_str_method_returns_format(self):
        client1 = client(525,"Daniel","Chinchilla","erichilla0525@gmail.com")
        self.assertEqual(str(client1),"Chinchilla, Daniel [525] - erichilla0525@gmail.com")