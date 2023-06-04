import datetime
class Person:
    def __init__(self, name, birthday, address, phone):
        self.name = name
        self.birthday = birthday
        self.address = address
        self.phone = phone
    
    def info(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Address: ", self.address)
        print("phone: ", self.phone)
        
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        print(f"Age: {age}")
        
    
person1 = Person("John Smith", datetime.date(1990, 5, 15 ), "123 Main St, Anytown USA", "983-12345")
person1.info()
person1.get_age()