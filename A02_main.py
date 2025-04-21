"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Tong Xu}
Date: {2024-10-5}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from bank_account.savings_account import SavingsAccount
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequingAccount1 = ChequingAccount(12345,678,200,date(2020,5,25),300,0.1)


# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequingAccount1)
try:
    service_charge = chequingAccount1.get_service_charges()
    print(f"Calculated Service Charges:{service_charge:.2f}")
except ValueError as ve:
    print(f"Calculated Service Charges error:{ve}")



# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
try:
    chequingAccount1.deposit(500)
    print(chequingAccount1)
except ValueError as ve:
    print(f"Deposit error occures{ve}")
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    service_charge = chequingAccount1.get_service_charges()
    print(f"Calculated Service Charges:{service_charge:.2f}")
except ValueError as ve:
    print(f"Calculated Service Charges error:{ve}")



print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savingAccount1 = SavingsAccount(3055,4187,300,date(2020,5,25),200)
    print(savingAccount1)
except ValueError as ve:
    print(f"Error Occurs:{ve}")

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    service_charge1 = savingAccount1.get_service_charges()
    print(f"Calculated Service Charge:{service_charge1:.2f}")
except ValueError as ve:
    print(f"Error Occurs:{ve}")
    
# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
try:
    savingAccount1.withdraw(250)
    print(savingAccount1)
except ValueError as ve:
    print(f"Withdraw Error Occurs")
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    service_charge1 = savingAccount1.get_service_charges()
    print(f"Calculated Service Charge:{service_charge1:.2f}")
except ValueError as ve:
    print(f"Error Occurs:{ve}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
# 9a. Print the InvestmentAccount created in step 8.
try:
    investmentAccount1 = InvestmentAccount(1212,2021,300,date(2021,12,12),5)
    print(investmentAccount1)
except ValueError as ve:
    print(f"Error Occurs:{ve}")

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    service_charge2 = investmentAccount1.get_service_charges()
    print(f"Calculated Service Charges:{service_charge2:.2f}")
except ValueError as ve:
    print(f"Error Occurs:{ve}")


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

# 11a. Print the InvestmentAccount created in step 10.
try:
    investmentAccount2 = InvestmentAccount(1212,2021,300,date(2011,12,12),5)
    print(investmentAccount2)
except ValueError as ve:
    print(f"Error Occurs:{ve}")
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    service_charge3 = investmentAccount2.get_service_charges()
    print(f"Calculated Service Charges:{service_charge3:.2f}")
except ValueError as ve:
    print(f"Error Occurs:{ve}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequingAccount1.withdraw(chequingAccount1.get_service_charges())
    savingAccount1.withdraw(savingAccount1.get_service_charges())
    investmentAccount1.withdraw(investmentAccount1.get_service_charges())
    investmentAccount2.withdraw(investmentAccount2.get_service_charges())
except ValueError as ve:
    print(f"Error Occurs:{ve}")


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequingAccount1)
print(savingAccount1)
print(investmentAccount1)
print(investmentAccount2)

