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

    @property
    def status(self) -> str:
        if self.__balance == 0:
            return "Empty"
        elif self.__balance < 100:
            return "Low"
        else:
            return "Healthy"
        
account = BankAccount("Dmitriy", 50)
print(account.status)
account.balance = 200
print(account.status)