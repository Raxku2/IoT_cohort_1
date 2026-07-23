
from sys import set_int_max_str_digits





set_int_max_str_digits(100000)

class BankAccount():
    def __init__(self,account_holder:str, initial_balance:float=0.0) -> None:
        self.holder = account_holder
        self.balance = initial_balance

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            return f"withdraw {amount}, available bal {self.balance}"
        return "Insufficent balance"


    def diposit(self,amount):
        if amount > 0:
            self.balance+=amount
            return f"Diposit {amount}, available bal {self.balance}"
        return "Diposit amount must be positive."




class CurrentAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0) -> None:
        super().__init__(account_holder, initial_balance)



my_account = BankAccount("Rakesh")

print(my_account.balance)

my_account.diposit(500000)

print(my_account.balance)

my_account.withdraw(130000)

print(my_account.balance)








