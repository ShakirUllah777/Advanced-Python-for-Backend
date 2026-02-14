'''
Create a class BankAccount with:
owner
balance
Methods:
deposit(amount)
withdraw(amount)
display_balance()
Rules:
Cannot withdraw more than balance
Print proper messages
👉 Bonus:
Make balance private and use a @property to read it.
'''
class BankAccount:
    def __init__(self, owner, bal):
        self.owner = owner
        self.balance = bal
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Pasy Kam hay, LALA')
        else:
            self.balance -= amount
            return self.balance
        
    def display_balance(self):
        print('Total Balance is ',self.balance)

c1 = BankAccount("ali",90)
c1.display_balance()
c1.deposit(10)
c1.display_balance()
c1.withdraw(50)
c1.display_balance()

