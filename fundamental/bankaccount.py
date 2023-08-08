class BankAccount:
    Bank_name = "ABC Bank"
    bank_account_list = []
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = float(int_rate)/100
        self.balance = balance
        BankAccount.bank_account_list.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 - self.int_rate)
            return self
        else:
            return self
    @classmethod
    def dispay_all_account_info(cls):
        print(cls.Bank_name)
        for account in cls.bank_account_list:
            print(f"Account {cls.bank_account_list.index(account) + 1}")
            print (f"Account Rate: {account.int_rate}%, Account Balance: ${account.balance}")

A_account = BankAccount(5, 20)
B_account = BankAccount(0.3)

A_account.deposit(100).deposit(300).deposit(30).withdraw(100).yield_interest()\
    .display_account_info()
B_account.deposit(100).deposit(100).withdraw(50).withdraw(100).withdraw(50).withdraw(100)\
    .yield_interest().display_account_info()
BankAccount.dispay_all_account_info()