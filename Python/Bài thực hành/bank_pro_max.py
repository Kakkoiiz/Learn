class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def age(self):
        pass
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self.age = age
        
try:
    person = Person("Dũng", 20)
    person.age = -30
    print(person.age)
except ValueError as e:
    print(e)
    
person._age = -30
print(person._age)