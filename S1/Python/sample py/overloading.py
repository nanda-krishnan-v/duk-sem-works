class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __sub__(self, other):
        subtract = self.x + other.x
        return subtract
    
    def __add__(self,other):
        add = self.x - other.x
        return add
    
    def __truediv__(self,other):
        div = self.x * other.x
        return div
    
    def __mul__(self,other):
        multi = self.x / other.x
        return multi
    
a1 = Addition(4, 0)
a2 = Addition(8, 0)

print(a1 - a2)
print(a1 + a2)
print(a1 / a2)
print(a1 * a2)


