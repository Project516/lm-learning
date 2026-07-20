# class Student:

#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Hi, I am", self.name)

# myStudent = Student("Aidan")
# myStudent.hello()
# myStudent1 = Student("Evan")
# myStudent1.hello()

class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("insufficient funds")
    
    def transfer(self, other_acct, amount):
        if(self.balance >= amount):
            self.balance -= amount
            other_acct.balance += amount
        else:
            print("insufficent funds")
tom_acct = BankAccount("Tom", 1234)
mary_acct = BankAccount("Mary", 5678)
tom_acct.deposit(100)
tom_acct.transfer(mary_acct, 40)
print(tom_acct.balance)
print(mary_acct.balance)
