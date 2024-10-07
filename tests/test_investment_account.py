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
from bank_account.investment_account import InvestmentAccount
from datetime import date

class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        self.InvestAccount1 = InvestmentAccount(12345,678,300.00,date(2010,5,25),5)

    # test attributes are set to parameter values.
    def test_attributes_are_set_to_parameter_values(self):
        self.assertEqual(12345,self.InvestAccount1.account_number)
        self.assertEqual(678,self.InvestAccount1.client_number)
        self.assertEqual(300.00,self.InvestAccount1.balance)
        self.assertEqual(date(2010,5,25),self.InvestAccount1._date_created)
        self.assertEqual(5,self.InvestAccount1._InvestmentAccount__management_fee)

    # test management fee convert to a float when input value is invalid type.
    def test_management_fee_convert_to_a_float_when_input_value_is_invalid_type(self):
        investmentaccount = InvestmentAccount(12345,678,300.00,date(2020,5,25),"abc")
        self.assertEqual(2.55,investmentaccount._InvestmentAccount__management_fee)

    # test service when date created more than 10 years ago
    def test_service_when_date_created_more_than_10_years_ago(self):
        investmentaccount = InvestmentAccount(12345,678,300.00,date(2010,5,25),5)
        self.assertEqual(investmentaccount.get_service_charges(),InvestmentAccount.BASE_SERVICE_CHARGE)

    # test service when date created less than 10 years ago
    def test_service_when_date_created_not_more_than_10_years_ago(self):
        investmentaccount = InvestmentAccount(12345,678,300.00,date(2020,5,25),5)
        self.assertEqual(investmentaccount.get_service_charges(),InvestmentAccount.BASE_SERVICE_CHARGE + investmentaccount._InvestmentAccount__management_fee)

    # test service when date created is excactly 10 years ago
    def test_service_when_date_created_is_excatly_10_years_ago(self):
        investmentaccount = InvestmentAccount(12345,678,300.00,date(2014,10,4),5)
        self.assertEqual(investmentaccount.get_service_charges(),InvestmentAccount.BASE_SERVICE_CHARGE + investmentaccount._InvestmentAccount__management_fee)

    # test correctly displays waived management fee when date created more than 10 years ago.
    def test_correctly_displays_waived_management_fee_when_date_created_more_than_10_years_ago(self):
        expected_str = ("Account Number: 12345 Balance: $300.00"
                        "\nDate Created: 2010-05-25 Management Fee: Waived"
                        "\nAccount Type: Investment")
        self.assertEqual(expected_str,str(self.InvestAccount1))

    # test correctly displays management fee when date created within last 10 years.
    def test_correctly_displays_waived_management_fee_when_date_created_more_than_10_years_ago(self):
        investmentaccount = InvestmentAccount(12345,678,300.00,date(2020,10,1),5)
        expected_str = ("Account Number: 12345 Balance: $300.00"
                        "\nDate Created: 2020-10-01 Management Fee: $5.00"
                        "\nAccount Type: Investment")
        self.assertEqual(expected_str,str(investmentaccount))



