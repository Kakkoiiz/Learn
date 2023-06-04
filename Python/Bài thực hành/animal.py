class Animal:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def info(self):
        print("Name : ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)
        print("Weight: ", self.weight)
        
animal = Animal("Khải", 20, "vàng", "50kg") 
animal.info()

# tạo một đối tượng mới  
animal2 = Animal("Mimi", 3, "Nâu", "5kg")
# in ra thông tin 
animal2.info()
# thay đổi tuổi của đối tượng con vật
animal2.age = 4
animal2.info()