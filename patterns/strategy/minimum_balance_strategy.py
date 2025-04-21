"""
Description: {MinimumBalanceStrategy class}
Author: {Tong Xu}
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A class for the minimum balance strategy.
    Attributes:
        SERVICE_CHARGE_PREMIUM(float): A mutiplier that applied to the base_service_charg if account balance less than the minimum balance.
        minimum_balance(float): The amount of minimum balance that does not need to apply the SERVICE_CHARGE_PREMIUM.

    Methods:
        calculate_service_charges(account: BankAccount): Calculate the service charge based on the account balance.

    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initiazlize an instance of minimum balance strategy with given minimum balance of the account.
        Args:
            minimum_balance(float): Minimum balance of the account that will avoid to apply the SERVICE_CHARGE_PREMIUM multiplier.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charge based on the balance of given account.
        Args:
            account: BankAccount: The bank account that applie the calculation of service charge.
        Return:
            A float that represent the result of service charge calculation.
        """
        if account.balance >= self.__minimum_balance:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge * self.SERVICE_CHARGE_PREMIUM
        
