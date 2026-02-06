# Parent Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}")


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"{amount} withdrawn using overdraft if needed.")
        else:
            print("Overdraft limit exceeded.")


# Savings Account Object
print("\n--- Savings Account ---")
savings = SavingsAccount("Keerthana", 10000, 5)

savings.display_balance()
savings.deposit(2000)
savings.withdraw(1500)
savings.add_interest()
savings.display_balance()


# Current Account Object
print("\n--- Current Account ---")
current = CurrentAccount("Rahul", 5000, 3000)

current.display_balance()
current.deposit(1000)
current.withdraw(2000)
current.withdraw_with_overdraft(7000)
current.display_balance()
