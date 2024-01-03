class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        Account.__init__(self, balance)
        self.interest_rate = interest_rate

    def compute_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(Account):
    def __init__(self, balance, overdraft):
        Account.__init__(self, balance)
        self.overdraft = overdraft

    def withdraw_overdraft(self, amount):
        if amount <= (self.balance + self.overdraft):
            self.withdraw(amount)
        else:
            print("Could not make transaction")


if __name__ == "__main__":
    saving = SavingsAccount(100, 0.02)
    saving.deposit(100)
    saving.compute_interest()
    print(saving.balance)

    checking = CheckingAccount(100, 110)
    checking.withdraw_overdraft(200)
    print(checking.balance)

