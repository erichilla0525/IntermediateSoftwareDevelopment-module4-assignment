"""
Description: {OverdraftStrategy class}
Author: {Tong Xu}
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class OverdraftStrategy(ServiceChargeStrategy):
    """
    A class for the overdraft strategy.
    Attributes:
        overdraft_limit(float): The limit of balance that applies the overdraft rate.
        overdraft_rate(float): The rate of overdraft that applies to given account with a balance less than the overdraft limit.
    Methods:
        calculate_service_chargs(account: BankAccount): Calculate the service chargs based on the account balance of given bank account.

    """
    
    
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize a instance of overdraftstrategy class with given overdraft limit and overdraft rate.
        Args:
            overdraft_limit(float): The limit of balance that applies the overdraft rate.
            overdraft_rate(float): The rate of overdraft that applies to given account with a balance less than the overdraft limit.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges based on the account balance of the given account.
        Args:
            account(BankAccount): The account that applies to the calculate service chargs.
        Return:
            A float that represent the result of calculate service charges.
        """
        if account.balance >= self.__overdraft_limit:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge + (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        


