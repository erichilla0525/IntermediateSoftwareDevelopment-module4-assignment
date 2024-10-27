"""
Description: {description of the file.}
Author: {student name}
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class OverdraftStrategy(ServiceChargeStrategy):
    """
    """
    
    
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        """
        if account.balance >= self.__overdraft_limit:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge + (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        


