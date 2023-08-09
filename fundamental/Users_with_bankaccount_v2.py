class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def create_account(self, account_type = ""):

        if account_type != "":
            if account_type == "Saving":
                New_account = BankAccount(int_rate=0.02, balance=0)
                self.accounts[account_type] =New_account
            elif account_type == "Checking":
                New_account = BankAccount(balance=0)
                self.accounts[account_type] =New_account
            else:
                print("Verify account type name!!")
        else:
            print("Need Account type! Checking or Saving")


    def deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)

    def withdraw(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)

    def yield_interest(self, account_type):
        self.accounts[account_type].yield_interest(account_type)

    def display_account_info(self):
        print(self.name)
        for account, value in self.accounts.items():
            print(f"{account} Balance: ${value.balance}")
        
    def transfer_money(self, from_account_type, amount, name, to_account_type):
        if from_account_type == "Checking":   
            self.accounts[from_account_type].withdraw(amount)
            if to_account_type != "":
                name.accounts[to_account_type].deposit(amount)
            else:
                print("Need acount to Transfer Money")
        else:
            print("Saving can not Transfer Money")

class BankAccount:

    def __init__(self, int_rate=0, balance = 0):
        self.int_rate = float(int_rate)/100
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

    def yield_interest(self, account_type):
        if account_type != "Checking":
            if self.balance > 0:
                self.balance *= (1 - self.int_rate)
            else:
                print("Zero Interest")
        else:
            print("Checking has no yield")

james = Users("james","jc@email.com")
james.create_account("Checking")
james.create_account("Saving")

james.deposit(800, "Checking")
james.withdraw(300,"Checking")
james.deposit(200, "Saving")
james.yield_interest("Saving")
bob = Users("bob", "bb@email.com")
bob.create_account("Checking")
bob.create_account("Saving")
james.transfer_money("Checking", 200, bob, "Checking")
bob.transfer_money("Checking", 100, bob, "Saving")
james.transfer_money("Saving", 100, james, "Checking")

bob.display_account_info()
james.display_account_info()