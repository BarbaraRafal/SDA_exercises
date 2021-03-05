class Account:
    def __init__(self, balance_amount: float, user_status: str) -> None:
        self.balance_amount = balance_amount
        self.user_status = user_status

    def transfer(self, amount_of_money: float) -> float:
        try:
            self.balance_amount += amount_of_money
        except TypeError:
            print(f"{amount_of_money} is not a float!")
        return self.balance_amount

    def balance(self) -> float:
        return self.balance_amount
