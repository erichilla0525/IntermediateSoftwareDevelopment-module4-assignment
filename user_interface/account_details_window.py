from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A Python class which allows users perform bank account transactions. 
    This class is meant to work in conjunction with the BankAccount class such that deposit and withdraw functionality may be used.

    Initializes the Transaction window by adding various widgets and setting properties. 
    Widgets include: accountNumberLabel, balanceLabel, transactionAmountEdit, depositButton, withdrawButton and exitButton.
    
    Methods:
        __init__(account): Initializes the transaction window with the given bank account.
        __on_apply_transaction(): handles both deposit and withdraw functions.
        __on_exit(): Closes the transaction window.
    """
    balance_update = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        # Evaluate the received account parameter to ensure it is an instance of BankAccount.
        if not isinstance(account, BankAccount):
            self.reject()
            return
        
        # Set the account attribute to a copy of the received parameter value.
        self.account = copy.copy(account)

        # Use the setText method to populate the account_number_label 
        # and balance_label
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(str(self.account.balance))

        # Establish a connection between the deposit_button's clicked event and 
        # the on_apply_transaction method.
        self.deposit_button.clicked.connect(self.__on_apply_transaction)

        # Establish a connection between the withdraw_button's clicked event and 
        # the on_apply_transaction method.
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)

        # Establish a connection between the exit_button's clicked event and 
        # the on_exit method.
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self):
        """
        Method that handle both deposit and withdraw functions.
        """
        try:
            transaction_amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(transaction_amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(transaction_amount)
        
            self.balance_label.setText(f"${self.account.balance:.2f}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            
            # Emit a signal passing the updated account attribute
            self.balance_update.emit(self.account)

        except Exception as e:
            QMessageBox(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
    
    def __on_exit(self):
        """
        Closes the transaction amount window.
        """
        self.close()


