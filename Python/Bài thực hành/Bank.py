class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def desposit(self, amount):
        self.balance += amount
    
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Số tiền rút không được lớn hơn số dư")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
account = BankAccount("Dũng dz", 1000)

print(account.get_balance())    

try:
    account.withdraw(10000)
except ValueError as e:
    print(e)
    
account.desposit(500)
account.withdraw(100)

print(account.get_)