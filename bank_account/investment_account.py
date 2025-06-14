""""gi
Description: InvestmentAccount Class.
Author: {Tong Xu}
Date: {2024.10.2}
"""
from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintain InvestmentAccount data
    Attributes:
        TEN_YEARS_AGO(date): The TEN_YEARS_AGO constant of date type will be calculated to the current date minus ten years using the following formula
        management_fee(float): a flat-rate fee the bank charges for managing an InvestmentAccount
    Methods:
        __init__(): Initializes investmentAccount instance.
        __str__(): Returns a string representation of investmentAccount.
        get_service_charges(): Calculate the service charge for investmentAccount.

    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    

    def __init__(self,account_number:int, client_number:int, balance:float, date_created:date, management_fee:float):
        """
        Initialize a investmentaccount object
        Args:
            management_fee(float):A float which stores a flat-rate fee the bank charges for managing an InvestmentAccount
        """
        super().__init__(account_number,client_number,balance,date_created)

        self.__service_charge = ManagementFeeStrategy(date_created, management_fee)


        # Validate the management fee can be converted to a float
        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

    def __str__(self):
        """
        Returns a string formatted representation of investment object
        """
        if self._date_created >= self.TEN_YEARS_AGO:

            return(super().__str__()
                   + f"\nDate Created: {self._date_created}"
                   + f" Management Fee: ${self.__management_fee:.2f}"
                   + "\nAccount Type: Investment")
        else:
            return(super().__str__()
                   + f"\nDate Created: {self._date_created}"
                   + " Management Fee: Waived"
                   + "\nAccount Type: Investment")
    
    def get_service_charges(self):
        """
        Calculate the service charages based on years
        """
        return self.__service_charge.calculate_service_charges(self)
        

        

