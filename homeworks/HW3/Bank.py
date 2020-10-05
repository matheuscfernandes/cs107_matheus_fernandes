from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        self.owner=owner
        self.accountType=accountType
        self.balance=0

    def withdraw(self, amount):
        if amount<0: raise Exception("Not a valid amount to withdrawal: amount < 0")

        currentBal=self.balance
        newBal=currentBal-amount

        if newBal<0: raise Exception("Not enough funds")
        
        self.balance=newBal

        
    def deposit(self, amount):
        if amount<0: raise Exception("Not a valid amount to deposit: amount < 0")
        self.balance+=amount

    def __str__(self):
        return 'Owner Name: {}; Account type: {}'.format(self.owner,self.accountType.name)

    def __len__(self):
        return self.balance


# acct=BankAccount('Matheus',AccountType.SAVINGS)
# acct.deposit(1000)
# acct.withdraw(500)
# acct.withdraw(500)


# print(str(acct))
# print(len(acct))


# class BankUser():
    
#     def __init__(self, owner):
#         # your code
    
#     def addAccount(self, accountType):
#         # your code
        
#     def getBalance(self, accountType):
#         # your code
        
#     def deposit(self, accountType, amount):
#         # your code

#     def withdraw(self, accountType, amount):
#         # your code

#     def __str__(self):
#         # your code