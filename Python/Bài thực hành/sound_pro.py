class Animal:
    def __init__(self, name):
        self.name = name
    
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
class Bird(Animal):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
animals=[Dog("Lucky","Golden Retriever"),Cat("Tom","Đen"),Bird("Tweety","Chim sẻ")]

for i, animal in enumerate(animals):
    print(f"{i+1}.{animal.name}")
    
choice = int(input("Chọn một con vật để in ra thông tin: "))

selected_animal = animals[choice - 1]



if isinstance(selected_animal, Dog):
    print(f"Tên: {selected_animal.name}, Giống: {selected_animal.breed}")
elif isinstance(selected_animal, Cat):
    print(f"Tên: {selected_animal.name}, Màu sắc: {selected_animal.color}")
elif isinstance(selected_animal, Bird):
    print(f"Tên: {selected_animal.name}, Loài: {selected_animal.species}") 
else:
    print("Loại động vật này chưa được hỗ trợ.") 