
import random
from datetime import datetime

# ==========================================
# 1. TRAIN CLASS
# ==========================================

class Train:
    def __init__(self, train_number, train_name, source, destination):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination

        # Seat availability for each coach class
        self.seats = {
            "Sleeper": 10,
            "3AC": 6,
            "2AC": 4,
            "1AC": 2
        }

        self.booked_seats = {
            "Sleeper": 0,
            "3AC": 0,
            "2AC": 0,
            "1AC": 0
        }

        self.waiting_list = []


    def display_train_details(self):
        print("\n----------------------------------")
        print("Train Number:", self.train_number)
        print("Train Name:", self.train_name)
        print("Source:", self.source)
        print("Destination:", self.destination)

        for coach, total in self.seats.items():
            available = total - self.booked_seats[coach]
            print(f"{coach} - Available Seats: {available}")

        print("----------------------------------")


# ==========================================
# 2. PASSENGER CLASS
# ==========================================

class Passenger:
    def __init__(self, name, age, gender, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.berth = None


# ==========================================
# 3. ACCOUNT CLASS
# ==========================================

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# ==========================================
# 4. TICKET CLASS
# ==========================================

class Ticket:
    def __init__(self, pnr, train, passengers, coach, journey_date):
        self.pnr = pnr
        self.train = train
        self.passengers = passengers
        self.coach = coach
        self.journey_date = journey_date
        self.status = "Confirmed"


    def display_ticket_details(self):
        print("\n========== TICKET DETAILS ==========")

        print("PNR:", self.pnr)
        print("Train Number:", self.train.train_number)
        print("Train Name:", self.train.train_name)
        print("Source:", self.train.source)
        print("Destination:", self.train.destination)
        print("Journey Date:", self.journey_date)
        print("Coach:", self.coach)
        print("Status:", self.status)

        for index, passenger in enumerate(self.passengers, start=1):
            print(f"\nPassenger {index}")
            print("Name:", passenger.name)
            print("Age:", passenger.age)
            print("Gender:", passenger.gender)
            print("Phone:", passenger.phone_number)
            print("Berth:", passenger.berth)

        print("====================================")


# ==========================================
# 5. RAILWAY SYSTEM CLASS
# ==========================================

class RailwaySystem:
    def __init__(self):
        self.accounts = []
        self.trains = []
        self.tickets = []
        self.pnr_numbers = set()

        self.add_sample_trains()


    # --------------------------------------
    # ADD SAMPLE TRAINS
    # --------------------------------------

    def add_sample_trains(self):
        self.trains.append(
            Train("12737", "Gowthami Express", "Tadepalligudem", "Secunderabad")
        )

        self.trains.append(
            Train("12738", "Krishna Express", "Vizag", "Secunderabad")
        )

        self.trains.append(
            Train("12739", "Venkatadri Express", "Bangalore", "Secunderabad")
        )


    # --------------------------------------
    # ACCOUNT CREATION
    # --------------------------------------

    def create_account(self):
        print("\n========== CREATE ACCOUNT ==========")

        username = input("Enter username: ")

        for account in self.accounts:
            if account.username == username:
                print("Username already exists!")
                return

        password = input("Enter password: ")

        account = Account(username, password)
        self.accounts.append(account)

        print("Account created successfully!")


    # --------------------------------------
    # LOGIN
    # --------------------------------------

    def login(self):
        print("\n========== LOGIN ==========")

        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in self.accounts:
            if account.username == username:
                if account.check_password(password):
                    print("Login successful!")
                    return account

                print("Incorrect password!")
                return None

        print("Username not found!")
        return None


    # --------------------------------------
    # DISPLAY TRAINS
    # --------------------------------------

    def display_trains(self):
        print("\n========== AVAILABLE TRAINS ==========")

        for train in self.trains:
            train.display_train_details()


    # --------------------------------------
    # SELECT TRAIN
    # --------------------------------------

    def select_train(self):
        self.display_trains()

        train_number = input("\nEnter train number: ")

        for train in self.trains:
            if train.train_number == train_number:
                print("Train selected:", train.train_name)
                return train

        print("Invalid train number!")
        return None


    # --------------------------------------
    # SELECT COACH
    # --------------------------------------

    def select_coach(self):
        print("\nAvailable Coaches:")
        print("1. Sleeper")
        print("2. 3AC")
        print("3. 2AC")
        print("4. 1AC")

        coach_options = {
            "1": "Sleeper",
            "2": "3AC",
            "3": "2AC",
            "4": "1AC"
        }

        choice = input("Select coach: ")

        return coach_options.get(choice)


    # --------------------------------------
    # PASSENGER REGISTRATION
    # --------------------------------------

    def register_passengers(self):
        passengers = []

        try:
            count = int(input("Enter number of passengers: "))

            if count <= 0:
                print("Passenger count must be greater than zero!")
                return []

            for i in range(count):
                print(f"\nPassenger {i + 1}")

                name = input("Name: ")
                age = int(input("Age: "))
                gender = input("Gender: ")
                phone = input("Phone number: ")

                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)

        except ValueError:
            print("Invalid input!")
            return []

        return passengers


    # --------------------------------------
    # BERTH ALLOCATION
    # --------------------------------------

    def allocate_berths(self, passengers):
        berths = [
            "Lower",
            "Middle",
            "Upper",
            "Side Lower",
            "Side Upper"
        ]

        for passenger in passengers:
            passenger.berth = random.choice(berths)


    # --------------------------------------
    # GENERATE UNIQUE PNR
    # --------------------------------------

    def generate_pnr(self):
        while True:
            pnr = random.randint(100000, 999999)

            if pnr not in self.pnr_numbers:
                self.pnr_numbers.add(pnr)
                return pnr


    # --------------------------------------
    # BOOK TICKET
    # --------------------------------------

    def book_ticket(self):
        train = self.select_train()

        if train is None:
            return

        coach = self.select_coach()

        if coach is None:
            print("Invalid coach selection!")
            return

        try:
            journey_date = input("Enter journey date (YYYY-MM-DD): ")
            journey_date = datetime.strptime(
                journey_date, "%Y-%m-%d"
            ).date()

            if journey_date < datetime.today().date():
                print("Journey date cannot be in the past!")
                return

        except ValueError:
            print("Invalid date format!")
            return

        passengers = self.register_passengers()

        if not passengers:
            return

        available_seats = (
            train.seats[coach] - train.booked_seats[coach]
        )

        # CONFIRMED BOOKING

        if len(passengers) <= available_seats:

            self.allocate_berths(passengers)

            train.booked_seats[coach] += len(passengers)

            pnr = self.generate_pnr()

            ticket = Ticket(
                pnr, train, passengers, coach, journey_date
            )

            self.tickets.append(ticket)

            ticket.display_ticket_details()

            print("\nTicket booked successfully!")

        # WAITING LIST

        else:
            print("\nSeats not available!")

            choice = input("Do you want to join waiting list? (yes/no): ")

            if choice.lower() == "yes":

                pnr = self.generate_pnr()

                ticket = Ticket(
                    pnr, train, passengers, coach, journey_date
                )

                ticket.status = "Waiting"

                train.waiting_list.append(ticket)

                self.tickets.append(ticket)

                print("Added to waiting list!")
                print("Waiting list PNR:", pnr)

            else:
                print("Booking cancelled!")


    # --------------------------------------
    # VIEW TICKET
    # --------------------------------------

    def view_ticket(self):
        pnr = input("Enter PNR number: ")

        for ticket in self.tickets:
            if str(ticket.pnr) == pnr:
                ticket.display_ticket_details()
                return

        print("Ticket not found!")


    # --------------------------------------
    # CANCEL TICKET
    # --------------------------------------

    def cancel_ticket(self):
        pnr = input("Enter PNR number to cancel: ")

        for ticket in self.tickets:

            if str(ticket.pnr) == pnr:

                if ticket.status == "Cancelled":
                    print("Ticket is already cancelled!")
                    return

                if ticket.status == "Waiting":
                    ticket.train.waiting_list.remove(ticket)

                elif ticket.status == "Confirmed":
                    ticket.train.booked_seats[ticket.coach] -= len(
                        ticket.passengers
                    )

                ticket.status = "Cancelled"

                print("Ticket cancelled successfully!")
                return

        print("Invalid PNR number!")


    # --------------------------------------
    # MAIN MENU
    # --------------------------------------

    def main_menu(self):
        while True:
            print("\n========== RAILWAY BOOKING SYSTEM ==========")
            print("1. Display Trains")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_trains()

            elif choice == "2":
                self.book_ticket()

            elif choice == "3":
                self.view_ticket()

            elif choice == "4":
                self.cancel_ticket()

            elif choice == "5":
                print("Logged out successfully!")
                break

            else:
                print("Invalid choice!")


# ==========================================
# 6. MAIN PROGRAM
# ==========================================

def main():

    railway = RailwaySystem()

    while True:
        print("\n========== WELCOME ==========")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            railway.create_account()

        elif choice == "2":
            account = railway.login()

            if account is not None:
                railway.main_menu()

        elif choice == "3":
            print("Thank you for using Railway Booking System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
