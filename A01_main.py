""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: {Tong Xu}
Date: {2024-10-5}
"""
from bank_account.bank_account import BankAccount
from client.client import client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.

    client1 = client(525,"Daniel","Chinchilla","erichilla0525@gmail.com")

    # 2. Declare a BankAccount object with an initial value of None.
    account1 = None
    
    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    account1 = BankAccount(100,client1.client_number,1000.55)
    
    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        account = BankAccount(101,client1.client_number,"invalid balance")
    except ValueError as e:
        print(f"Invalid balance:{e}")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Client detail:{client1}")
    print(f"BackAccount detail:{account1}")


    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        account1.deposit("abc")
    except ValueError as e:
        print(f"Invalid deposit amount: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        account1.deposit(-100.00)
    except ValueError as e:
        print(f"Invalid deposit amount: {e}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 

    account1.withdraw(100.00)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        account1.withdraw("abc")
    except ValueError as e:
        print(f"Invalid withdraw amount: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        account1.withdraw(-100)
    except ValueError as e:
        print(f"Invalid withdraw amount: {e}")

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        account1.withdraw(5000)
    except ValueError as e:
        print(f"Invalid withdraw amount(exceed account balance):{e}")
 
    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(f"Final account status: {account1}")
  
if __name__ == "__main__":
    main()