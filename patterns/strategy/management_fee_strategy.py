"""
Description: {description of the file.}
Author: {student name}
"""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.Base_Service_Charge
        else:
            return self.Base_Service_Charge + self.__management_fee
