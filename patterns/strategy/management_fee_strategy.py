"""
Description: {ManagementFeeStrategy class}
Author: {Tong Xu}
"""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A class for the management fee strategy.
    Attribues:
        Ten_YEARS_AGO: Represent the date from 10 years ago.
        date_created(date): Represent the date of account been created.
        management_fee(float): Represent the management fee that will applied to accounts that less than 10 years.

    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initialize a instance of ManagementFeeStrategy with the date that account been created and management fee.
        Args:
            date_created(date): Represent the date that account was created.
            Management_fee(float): Represent the management fee that applied to the accounts less than 10 years.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charge based on the creation date of given account.
        Args:
            account(BankAccount): The bank account that used for calculate the service charges.
        Return:
            The result of calculated service charges.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge + self.__management_fee
