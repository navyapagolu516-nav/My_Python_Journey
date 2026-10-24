#Implement an ATM program using object-oriented programming(OOP) concepts class object inheritance.

class BankAccount:
    def __init__(self, bank_name, account_holder, balance):
        self.bank_name = bank_name
        self.account_holder = account_holder
        self.balance = balance
    def check_balance(self):
        print(f"Your balance is : {self.balance}")

class ATM(BankAccount):
    def __init__(self, bank_name, account_holder, branch, balance):
        super().__init__(bank_name, account_holder, balance)
        self.branch = branch
    def deposit(self, depo_amount):
        if depo_amount >0:
            self.balance += depo_amount
            print(f"Amount has been deposited successfuly")
            print(f"Your Balance is : {self.balance}")
        else:
            print(f"Invalid Entry")
            
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount > self.balance:
                print("Insufficient Funds")
            else:
                self.balance -= withdraw_amount
                print(f"Amount Withdrawn successfully")
                print(f"Your Balance is : {self.balance}")
        else:
            print(f"Invalid Entry")
    def mini_statement(self):
        print(f"""Welcome to {self.bank_name}!
              Dear {self.account_holder}, 
              Your Current Balance is : {self.balance}""")
        
obj = ATM("SBI", "Navya", "Hyderabad", 1000)

while True:
    print("===== Welcome to ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Exit")

    choice = (input("Enter Your Choice: "))

    if choice == "1":
        obj.check_balance()

    elif choice == "2":
        depo_amount = int(input("Please enter deposit amount :"))
        obj.deposit(depo_amount)

    elif choice == "3":
        withdraw_amount = int(input("Please enter withdraw amount :"))
        obj.withdraw(withdraw_amount)

    elif choice == "4":
        obj.mini_statement()

    elif choice == "5":
        print("Thank You! Visit again...")
        break

    else:
        print(f"Invalid entry")
    
