n = int(input("enter the 2 digit number: "))
sum = 0
x = n
while n>0:
    rem = n % 10
    sum = sum + int(rem)
    n = n/10
    
print("The sum of ",x,"is",sum)
 