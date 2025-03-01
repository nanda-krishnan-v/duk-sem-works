#7.	WAP that print prime numbers between 2 numbers.

num = int(input("Enter the starting number: "))

if num > 1:
        flag = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            print("true")
 
 
