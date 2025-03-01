#6.	WAP that output the factorial of a given number.

fact = 1
i = 1

n = int(input("Enter the number: "))

while i<=n:
  fact = fact*i
  i=i+1

print(fact)

# for i in range(1,n):
#   fact = fact * i
  
# print(fact)