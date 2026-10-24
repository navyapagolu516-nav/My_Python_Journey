#Create a ATM program using functions

#Step 1: PIN Verification
def check_pin(pin):
    if pin == "1234":
        return True
    return False

#Step 2: Check Balance
def check_balance(balance):
    return balance

#Step 3: Deposit 
def deposit(balance, amount):
    balance += amount
    return balance

#Next: Step 4 — Withdraw
def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return balance
    else:
        print("Insufficient Balance")
        return balance

#Step 5 — ATM Menu
def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

#Step 6 — Connect Everything
balance = 10000
pin = input("Enter Your PIN: ")
if check_pin(pin):
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is: {check_balance(balance)}")

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"Amount deposited successfully. Your new balance is: {balance}")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
            print(f"Amount withdrawn successfully. Your new balance is: {balance}")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1-4.")

else:
    print("Invalid PIN")


    