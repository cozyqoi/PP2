class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return "{} aksha salyndy. Jana balans: {} tenge".format(amount, self.balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Shygaru mumkin emes: Qarajat jetkiliksiz"
        self.balance -= amount
        return "{} aksha alyndy. Jana balans: {} tenge".format(amount, self.balance)
    
    def __str__(self):
        return "Esep iesi: {}\nEseptegy balans: {} tenge".format(self.owner, self.balance)

owner = input("Atynyzdy engiziniz: ")
balance = float(input("Bastapky soma: "))
account = Account(owner, balance)

print(account)

deposit_amount = float(input("Aksha salu: "))
print(account.deposit(deposit_amount))

withdraw_amount = float(input("Aksha alu: "))
print(account.withdraw(withdraw_amount))

print(account)
