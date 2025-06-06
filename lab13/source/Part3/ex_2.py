class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.__balance = balance # Private attribute

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value
        
# a)
account = BankAccount("Dmitriy", 50)

# b)
print("Balance:", account.balance)

# c)
try:
    account.balance = -100
except ValueError as e:
    print("Error:", e)

# d)
account.balance = 200
print("New balance:", account.balance)