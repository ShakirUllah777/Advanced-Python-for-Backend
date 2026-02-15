'''
Decorators allow you to:
Add extra behavior to a function without modifying its original code.
'''

def login_required(func):
    def wrapper(*args, **kwargs):
        user_logged_in = True

        if not user_logged_in:
            print('Access Denied, Need Login')
            return 
        return func(*args, **kwargs)
    
    return wrapper

@login_required
def transfer_money(amount):
    print(f"Transferring {amount}...")

@login_required
def withdraw_money(amount):
    print(f"Withdrawing {amount}...")

@login_required
def view_balance():
    print("Your balance is 5000")


transfer_money(1000)
withdraw_money(500)
view_balance()
