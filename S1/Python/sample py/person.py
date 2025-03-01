#Create a class Person with attributes name, age, and city. 
# Define the __str__ method to return a string representation of the object. 
# Create an instance and print it to see the effect of __str__.

class Person():
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        
    def __str__(self):
        return f"The Persons Name is {self.name}, age is {self.age}, palce of {self.name} is {self.city}"

p = Person("nkv",50,"london")
print(p)