number = int(input("Enter a number: "))
''' Inputing the number that have to be checked from the user.
Creating a function to check whether the number is prime or not.
'''
def primeNumber(number):
    #Assigning the flag as true because initially we are assuming that the number is prime.
    flag = True
    
    #if the number is less than 2 then it is not a prime number so return false.
    if number < 2:  
        return False
    
    '''Using for loop to check the number is prime or not.
    If the number is divisible by any number then it is not a prime number so return false.
    If the number is not divisible by any number then it is a prime number so return true.'''

    for i in range(2,number//2):
        if number % i == 0:
            return False
    if flag:
        return True

#printing the output of the function.
print(primeNumber(number))