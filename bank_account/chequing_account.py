""""
Description: ChequingAccount Class.
Author: {Tong Xu}
Date: {2024.10.2}
"""

from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    chequing_account class: Maintain chequing account data. 
    Attributes:
        overdraft_limit(float): The maximum amount a balance can be overdrawn (below 0.00) before overdraft fees are applied
        overdraft_rate(float): The rate to which overdraft fees will be applied
    """
    def __init__(self, account_number:int, client_number:int, balance:float, 
                 date_created:date, overdraft_limit:float, overdraft_rate:float):
        """
        Initilize a chequing account object
        Args:
            account(int):
            client_number(int):
            balance:(float):
            date_created(date):
            overdraft_limit(float):
            overdraft_rate(float):
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate overdraft limit can be converted to float
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100

        # Validate overdraft rate can be converted to float
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

    def __str__(self):
        """
        Returns to a string format of chequing object.
        """
        return (super().__str__()
                + f"\nOverdraft Limit: ${self.__overdraft_limit:.2f}" 
                + f" Overdraft Rate: {self.__overdraft_rate * 100:.2f}%"
                + "\nAccount Type: Chequing")
    
    def get_service_charges(self):
        """
        Returns to calculated service charge:

        If the balance of the ChequingAccount instance is greater than or equal to the overdraft limit, then the service charge is set to the BASE_SERVICE_CHARGE value.
        If the balance of the ChequingAccount instance is less than the overdraft limit, then the service charge is calculated using the following formula:
        BASE_SERVICE_CHARGE + (overdraft limit - balance) * overdraft rate
        """
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        

  
