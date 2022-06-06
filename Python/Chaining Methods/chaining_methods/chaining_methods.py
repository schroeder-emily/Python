class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f'User: {self.name} - Balance: {self.amount}')
        return self
    def transfer_money(self, amount, user):
        self.amount += amount
        return self
goose = User('Goose') #names of cats I have or have raised :) 
ducky = User('Ducky')
mouse = User('Mouse')

goose.make_deposit(200).make_deposit(500).make_deposit(800).make_withdrawal(200).display_user_balance()

ducky.make_deposit(800).make_withdrawal(200).make_deposit(400).make_withdrawal(100).display_user_balance()

mouse.make_deposit(4000).make_withdrawal(800).make_withdrawal(400).make_withdrawal(300).display_user_balance()

goose.transfer_money(5000, mouse).display_user_balance()
mouse.transfer_money(-5000, goose).display_user_balance()