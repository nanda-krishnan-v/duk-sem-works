#19 WAP to determine the type of the triangle.

a = int(input("Enter the sides in order: "))
b = int(input("Enter the sides in order: "))
c = int(input("Enter the sides in order: "))

a1 = a*a
b1 = b*b
c1 = c*c

if a==b==c:
  print("Equilateral Triangle")
elif a==b or b==c or c==a:
  print("Isosceles Triangle")
elif c1==a1+b1 or a1==b1+c1 or b1==a1+c1:
  print("Right-angled Triangle")
else:
  print("Scalene Triangle")

