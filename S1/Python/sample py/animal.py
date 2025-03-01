#Create a base class Animal with attributes name and species and a method sound() that prints a generic message. 
# Create subclasses Dog and Cat that override the sound() method to print species-specific sounds. 
# Instantiate each subclass and call the sound() method.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def sound(self):
        print("This is a fact that an Animal will make some sound!")
        
class Dog(Animal):
    def __init__(self):
        pass
    
    def dog_sound(self):
        print("The sound made by dog is Bow Bow")

class Cat(Animal):
    def __init__(self):
        pass
    
    def cat_sound(self):
        print("The sound made by cat is meow meow") 
    
#a = Animal("Jacky","Dog")
d = Dog()
c = Cat()

#a.sound()
d.dog_sound()
c.cat_sound()

d.sound()
c.sound()