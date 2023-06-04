import datetime
class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    
    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
        print("phone: ", self.phone)
        
    
person1 = Person("John Smith", 22, "123 Main St, Anytown USA", "983-12345")
person1.info()