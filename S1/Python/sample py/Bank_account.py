#5.     Implement a class BankAccount with attributes account_number and balance. 
# Make balance a private attribute and create methods deposit() and withdraw() to modify it. 
# Include a method to display the balance. 
# Test the methods by creating an instance and performing a few transactions.

class BankAccount():
    def __init__(self,account_number):
        self.account_number = account_number
        self.__balance = 0
        
    def deposit(self,amount):
        self.__balance += amount
        print(f"Amount Credited: {amount}")
        print(f"Account Balance: {self.__balance}")
    
    def withdraw(self,amount):
        self.__balance -= amount
        print(f"Amount Credited: {amount}")
        print(f"Account Balance: {self.__balance}")
  
b = BankAccount(123)
b.deposit(5000)
print()
b.withdraw(2000)
