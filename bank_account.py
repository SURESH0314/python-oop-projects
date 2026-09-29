class BankAccount:
    def _init_(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: Rs.{amount}")
        print(f"Deposited Rs.{amount}. New Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: Rs.{amount}")
            print(f"Withdrew Rs.{amount}. New Balance: Rs.{self.balance}")
        else:
            print("Insufficient balance!")

    def show_history(self):
        print(f"\n--- History for {self.account_holder} ---")
        for t in self.transaction_history:
            print(t)
        print(f"Current Balance: Rs.{self.balance}")

# Example
acc = BankAccount("Suresh", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_history()
