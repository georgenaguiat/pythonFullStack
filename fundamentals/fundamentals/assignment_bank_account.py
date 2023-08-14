class BankAccount:
    all_accounts = []

    def __init__(self, ini_rate, balance):
        self.ini_rate = ini_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print('Balance: ${:.2f}'.format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.ini_rate
            self.balance += interest
        return self
    
    @classmethod
    def show_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
            

chase_bank_account = BankAccount(.03, 2000)
bank_of_america_account = BankAccount(.03, 4000)
chase_bank_account.deposit(100).deposit(200).deposit(200).withdraw(1000).yield_interest().display_account_info()
bank_of_america_account.deposit(100).deposit(150).withdraw(200).withdraw(200).withdraw(500).withdraw(800).yield_interest().display_account_info()
BankAccount.show_all_accounts()