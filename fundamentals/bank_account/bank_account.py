class BankAccount:
    balance=0
    all_accounts=[]

    def __init__(self, int_rate, balance):
        self.balance=balance
        self.int_rate=int_rate
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance-=5
        else:
            self.balance-=amount
            return self
    def display_account_info(self):
        print(f"Balance is ${self.balance}, interest rate is {self.int_rate}")
        return self
    def yield_interest(self):
        interest=self.balance*self.int_rate
        self.balance+=interest
        print(f"Your interest is {interest}")
        return self
    @classmethod
    def find_accounts(cls):
        for account in cls.all_accounts:
            print(f"""Account balance={account.balance}, Interest rate={account.int_rate}""")
class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account= BankAccount(int_rate=.01, balance=0)
    def make_deposit(self):
        self.account.deposit()
    def make_withdrawal(self):
        self.account.withdraw()
    def display_user_balance(self):
        self.account.display_account_info()

    



user_brittany=BankAccount(.01, 100)
user_brittany.deposit(50).deposit(75).deposit(100).withdraw(90).yield_interest().display_account_info()

user1=User("Brittany", "brittanyfranics200@gmail.com")
#user1.make_deposit()
"""user_clinton=BankAccount(.01, 200)
user_clinton.deposit(800).deposit(9.90).withdraw(150).withdraw(70).withdraw(8.50).withdraw(32).yield_interest().display_account_info()

BankAccount.find_accounts()
"""
