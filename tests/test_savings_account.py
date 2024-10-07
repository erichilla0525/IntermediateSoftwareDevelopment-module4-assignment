"""
Description: Unit tests for the saving_account class.
Author: ACE Faculty
Modified by: {Tong Xu}
Date: {2024.9.11}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingAcount(unittest.TestCase):
    def setUp(self):
        self.SavingAccount = SavingsAccount(12345,678,200,date(2020,5,25),100)

    # test Attributes are set to parameter values.
    def test_attributes_are_set_to_parameter_values(self):
        self.assertEqual(100,self.SavingAccount._SavingsAccount__minimum_balance)

    # test minimum_balance set to 50 when input value is invalid type.
    def test_minimum_balance_set_to_50_when_input_value_is_invalid_type(self):
        savingAccount1 = SavingsAccount(12345,678,200,date(2020,5,25),"Invalid")
        self.assertEqual(50,savingAccount1._SavingsAccount__minimum_balance)

    # test service charge equals to Base service charge when balance greater than minimum balance
    def test_service_charge_equals_to_Base_service_charge_when_balance_greater_than_minimum_balance(self):
        savingAccount = SavingsAccount(12345,678,200,date(2020,5,25),100)
        self.assertEqual(0.5,savingAccount.get_service_charges())

    # test service charge equals to Base service charge when balance equals to minimum balance
    def test_service_charge_equals_to_Base_service_charge_when_balance_equals_to_minimum_balance(self):
        savingAccount = SavingsAccount(12345,678,200,date(2020,5,25),200)
        self.assertEqual(0.5,savingAccount.get_service_charges())

    # test service charge equals to Base service charge when balance less than minimum balance
    def test_service_charge_equals_to_Base_service_charge_when_balance_less_than_minimum_balance(self):
        savingAccount = SavingsAccount(12345,678,200,date(2020,5,25),300)
        self.assertEqual(1,savingAccount.get_service_charges())

    # test __str__ method should return a formatted string
    def test_str_method_should_return_a_formatted_string(self):
        expected_str = (f"Account Number: 12345 Balance: $200.00"
                        +"\nMinimum Balance: $100.00 Account Type: Savings")
        self.assertEqual(expected_str,str(self.SavingAccount))

