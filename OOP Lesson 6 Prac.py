# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#             return f'Hey, its {self.name}!'
#     def have_birthday(self):
#         self.age += 1
#         return f'Happy Birthday! You are {self.age} years old'
# person1 = Person('Alice', 30)
# print(person1.greet())
# print(person1.have_birthday())

class BankAccount:
    def __init__(self, acc_holder, balance=0):
          self.acc_holder = acc_holder
          self.balance = balance
    def deposit(self, amount):
          if amount > 0:
               self.balance += amount
               return f'Deposited ${amount}. New balance ${self.balance}'
          else:
               return 'Deposit amount must be positive'
    def withdraw(self, amount):
         if 0 < amount <= self.balance:
              self.balance -= amount
              return f"Withdrew ${amount}. New balance: ${self.balance}"    
         else:
              return "insufficent funds or invalid amount"
         
# Creating an instance of BankAccount
account = BankAccount("Alice", 100)
# Testing the methods
print(account.deposit(50))      # Output: Deposited $50.00. New balance: $150.00
print(account.withdraw(30))     # Output: Withdrew $30.00. New balance: $120.00
print(account.withdraw(200))    # Output: Insufficient funds or invalid amount.