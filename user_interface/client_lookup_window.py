from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from client.client import Client
from typing import Dict

class ClientLookupWindow(LookupWindow):
    """
    A class which allows users to retrieve Client information.

    Initializes the Lookup Window by adding various widgets and setting properties. 
    Widgets include: clientNumberEdit, clientInfoLabel, lookupButton and accountTable.
    """
    def __init__(self):
        """
        Initializes the Lookup Window by adding various widgets and setting properties. 
        Widgets include: clientNumberEdit, clientInfoLabel, lookupButton and accountTable.
        """
        # Execute the super class __init__ method to perform all super class initializations.
        super().__init__()
        data = load_data()
        self.client_listing: Dict[int, Client] = data[0] 
        self.accounts: Dict[int, BankAccount] = data[1]   

        self.lookup_button.clicked.connect(self.on_lookup_client)

        self.account_table.cellClicked.connect(self.on_select_account)

        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        
    @Slot()
    def __on_text_changed(self):
        self.account_table.setRowCount(0)
    
    def on_lookup_client(self):
        """
        """

        # Obtain the client number entered into the the client_number_edit widget and convert 
        # the data to an int.
        try:
            client_number = int(self.client_number_edit.text())
        except Exception as e:
            QMessageBox.warning(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return
        

        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        else:
            client = self.client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

            self.account_table.setRowCount(0)

            # Iterate through the accounts dictionary values
            for account in self.accounts.values():
                if account.client_number == client_number:
                    row_position = self.account_table.rowCount()
                    self.account_table.insertRow(row_position)
                    self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                    self.account_table.setItem(row_position, 1, QTableWidgetItem(f"{account.balance:.2f}"))
                    self.account_table.setItem(row_position, 2, QTableWidgetItem(str(account._date_created)))
                    self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))
            # Ensure that none of the data in the table is truncated.
            self.account_table.resizeColumnsToContents()

    @Slot(int, int)
    def on_select_account(self, row: int, column: int) ->None:
        """
        """
        account_number = self.account_table.item(row, 0)

        if account_number.text() == "":
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return
        
        # Convert the selected account number to an integer
        try:
            account_number = int(account_number.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid account number", "Account number is invalid.")
            return
        
        # If the selected account_number does not reside in the accounts dictionary:
        if account_number not in self.accounts:
            QMessageBox.warning(self, "No bank account", "Bank account selected does not exist.")
            return
        
        # Obtain the BankAccount object which corresponds with the account_number key
        account = self.accounts[account_number]

        # Create an instance of the AccountDetailsWindow (class) passing the BankAccount object.
        account_detail_window = AccountDetailsWindow(account)

        account_detail_window.balance_update.connect(self.update_data)
        account_detail_window.exec()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount):
        """
        """
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if int(account_number_item.text()) == account.account_number:
                # Update the value of the second column
                self.account_table.setItem(row, 1, QTableWidgetItem(f"{account.balance:.2f}"))

                # Update the appropriate entry in the accounts dictionary 
                # with the updated BankAccount.
                self.accounts[account.account_number] = account

                # Invoke the update_data function of the manage_data module
                # passing the updated BankAccount.
                update_data(account)
                




        



        
