class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(type= "Checking", balance=0)
        self.saving = BankAccount( type = "Saving", int_rate=0.02, balance=0)

    # def deposit(self, amount):
    #     self.deposit(amount)

    # def withdraw(self, accounttype, amount):
    #     self.account.withdraw(accounttype, amount)

    def display_account_info(self):
        print(f"{self.name},\n{self.checking.type} Balance: ${self.checking.balance}\n\
{self.saving.type} Balance: ${self.saving.balance}\n")
        
    def transfer_money(self, from_accounttype, amount, name, to_accounttype):
        if from_accounttype == "checking":   
            self.checking.withdraw(amount)
            if to_accounttype == "checking":
                name.checking.deposit(amount)
            elif to_accounttype == "saving":
                name.saving.deposit(amount)
            else:
                print("Need acount to Transfer Money")
        else:
            print("Saving can not Transfer Money")

class BankAccount:

    def __init__(self, type, int_rate=0, balance = 0):
        self.type = type
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

    def yield_interest(self):
        if self.type != "Checking":
            if self.balance > 0:
                self.balance *= (1 - self.int_rate)
            else:
                print("Zero Interest")
        else:
            print("Checking has no yield")

james = Users("james","jc@email.com")
james.saving.deposit(400)
james.checking.deposit(500)
james.checking.withdraw(300)
james.saving.yield_interest()
bob = Users("bob", "bb@email.com")
james.transfer_money("saving", 200, bob, "checking")

bob.display_account_info()
james.display_account_info()