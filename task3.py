class BankAccount:
    """Работа с банковским аккаунтом"""
    def __init__(self, balance: float = 0) -> None:
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self._balance = balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f"Баланс: {self._balance}"


if __name__ == "__main__":
    acc = BankAccount(10000)
    print(acc.deposit(1000))     
    print(acc.withdraw(100))     
    print(acc)               
