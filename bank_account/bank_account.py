""""
Description: Client Class.
Author: {Tong Xu}
Date: {2024.9.10}
"""

class BankAccount:
    """
    BankAcount: For containing BankAccount data
    Attributes:
        __account_number(int): An integer value representing the bank account number.
        __client_number(int): An integer value representing the client number representing the account holder.
        __balance(float): A float value representing the current balance of the bank account.
    """
    def __init__(self, account_number:int, client_number:int, balance:float):
        """
        init: Initialize a class of attribute with args value
        Args:
            account_number(int): An integer value representing the bank account number.
            client_number(int): An integer value representing the client number representing the account holder.
            balance(float): A float value representing the current balance of the bank account.
        """

        # Validate account number is integer
        if not isinstance(account_number,int):
            raise ValueError("account number needs to be an integer")
        self.__account_number = account_number

        # Validate client number is integer
        if not isinstance(client_number,int):
            raise ValueError("account number needs to be an integer")
        self.__client_number = client_number

        # Validate balance is a float number
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0


    # Add property for account number
    @property
    def account_number(self):
        """
        Accessor for account number
        """
        return self.__account_number
    
    # Add property for client number
    @property
    def client_number(self):
        """
        Accessor for client number
        """
        return self.__client_number
    
    # Add property for balance
    @property
    def balance(self):
        """
        Accessor for balance
        """
        return self.__balance
    
    def update_balance(self,amount):
        """
        update_balance: For updating balance of the account
        Args:
            amount: amount has to ba a float number
        """
        if isinstance(amount,float):
            self.__balance += amount
        else:
            raise ValueError("Amount must be a float")

    def deposit(self,amount):
        """
        deposit: Verify if deposit amount is a positive float number
        Args:
            amount: deposit amount has to be a positive float number
        """
        # Verify deposit amount is numeric
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        # Verify deposit amount is positive
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")
        
        # Update the balance if deposit amount is valid
        self.update_balance(amount)


    def withdraw(self,amount):
        """
        withdraw: Verify withdraw amount received is in correct data type
            Args:
                amount: withdraw amount has to be in correct data type
        """
        # Verify withdraw amount is numeric
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        # Verify deposit amount is positive
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must be positive.")
        
        # Verify withdraw amount received not exceed the current balance
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount:.2f} must not exceed the account balance: {self.__balance:.2f}")
        
        # Update the balance if withdraw amount is valid 
        self.update_balance(-amount)

    # def a str method that the balance is displayed to 2 decimal places with currency ($) formatting
    def __str__(self):
        """

        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:.2f}"

        


    