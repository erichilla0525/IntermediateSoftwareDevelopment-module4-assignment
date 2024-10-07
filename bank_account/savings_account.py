""""
Description: Savings_account Class.
Author: {Tong Xu}
Date: {2024.10.2}
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Maintain InvestmentAccount data
    Attributes:
        account_number(int):
        client_number(int):
        balance:(float):
        date_created(date):
        SERVICE_CHARGE_PREMIUM:(float=2.0):
        minimum_balance:(float): The minimum balance for the saving account
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self,account_number:int, client_number:int, balance:float, date_created:date, minimum_balance:float):
        """
        Initialize a SavingsAccount object
        Args:
            account_number(int):
            client_number(int):
            balance:(float):
            date_created(date):
            minimum_balance:(float)
        """
        super().__init__(account_number,client_number,balance,date_created)


        # Validate that minimum balance can be converted to a float
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50

    def __str__(self):
        """
        Returns a string formatted representation of savingsaccount object
        """
        return(super().__str__()
            + f"\nMinimum Balance: ${self.__minimum_balance:.2f} Account Type: Savings")
    
    def get_service_charges(self):
        """
        Calculate the service charges based on minimum balance
        """
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        
