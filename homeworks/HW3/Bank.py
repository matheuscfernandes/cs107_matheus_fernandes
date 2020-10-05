from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    #initialize the bank account class with necessary informaiton 
    def __init__(self, owner, accountType: AccountType):
        self.owner=owner
        self.accountType=accountType
        self.balance=0

    def withdraw(self, amount):
        #check to make sure the amount is greater than 0
        if amount<0: raise Exception("Not a valid amount to withdrawal: amount < 0")

        #calculate the new balance
        currentBal=self.balance
        newBal=currentBal-amount

        #check if the new balance is not less than 0
        if newBal<0: raise Exception("Not enough funds")
        
        #update the balance with new amount after withdrawal
        self.balance=newBal

        
    def deposit(self, amount):
        #check if the amount depositing is greater than 0
        if amount<0: raise Exception("Not a valid amount to deposit: amount < 0")
        
        #update the balance with the new amount after deposit
        self.balance+=amount

    def __str__(self):
        #return string that contains the owner information and the account type
        return 'Owner Name: {}; Account type: {}'.format(self.owner,self.accountType.name)

    def __len__(self):
        #return the float balance of the account
        return self.balance


class BankUser():

    #initialize the bank user class with the necessary information
    def __init__(self, owner):
        self.owner=owner
        self.balance={}
    
    def addAccount(self, accountType):
        try: # check if there is an existing bank account
            self.balance[accountType]
            raise Exception('Account: {} already exists'.format(accountType.name))
        #if account does not exist create one and set the balance to 0
        except:
            self.balance[accountType] = 0

    def getBalance(self, accountType):
        #check if account esists, if so return the balance and if not raise and expetion
        try:
            return self.balance[accountType]
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))
        
    def deposit(self, accountType, amount):
        #check if the amount is greater than 0
        if amount<0: raise Exception("Not a valid amount to deposit: amount < 0")
        #ty to see if account exists, if so update balancem, if not raise an exception error
        try:
            self.balance[accountType]+=amount
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

    def withdraw(self, accountType, amount):
        #check of the amount is greater than 0
        if amount<0: raise Exception("Not a valid amount to withdrawal: amount < 0")

        #ty to see if account exists, if so update balancem, if not raise an exception error
        try:
            currentBal=self.balance[accountType]
            newBal=currentBal-amount
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

        if newBal<0: raise Exception("Not enough funds")

        #ty to see if account exists, if so update balancem, if not raise an exception error
        try:
            self.balance[accountType]=newBal
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))

    def __str__(self):
        #create a string that provides the owners name and each account type as well as corresponding balance. Return that string.
        vals='Owner Name: {}\n'.format(self.owner)
        for i in self.balance:
            vals+='Account type: {} -- Balance: {} \n'.format(i.name,self.balance[i])
        return vals

class ATMSession():

    def __init__(self,bankUser):
        self.bu=bankUser
    
    def Interface(self):
        print('Enter Option: \n')
        print('1)Exit\n')
        print('2)Create Account\n')
        print('3)Check Balance\n')
        print('4)Deposit\n')
        print('5)Withdraw \n')
        op1 = input('')

        if op1 == '1':
            return 

        print('Enter Option: \n')
        print('1)Checking\n')
        print('2)Saving\n')
        opt2 = input('')

        while(opt2 not in ['1','2']):
            print('This account type is invalid, try again.')
            print('Enter Option: \n')
            print('1)Checking\n')
            print('2)Saving\n')
            opt2 = input('')

        if opt2 == '1':
            self.ac=AccountType.CHECKING
        else:
            self.ac=AccountType.SAVINGS

        



user=BankUser('Matheus')
sess=ATMSession(user)
sess.Interface()
