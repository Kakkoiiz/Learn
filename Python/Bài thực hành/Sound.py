class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Chó: Gâu gâu")
class Cat(Animal):
    def make_sound(self):
        print("Mèo: Meo meo")
class Bird(Animal):
    def make_sound(self):
        print("Chim: Chíp chíp")

animals =[Dog(),Cat(),Bird()]
for animal in animals:
    animal.make_sound()