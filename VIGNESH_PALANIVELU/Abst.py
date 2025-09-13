from abc import ABC, abstractmethod

# Abstract ATM class
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

# Concrete ATM class
class SBIATM(ATM):
    def __init__(self, pin, balance=5000):
        self.correct_pin = pin
        self.balance = balance
        self.authenticated = False

    def login(self, pin_input):
        if pin_input == self.correct_pin:
            self.authenticated = True
            print("✅ Login Successful!\n")
        else:
            print("❌ Invalid PIN!")

    def withdraw(self, amount):
        if self.authenticated:
            if amount > self.balance:
                print("❌ Insufficient Balance!")
            else:
                self.balance -= amount
                print(f"✅ ₹{amount} Withdrawn Successfully.")
        else:
            print("⚠️ Please login first.")

    def deposit(self, amount):
        if self.authenticated:
            self.balance += amount
            print(f"✅ ₹{amount} Deposited Successfully.")
        else:
            print("⚠️ Please login first.")

    def check_balance(self):
        if self.authenticated:
            print(f"💰 Available Balance: ₹{self.balance}")
        else:
            print("⚠️ Please login first.")

# --- Main Program ---

atm = SBIATM(pin=1234)

print("🏧 Welcome to SBI ATM")
user_pin = int(input("🔑 Enter your 4-digit PIN: "))
atm.login(user_pin)

while True:
    print("\n📋 MENU:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("👉 Enter your choice (1-4): ")

    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        amount = float(input("💵 Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == '3':
        amount = float(input("💸 Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == '4':
        print("👋 Thank you for using SBI ATM. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")

