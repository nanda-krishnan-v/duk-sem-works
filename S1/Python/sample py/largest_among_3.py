#12 Largest among 3 number

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b:
  if a>c:
    print(a," is large")
  else:
    print(c," is large")
else:
  if b>c:
    print(b," is large")
  else:
    print(c," is large")
