"""
Description: {description of the file.}
Author: {student name}
"""

from abc import abstractmethod, ABC
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    """
    Base_Service_Charge = 0.50
    
    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        """
        pass
