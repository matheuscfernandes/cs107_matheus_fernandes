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


class BankUser():
    
    def __init__(self, owner):
        self.owner=owner
        self.balance={}
    
    def addAccount(self, accountType):
        try: # check if there is an existing bank account
            self.balance[accountType]
            print('Account: {} already exists'.format(accountType.name))
        except:
            self.balance[accountType] = 0

    def getBalance(self, accountType):
        try:
            return self.balance[accountType]
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))
        
    def deposit(self, accountType, amount):
        if amount<0: raise Exception("Not a valid amount to deposit: amount < 0")
        try:
            self.balance[accountType]+=amount
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

    def withdraw(self, accountType, amount):
        if amount<0: raise Exception("Not a valid amount to withdrawal: amount < 0")
        try:
            currentBal=self.balance[accountType]
            newBal=currentBal-amount
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

        if newBal<0: raise Exception("Not enough funds")

        try:
            self.balance[accountType]=newBal
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

    def __str__(self):
        vals='Owner Name: {}\n'.format(self.owner)
        for i in self.balance:
            vals+='Account type: {} -- Balance: {} \n'.format(i.name,self.balance[i])
        return vals

        