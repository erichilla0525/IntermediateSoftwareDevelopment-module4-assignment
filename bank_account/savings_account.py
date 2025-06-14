""""
Description: Savings_account Class.
Author: {Tong Xu}
Date: {2024.10.2}
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Maintain InvestmentAccount data
    Attributes:
        SERVICE_CHARGE_PREMIUM:(float=2.0): The SERVICE_CHARGE_PREMIUM constant is set to a flat rate of 2.00. 
        That is, a SavingsAccounts will incur 2 times the BASE_SERVICE_CHARGE when the balance drops below the minimum_balance.
        minimum_balance:(float): The minimum value a balance can be before further service charges are applied.
    Methods:
        __init__(): Initializes a SavingAccount instance.
        __str__(): Returns to a string representation of SavingAccount.
        get_service_charges(): Calculate the service charge of saving account.
    """


    def __init__(self,account_number:int, client_number:int, balance:float, date_created:date, minimum_balance:float):
        """
        Initialize a SavingsAccount object
        Args:
            minimum_balance:(float): A float that represent the minimum value a balance can be before further service charges are applied.
        """
        super().__init__(account_number,client_number,balance,date_created)

        self.__service_charge = MinimumBalanceStrategy(minimum_balance)


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
        return self.__service_charge.calculate_service_charges(self)
        
