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


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            'checking': BankAccount(ini_rate=0.03, balance=0),
            'saving': BankAccount(ini_rate=2.4, balance=0)
        }

    def make_deposit(self, account_type, amount):
        self.account[account_type].deposit(amount)
        return self

    def make_withdrawal(self, account_type, amount):
        self.account[account_type].withdraw(amount)
        return self

    def display_user_balance(self, account_type):
        print('Users: {}, Account Type: {}'.format(self.name, account_type))
        self.account[account_type].display_account_info()
        return self

    def transfer_money(self, amount, other_user, from_account_type, to_account_type):
        if self.account[from_account_type].balance < amount:
            print('Insufficient funds: Transfer failed')
            return self

        self.account[from_account_type].withdraw(amount)
        other_user.account[to_account_type].deposit(amount)

        print('${} transferred from {} {} account to {} {} account'.format(amount, self.name, from_account_type, other_user.name, to_account_type))
        return self


account1 = User('George', 'georgeemaail@gmail.com')
account2 = User('Ryan', 'ryanemail@yahoo.com')

account1.make_deposit('checking', 1000).make_withdrawal('checking', 200).display_user_balance('checking')
account2.make_deposit('saving', 2000).make_withdrawal('saving', 500).display_user_balance('saving')
account1.transfer_money(50, account2, 'checking', 'saving').display_user_balance('checking')