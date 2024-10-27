"""
Description: {description of the file.}
Author: {student name}
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        """
        if account.balance >= self.__minimum_balance:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge * self.SERVICE_CHARGE_PREMIUM
        
