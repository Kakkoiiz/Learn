class Animal:
    def __init__(self,name):
        self.name = name
        
    def make_sound(self):
        pass
    
class Dog:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Gâu Gâu"

class Cat:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Meow Meow"
        
class Bird:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Chíp Chíp"
        
animals = [Dog("Chó"), Cat("Mèo"), Bird("Chim")]
while True:
    print("Chọn một con vật để kêu: ")
    for i, animal in enumerate(animals):
        print(f"{i+1} {animal.name}")

    choice = input("Chọn số tướng ứng hoặc ấn q để thoát: ")
    if choice == "q":
        break
    
    try:
        choice = int(choice)
        animal = animals[choice - 1]
        print(f"{animal.name} kêu {animal.make_sound()}")
    except(ValueError, IndexError):
        print("Vui lòng nhập lại: ")
            

   

        