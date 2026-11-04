#creating the Account class from where we can debit and credit the balance and get the balance
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credit")
        print("total balance", self.balance)

    def get_balance(self):
        return self.balance


acc1 = Account(12000, 452012233)

print(acc1.get_balance())
