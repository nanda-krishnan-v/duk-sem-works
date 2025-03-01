#Create a class Vector with x and y coordinates. 
# Overload the + operator to add two vectors, and overload __str__ to display the vector in (x, y) format. 
# Create two vectors and test the addition.

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __str__(self):
        return f"{self.x} {self.y}"
        
v1 = Vector(3, 4)
v2 = Vector(1, 2)

addition = v1 + v2
print(v1)
print(v2)
print(addition)