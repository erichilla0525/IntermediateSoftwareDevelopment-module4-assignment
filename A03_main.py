"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Tong Xu}
Date: {2024-10-23}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client


# 2. Create a Client object with data of your choice.
client1 = Client(client_number=123, first_name="Daniel", last_name="San", email_address="erichilla0525@gmail.com")


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.

chequingaccount = ChequingAccount(account_number=456, client_number=123, balance=1000.00, date_created=date(2020,5,25), overdraft_limit=500.00, overdraft_rate=0.1)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savingsaccount1 = SavingsAccount(account_number=789, client_number=123, balance=500.00, date_created=date(2020,5,25), minimum_balance=300.00)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequingaccount.attach(client1)
savingsaccount1.attach(client1)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(client_number=321, first_name="Henry", last_name="Hu", email_address="dkmd251@163.com")
savingsaccount2 = SavingsAccount(account_number=987, client_number=321, balance=300.00, date_created=date(2021,12,12), minimum_balance=200.00)

savingsaccount2.attach(client2)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
    chequingaccount.deposit(10000)
    chequingaccount.withdraw(200)
    chequingaccount.withdraw(10000)
except Exception as e:
    print (f"ChequingAccount error: {e}")


try:
    savingsaccount1.deposit(300)
    savingsaccount1.deposit(1000)
    savingsaccount1.withdraw(1780)
except Exception as e:
    print (f"SavingAccount error: {e}")


try:
    savingsaccount2.deposit(20000)
    savingsaccount2.withdraw(280)
    savingsaccount2.withdraw(20000)
except ValueError as ve:
    print (f"SavingAccount error: {ve}")




