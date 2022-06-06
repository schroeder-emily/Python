class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
    def make_withdrawal(self, amount):
        self.amount -= amount
    def display_user_balance(self):
        print(f'User: {self.name} - Balance: {self.amount}')
    def transfer_money(self, amount, user):
        self.amount += amount
        
goose = User('Goose') #names of cats I have or have raised :) 
ducky = User('Ducky')
mouse = User('Mouse')

goose.make_deposit(200)
goose.make_deposit(500)
goose.make_deposit(800)
goose.make_withdrawal(200)
goose.display_user_balance()

ducky.make_deposit(800)
ducky.make_withdrawal(200)
ducky.make_deposit(400)
ducky.make_withdrawal(100)
ducky.display_user_balance()

mouse.make_deposit(4000)
mouse.make_withdrawal(800)
mouse.make_withdrawal(400)
mouse.make_withdrawal(300)
mouse.display_user_balance()

goose.transfer_money(5000, mouse)
mouse.transfer_money(-5000, goose)
mouse.display_user_balance()
goose.display_user_balance()