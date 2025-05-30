class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> float:
        if self.balance < amount:
            raise InsufficientFundsError("You can't withdraw more than you have!")
        self.balance -= amount
        print("Money were successfully withdrawn.")
        return amount

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print("Money were successfully deposited.")

acc = BankAccount("Dmitriy", 1000)
acc.withdraw(100)
acc.deposit(100)
acc.withdraw(10000)