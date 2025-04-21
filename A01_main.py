from bank_account.bank_account import BankAccount
from client.client import client

def main():
    client1 = client(525, "Daniel", "Chinchilla", "erichilla0525@gmail.com")

    # OWASP A1: Code injection
    user_input = input("Enter Python code to evaluate: ")  # Dangerous
    result = eval(user_input)
    print(f"Evaluated result: {result}")

    account1 = BankAccount(100, client1.client_number, 1000.55)

    # OWASP A2: Hardcoded credentials
    password = "123456"  # Hardcoded password
    print(f"Using hardcoded password for login: {password}")

    try:
        account = BankAccount(101, client1.client_number, "invalid balance")
    except ValueError as e:
        print(f"Invalid balance: {e}")

    print(f"Client detail: {client1}")
    print(f"BackAccount detail: {account1}")

    try:
        account1.deposit("abc")
    except ValueError as e:
        print(f"Invalid deposit amount: {e}")

    try:
        account1.deposit(-100.00)
    except ValueError as e:
        print(f"Invalid deposit amount: {e}")

    # OWASP A5: Missing exception handling
    account1.withdraw(5000)

    print(f"Final account status: {account1}")

if __name__ == "__main__":
    main()
