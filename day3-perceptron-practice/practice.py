class BankAccount():

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print(self.balance)


a = BankAccount()
b = BankAccount()

a.deposit(100)
b.deposit(50)
a.show()
b.show()