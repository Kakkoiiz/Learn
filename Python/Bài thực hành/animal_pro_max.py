class Animal:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight}")
    
class Bird(Animal):
    def __init__(self, name, age ,color, weight, wingspan):
        super().__init__(name, age, color,  weight)
        self.wingspan = wingspan
        self.is_flying = False
    
    def fly(self):
        self.is_flying = True
        print(f"{self.name} đang bay với sải cánh {self.wingspan} cm")
    
    def stop_flying(self):
        self.is_flying = False
        print(f"{self.name} dừng bay")
        
    def print_info(self):
        super().print_info()
        print(f"Sải cánh: {self.wingspan} cm")
        if self.is_flying:
            print("Trạng thái: Đang bay")    
        else:
            print("Trạng thái: Không bay")
        
        if isinstance(self, Parrot) and self.can_talk:
            print(f"{self.name} Biết nói")
        else: 
            print(f"{self.name} Không biết")    
class Parrot(Bird):
    def __init__(self, name, age, color, weight, wingspan):
        super().__init__(name, age, color, weight, wingspan)
        self.can_talk = True
        
        
        
    def speak(self, word):
        self.word = word
        print(f"{self.name} nói {self.word}")



animal1 = Parrot("Polly", 3, "Đỏ", 0.5, 20)
animal1.fly()
animal1.print_info()
animal1.speak("xin chào")
animal1.stop_flying()


animal2 = Bird("Khải", 18, "Black", 50, 10000)
animal2.fly()
animal2.print_info()