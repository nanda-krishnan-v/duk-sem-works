class Bird:
    def speak(self):
        return "Bird chirps"

class Dog:
    def speak(self):
        return "Dog barks"

# Polymorphism through method overriding
def animal_sound(animal):
    print(animal.speak())

# Creating objects
bird = Bird()
dog = Dog()

# Polymorphic behavior
animal_sound(bird)  # Bird chirps
animal_sound(dog)   # Dog barks
