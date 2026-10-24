# import random
# from datetime import datetime


# # ============================================================
# # PARENT CLASS
# # ============================================================
# # BankAccount is the parent class.
# # It contains common account-related data and functionalities.
# # ============================================================

# class BankAccount:

#     def __init__(self, username, password, account_number):

#         # Public variable
#         # Stores the customer's username
#         self.username = username

#         # Encapsulation:
#         # __password is private.
#         # It should not be accessed directly outside the class.
#         self.__password = password

#         # __balance is also private.
#         # Initial balance is 0.
#         self.__balance = 0

#         # Stores the unique 9-digit account number
#         self.account_number = account_number

#         # List used to store transaction history
#         self.transactions = []


#     # ========================================================
#     # GET PASSWORD
#     # ========================================================
#     # Since password is private, we use a method to access it.
#     # This is part of Encapsulation.
#     # ========================================================

#     def get_password(self):
#         return self.__password


#     # ========================================================
#     # GET BALANCE
#     # ========================================================
#     # Since balance is private, this method returns the balance.
#     # ========================================================

#     def get_balance(self):
#         return self.__balance


#     # ========================================================
#     # CREDIT / DEPOSIT METHOD
#     # ========================================================

#     def credit(self, amount):

#         # Check whether entered amount is valid
#         if amount > 0:

#             # Increase the account balance
#             self.__balance += amount

#             # Store transaction details
#             transaction = {
#                 "type": "Credit",
#                 "amount": amount,
#                 "date": datetime.now()
#             }

#             # Add transaction to transaction list
#             self.transactions.append(transaction)

#             print("\nAmount Credited Successfully")
#             print("Credited Amount :", amount)
#             print("Current Balance :", self.__balance)

#         else:
#             print("\nInvalid Amount")


#     # ========================================================
#     # DEBIT / WITHDRAW METHOD
#     # ========================================================

#     def debit(self, amount):

#         # Amount should be greater than 0
#         if amount <= 0:
#             print("\nInvalid Amount")

#         # User should have enough balance
#         elif amount > self.__balance:
#             print("\nInsufficient Balance")

#         else:

#             # Reduce balance
#             self.__balance -= amount

#             # Store debit transaction
#             transaction = {
#                 "type": "Debit",
#                 "amount": amount,
#                 "date": datetime.now()
#             }

#             self.transactions.append(transaction)

#             print("\nAmount Debited Successfully")
#             print("Debited Amount :", amount)
#             print("Current Balance :", self.__balance)


#     # ========================================================
#     # BALANCE ENQUIRY
#     # ========================================================

#     def balance_enquiry(self):

#         print("\n================================")
#         print("        BALANCE ENQUIRY")
#         print("================================")

#         print("Account Number :", self.account_number)
#         print("Account Holder :", self.username)
#         print("Available Balance :", self.__balance)


#     # ========================================================
#     # MINI STATEMENT
#     # ========================================================

#     def mini_statement(self):

#         print("\n================================")
#         print("         MINI STATEMENT")
#         print("================================")

#         print("Account Number :", self.account_number)
#         print("Account Holder :", self.username)

#         # Check whether transactions exist
#         if len(self.transactions) == 0:

#             print("\nNo Transactions Available")

#         else:

#             print("\n--------------------------------")
#             print("Type\t\tAmount\t\tDate")
#             print("--------------------------------")

#             # Show only last 5 transactions
#             for transaction in self.transactions[-5:]:

#                 print(
#                     transaction["type"],
#                     "\t\t",
#                     transaction["amount"],
#                     "\t\t",
#                     transaction["date"].strftime("%d-%m-%Y %H:%M:%S")
#                 )

#         print("--------------------------------")
#         print("Available Balance :", self.__balance)


# # ============================================================
# # CHILD CLASS
# # ============================================================
# # SavingsAccount inherits from BankAccount.
# #
# # This demonstrates INHERITANCE.
# #
# # BankAccount
# #      |
# #      |
# # SavingsAccount
# # ============================================================

# class SavingsAccount(BankAccount):

#     def __init__(self, username, password, account_number):

#         # super() calls the parent class constructor
#         super().__init__(
#             username,
#             password,
#             account_number
#         )

#         # Additional variable specifically for SavingsAccount
#         self.account_type = "Savings Account"


#     # ========================================================
#     # ACCOUNT DETAILS
#     # ========================================================

#     def account_details(self):

#         print("\n================================")
#         print("         ACCOUNT DETAILS")
#         print("================================")

#         print("Account Holder :", self.username)
#         print("Account Number :", self.account_number)
#         print("Account Type   :", self.account_type)
#         print("Balance        :", self.get_balance())


# # ============================================================
# # BANK CLASS
# # ============================================================
# # This class controls:
# #
# # Account Creation
# # Login
# # Account Number Generation
# # User Menu
# # Main Menu
# # ============================================================

# class Bank:

#     def __init__(self):

#         # Dictionary used to store all accounts
#         #
#         # Example:
#         #
#         # {
#         #     "vasu": account_object,
#         #     "ravi": account_object
#         # }
#         #
#         self.accounts = {}


#     # ========================================================
#     # GENERATE UNIQUE ACCOUNT NUMBER
#     # ========================================================
#     #
#     # Random number may sometimes generate the same number.
#     #
#     # Therefore:
#     #
#     # 1. Generate number
#     # 2. Check existing account numbers
#     # 3. If duplicate, generate again
#     # 4. If unique, return it
#     #
#     # ========================================================

#     def generate_account_number(self):

#         while True:

#             # Generate random 9-digit number
#             account_number = random.randint(
#                 100000000,
#                 999999999
#             )

#             # Assume initially that number is unique
#             duplicate = False

#             # Loop through all existing accounts
#             for account in self.accounts.values():

#                 # Check whether account number already exists
#                 if account.account_number == account_number:

#                     duplicate = True
#                     break

#             # If duplicate is False,
#             # account number does not exist
#             if duplicate == False:

#                 return account_number


#     # ========================================================
#     # CREATE ACCOUNT
#     # ========================================================

#     def create_account(self):

#         print("\n================================")
#         print("        CREATE ACCOUNT")
#         print("================================")

#         username = input("Enter Username : ")

#         # Check whether username already exists
#         if username in self.accounts:

#             print("\nUsername Already Exists")
#             return

#         password = input("Enter Password : ")

#         # Generate unique 9-digit account number
#         account_number = self.generate_account_number()

#         # Create SavingsAccount object
#         account = SavingsAccount(
#             username,
#             password,
#             account_number
#         )

#         # Store account object in dictionary
#         #
#         # Username becomes dictionary key
#         #
#         self.accounts[username] = account

#         print("\nAccount Created Successfully")

#         print("--------------------------------")
#         print("Username       :", username)
#         print("Account Number :", account_number)
#         print("Account Type   :", account.account_type)
#         print("--------------------------------")


#     # ========================================================
#     # LOGIN
#     # ========================================================

#     def login(self):

#         print("\n================================")
#         print("             LOGIN")
#         print("================================")

#         username = input("Enter Username : ")
#         password = input("Enter Password : ")

#         # Check whether username exists
#         if username in self.accounts:

#             # Get corresponding account object
#             account = self.accounts[username]

#             # Check password
#             if account.get_password() == password:

#                 print("\nLogin Successful")
#                 print("Welcome,", username)

#                 # Open account menu
#                 self.user_menu(account)

#             else:

#                 print("\nIncorrect Password")

#         else:

#             print("\nAccount Does Not Exist")


#     # ========================================================
#     # USER MENU
#     # ========================================================
#     # This menu appears after successful login.
#     # ========================================================

#     def user_menu(self, account):

#         while True:

#             print("\n================================")
#             print("        BANK ACCOUNT MENU")
#             print("================================")

#             print("1. Credit")
#             print("2. Debit")
#             print("3. Balance Enquiry")
#             print("4. Mini Statement")
#             print("5. Account Details")
#             print("6. Logout")

#             choice = input("\nEnter Your Choice : ")


#             # ------------------------------------------------
#             # CREDIT
#             # ------------------------------------------------

#             if choice == "1":

#                 try:

#                     amount = float(
#                         input("Enter Credit Amount : ")
#                     )

#                     account.credit(amount)

#                 except ValueError:

#                     print("\nPlease Enter Valid Amount")


#             # ------------------------------------------------
#             # DEBIT
#             # ------------------------------------------------

#             elif choice == "2":

#                 try:

#                     amount = float(
#                         input("Enter Debit Amount : ")
#                     )

#                     account.debit(amount)

#                 except ValueError:

#                     print("\nPlease Enter Valid Amount")


#             # ------------------------------------------------
#             # BALANCE ENQUIRY
#             # ------------------------------------------------

#             elif choice == "3":

#                 account.balance_enquiry()


#             # ------------------------------------------------
#             # MINI STATEMENT
#             # ------------------------------------------------

#             elif choice == "4":

#                 account.mini_statement()


#             # ------------------------------------------------
#             # ACCOUNT DETAILS
#             # ------------------------------------------------

#             elif choice == "5":

#                 account.account_details()


#             # ------------------------------------------------
#             # LOGOUT
#             # ------------------------------------------------

#             elif choice == "6":

#                 print("\nLogout Successful")
#                 break


#             else:

#                 print("\nInvalid Choice")


#     # ========================================================
#     # MAIN BANK MENU
#     # ========================================================

#     def start(self):

#         while True:

#             print("\n================================")
#             print("      BANK MANAGEMENT SYSTEM")
#             print("================================")

#             print("1. Create Account")
#             print("2. Login")
#             print("3. Exit")

#             choice = input("\nEnter Your Choice : ")


#             # Create new bank account
#             if choice == "1":

#                 self.create_account()


#             # Login to existing account
#             elif choice == "2":

#                 self.login()


#             # Close application
#             elif choice == "3":

#                 print("\nThank You For Using Our Bank")
#                 print("Application Closed")

#                 break


#             else:

#                 print("\nInvalid Choice")


# # ============================================================
# # PROGRAM STARTING POINT
# # ============================================================

# # Create Bank object
# bank = Bank()

# # Start Bank Management System
# bank.start()