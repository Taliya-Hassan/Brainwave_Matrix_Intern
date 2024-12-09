class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.pin = "1234"    # Default PIN
        self.is_authenticated = False

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                self.is_authenticated = True
                print("Authentication successful!\n")
                return
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempt(s) left.")
        print("Too many incorrect attempts. Exiting...")
        exit()

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully!")
                self.check_balance()
            else:
                print("Invalid amount. Please enter a positive number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > self.balance:
                print("Insufficient funds. Please enter a smaller amount.\n")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.\n")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully!")
                self.check_balance()
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

    def run(self):
        self.authenticate()
        while True:
            print("ATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Please try again.\n")


# Run the ATM program
if __name__ == "__main__":
    atm = ATM()
    atm.run()
