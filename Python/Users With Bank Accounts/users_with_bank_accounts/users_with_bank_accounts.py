class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate} - Balance: ${self.balance}')
        #if self.balance > 600:
            #print('I can buy more boxing gear!')
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account1 = BankAccount(.0025, 400)
account2 = BankAccount(.0028, 800)

account1.deposit(200).deposit(900).deposit(3000).withdraw(800).yield_interest().display_account_info()

account2.deposit(400).deposit(8000).withdraw(200).withdraw(800).withdraw(100).withdraw(200).yield_interest().display_account_info()

BankAccount.print_accounts()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            'checking': BankAccount(0.0025, 8000),
            'money market': BankAccount(0.045, 26000),
            'savings': BankAccount(0.0028, 15000)
        }
    def make_deposit(self):
        self.account.deposit()
        return self
    def withdraw(self):
        self.account.withdraw()
        return self
    def display_user_balance(self):
        print(f"User: {self.name} - Checking: ${self.account['checking'].balance}")
        print(f"User: {self.name} - Savings: ${self.account['savings'].balance}")
        print(f"User: {self.name} - Money Market: ${self.account['money market'].balance}")
        return self

ducky = User('Ducky')
goose = User('Goose')

ducky.account['checking'].deposit(800)
ducky.account['money market'].deposit(800) #does this satisfy the SENSEI BONUS?
ducky.display_user_balance()
