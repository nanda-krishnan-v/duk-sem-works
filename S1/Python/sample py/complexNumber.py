class ComplexNumber():
    def __init__(self):
        self.imaginary = 0
        self.real = 0
        self.sign = '+'
    
    def input_complex(self):
        self.real = int(input("Enter the real part: "))
        self.imaginary = int(input("Enter the imaginary part: "))
        self.sign = input("Enter the sign (-/+): ")
        if self.imaginary < 0 and self.sign == '-':
            self.sign = '+'
            self.imaginary = abs(self.imaginary)
        elif self.imaginary < 0 and self.sign == '+':
            self.sign = '-'
            self.imaginary = abs(self.imaginary)
        print(f"{self.real} {self.sign} {self.imaginary}i")
        # return self.real,self.imaginary
    
c = ComplexNumber()
c.input_complex()

c1 = ComplexNumber()
c1.input_complex()