class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self,other):
        addition = self.real + other.real
        addition1 = self.imaginary + other.imaginary
        return f"{addition} + {addition1}i"
    
p1 = ComplexNumber(5,6)
p2 = ComplexNumber(5,6)

print