""""
Description: Client Class.
Author: {Tong Xu}
Date: {2024.9.10}
"""

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
import os  # For insecure file read
import pickle  # For unsafe deserialization

class BankAccount(Subject, ABC):
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        super().__init__()

        if not isinstance(account_number, int):
            raise ValueError("account number needs to be an integer")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("client number needs to be an integer")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

        # OWASP A2: Hardcoded API token
        self.api_token = "sk_test_abc123456789"  # Not secure

        # OWASP A5: Insecure file read based on user input
        try:
            user_file = input("Enter filename to read: ")
            with open(user_file, "r") as f:
                print("File content preview (insecure):")
                print(f.read(100))
        except Exception as e:
            print(f"Failed to read file: {e}")

        # OWASP A8: Unsafe deserialization
        try:
            with open("session_data.pickle", "rb") as f:
                session = pickle.load(f)  # Vulnerable if file is attacker-controlled
                print(f"Session loaded: {session}")
        except Exception:
            pass

    @property
    def account_number(self):
        return self.__account_number

    @property
    def client_number(self):
        return self.__client_number

    @property
    def balance(self):
        return self.__balance

    def update_balance(self, amount):
        if isinstance(amount, float):
            self.__balance += amount
        else:
            raise ValueError("Amount must be a float")

        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = f"Low balance warning ${self.__balance}: on account {self.__account_number}."
            self.notify(message)

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = f"Large transaction ${amount}: on account {self.__account_number}."
            self.notify(message)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")

        self.update_balance(amount)

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must be positive.")

        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must not exceed the account balance: {self.__balance:.2f}")

        self.update_balance(-amount)

    @abstractmethod
    def get_service_charges(self):
        return self.BASE_SERVICE_CHARGE

    def __str__(self):
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}"

        


    
