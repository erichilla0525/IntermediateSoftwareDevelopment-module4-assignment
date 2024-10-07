"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Tong Xu}
Date: {2024.10.1}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.chequeaccount1 = ChequingAccount(12345,678,1000.00,date(2024,10,1),300,0.10)
    
    # Test attributes are set to input values
    def test_attributes_are_set_to_input_values(self):
        self.assertEqual(12345,self.chequeaccount1.account_number)
        self.assertEqual(date(2024,10,1),self.chequeaccount1._date_created)
        self.assertEqual(678,self.chequeaccount1.client_number)
        self.assertEqual(1000.00,self.chequeaccount1.balance)
        self.assertEqual(300,self.chequeaccount1._ChequingAccount__overdraft_limit)
        self.assertEqual(0.10,self.chequeaccount1._ChequingAccount__overdraft_rate)

    # Test overdraft limit has invalid type returns to -100
    def test_overdraft_limit_has_invalid_type(self):
        cheque2 = ChequingAccount(12345,678,1000.00,date(2024,10,1),"Invalid limit","Invalid rate")
        self.assertEqual(-100,cheque2._ChequingAccount__overdraft_limit)

    # Test overdraft rate has invalid type returns to 0.05
    def test_overdraft_rate_has_invalid_type(self):
        cheque = ChequingAccount(12345,678,1000.00,date(2024,10,1),"Invalid limit","Invalid rate")
        self.assertEqual(0.05,cheque._ChequingAccount__overdraft_rate)

    # Test date created has invalid type will return to the date of today
    def test_date_created_has_invalid_type(self):
        cheque = ChequingAccount(12345,678,1000.00,"Invalid date",300,0.10)
        self.assertEqual(cheque._date_created,date.today())

    # Test service charge is set to the BASE_SERVICE_CHARGE value when balance greater than overdraft limit
    def test_service_charge_is_set_to_the_BASE_SERVICE_CHARGE_value_when_balance_greater_than_overdraft_limit(self):
        self.assertEqual(self.chequeaccount1.get_service_charges(),self.chequeaccount1.BASE_SERVICE_CHARGE)

    # Test service charge is set correctly when balance less than overdraft lmit
    def test_service_charge_is_set_correctly_when_balance_less_than_overdraft_lmit(self):
        cheque = ChequingAccount(12345,678,200.00,date(2024,10,1),300,0.10)
        expected_value = cheque.get_service_charges()
        actual_value = cheque.BASE_SERVICE_CHARGE + (300-200) * 0.10
        self.assertEqual(expected_value,round(actual_value,2))

    # Test service charge is set to the BASE_SERVICE_CHARGE when balance equal to overdraft limit
    def test_service_charge_is_set_to_the_BASE_SERVICE_CHARG_Ewhen_balance_equal_to_overdraft_limit(self):
        cheque = ChequingAccount(12345,678,300.00,date(2024,10,1),300,0.10)
        self.assertEqual(cheque.get_service_charges(),cheque.BASE_SERVICE_CHARGE)

    # Test appropriate str value returned based on attribute values.
    def test_appropriate_str_value_returned_based_on_attribute_values(self):
        expected_str = ("Account Number: 12345 Balance: $1000.00"
                        "\nOverdraft Limit: $300.00 Overdraft Rate: 10.00%"
                        "\nAccount Type: Chequing")
        actual_str = str(self.chequeaccount1)
        self.assertEqual(expected_str,actual_str)