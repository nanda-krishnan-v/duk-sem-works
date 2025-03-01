#9.	WAP to compute the sum of two numbers. If the sum is below or equal to twenty, two numbers will be entered again. If the sum is above 20, it will display the sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

if sum <=20:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  sum = num1 + num2
  print(sum)
else:
  print("Sum is above 20")
