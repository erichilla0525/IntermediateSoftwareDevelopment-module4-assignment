"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Tong Xu}
Date: {2024.9.12}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankaccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100,200,300.55)
    
    # Attributes are set to input values
    def test_attribute_are_set_to_input_values(self):
        self.assertEqual(100,self.account.account_number)
        self.assertEqual(200,self.account.client_number)
        self.assertEqual(300.55,self.account.balance)

    # Balance attribute set to 0 when non-numeric balance argument
    def test_balance_attribute_set_to_0_when_balance_is_non_numeric(self):
        account1 = BankAccount(100,200,"abc")
        self.assertEqual(account1.balance,0)

    # ValueError when non-numeric account number
    def test_ValueError_when_non_numeric_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount("abc",200,300.55)

    # ValueError when non-numeric client number
    def test_ValueError_when_non_numeric_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(100,"abc",300.55)

    # test account_number (getter)
    def test_account_number_getter(self):
        account = BankAccount(100,200,300.55)
        self.assertEqual(account.account_number,100)

    # test client_number (getter)
    def test_client_number_getter(self):
        account = BankAccount(100,200,300.55)
        self.assertEqual(account.client_number,200)

    # test balance (getter)
    def test_balance_getter(self):
        account = BankAccount(100,200,300.55)
        self.assertEqual(account.balance,300.55)

    # update_balance(positive)
    def test_update_balance_positive(self):
        account = BankAccount(100,200,300.55)
        account.update_balance(100.00)
        self.assertEqual(400.55,account.balance)

    # update_balance(negative)
    def test_update_balance_negative(self):
        account = BankAccount(100,200,300.55)
        account.update_balance(-100.00)
        self.assertEqual(200.55,account.balance)

    # update_balance(non-numeric)
    def test_update_balance_non_numeric(self):
        account = BankAccount(100,200,300.55)
        account.update_balance("abc")
        self.assertEqual(300.55,account.balance)

    # balance correctly updated when deposit a valid amount
    def test_balance_correctly_updated_when_deposit_a_valid_amount(self):
        account = BankAccount(100,200,300.55)
        account.deposit(100.00)
        self.assertEqual(account.balance,400.55)
        
    # ValueError when negative deposit amount is provided
    def test_negative_deposit_amount(self):
        account = BankAccount(100,200,300.55)
        with self.assertRaises(ValueError):
            account.deposit(-100.00)

    # BankAccount object's balance is updated correctly when a valid amount is provided
    def test_balance_updated_correctly_when_withdraw_amount_is_valid(self):
        account = BankAccount(100,200,300.55)
        account.withdraw(100.00)
        self.assertEqual(200.55,account.balance)

    # ValueError when negative withdraw amount is provided.
    def test_negative_withdraw_amount(self):
        account = BankAccount(100,200,300.55)
        with self.assertRaises(ValueError):
            account.withdraw(-100.00)

    # ValueError when exceed amount limit
    def test_withdraw_amount_over_balance(self):
        account = BankAccount(100,200,300.55)
        with self.assertRaises(ValueError):
            account.withdraw(500.00)

    # Verify str method returns to correct format
    def test_str_method_returns_to_correct_format(self):
        account = BankAccount(100,200,300.55)
        self.assertEqual(str(account),"Account Number: 100 Balance: $300.55")