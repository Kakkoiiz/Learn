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

bird1 = Bird("Đại bàng", 5 , "Nâu", 3.5, 180 )
bird1.print_info()

# sử dụng phương thức fly
bird1.fly()
bird1.print_info()

# sử dụng phương thức stop_fly
bird1.stop_flying()
bird1.print_info()