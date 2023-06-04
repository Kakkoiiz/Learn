class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def desposit(self, amount):
        if amount < 0 :
            print("Số tiền không hợp lệ!")
        else:
            self.balance += amount
    
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Số tiền rút không được lớn hơn số dư")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
account = BankAccount("Dũng dz", 1000)
account.desposit(500)
print(account.get_balance())

account.desposit(-200)
print(account.get_balance())