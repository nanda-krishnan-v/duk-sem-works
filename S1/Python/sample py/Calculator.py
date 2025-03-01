class Calculator():
    
    @staticmethod
    def add(n1,n2):
        add = n1 + n2
        print(f"Sum is {add}")
        
    @staticmethod
    def sub(n1,n2):
        sub = n1 - n2
        print(f"Difference is {sub}")
    
    @staticmethod
    def mult(n1,n2):
        mult = n1 * n2
        print(f"Product is {mult}")
    
    @staticmethod
    def div(n1,n2):
        div = n1 / n2
        print(f"Division is {div}")
    
Calculator.add(1,3)
Calculator.sub(10,3)
Calculator.mult(2,3)
Calculator.div(30,3)