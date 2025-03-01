#8.	WAP that calculate the roots of a quadratic equation.

import math
def find_roots(a, b, c):
    x = b**2 - (4 * a * c)
    if x > 0:
        m = (-b + math.sqrt(x)) / (2 * a)
        n = (-b - math.sqrt(x)) / (2 * a)
        print(f"The roots are real and different: m = {m}, n = {n}")
    elif x == 0:
        p = -b / (2 * a)
        print(f"The root is real and repeated: p = {p}")
    else:
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-x) / (2 * a)
        e = f"{realPart} + {imaginaryPart}i"
        f = f"{realPart} - {imaginaryPart}i"
        print(f"The roots are complex: e = {e}, f = {f}")

a = int(input("Enter the first coefficent: "))
b = int(input("Enter the second coefficent: "))
c = int(input("Enter the third coefficent: "))
find_roots(a, b, c)