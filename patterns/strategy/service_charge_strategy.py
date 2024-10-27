"""
Description: {description of the file.}
Author: {student name}
"""

from abc import abstractmethod, ABC
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for service charge strategies applied to bank accounts.
    Attributes:
        Base_Service_Charge(float): The base service charge that applies the bank accounts.
    Methods:
        calculate_service_chargs(account: BankAccount): Calculate service charge for the given account.


    """
    Base_Service_Charge = 0.50
    
    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate service charge for the given account.
        Args:
            account(BankAccount): The account for that service charge been calculated.
        Return:
            A float that represent the result of service charge calculation.

        """
        pass
