from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    #initialize the bank account class with necessary informaiton 
    def __init__(self, owner, accountType: AccountType):
        self.owner=owner
        self.accountType=accountType
        self.balance=float(0)

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
        currentBal=self.balance
        newBal=currentBal+amount

        self.balance=newBal


    def __str__(self):
        #return string that contains the owner information and the account type
        return 'Owner Name: {}; Account type: {}'.format(self.owner,self.accountType.name)

    def __len__(self):
        #return the float balance of the account
        return int(self.balance)


class BankUser():
    #initialize the bank user class with the necessary information
    def __init__(self, owner):
        self.owner=owner
        self.acct={}
    
    def addAccount(self, accountType):
        try: # check if there is an existing bank account
            self.acct[accountType]
            raise Exception('Account: {} already exists'.format(accountType.name))
        #if account does not exist create one and set the balance to 0
        except:
            self.acct[accountType] = BankAccount(self.owner,accountType)

    def getBalance(self, accountType):
        #check if account esists, if so return the balance and if not raise and expetion
        try:
            self.acct[accountType]
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))
        
        #return balance of particular account
        return len(self.acct[accountType])
        
    def deposit(self, accountType, amount):
        #try to see if account exists, if so update balancem, if not raise an exception error
        try:
            self.acct[accountType]
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))
        
        #update the account with the amount deposited
        self.acct[accountType].deposit(amount)


    def withdraw(self, accountType, amount):
        #try to see if account exists, if so update balancem, if not raise an exception error
        try:
            self.acct[accountType]
        except:
            raise Exception('Account {} for {} does not exists'.format(accountType.name,self.owner))
        
        #update the account with the amount deposited
        self.acct[accountType].withdraw(amount)


    def __str__(self):
        #create a string that provides the owners name and each account type as well as corresponding balance. Return that string.
        vals='Owner Name: {}\n'.format(self.owner)
        for i in self.acct:
            vals+='Account type: {} -- Balance: {} \n'.format(i.name,len(self.acct[i]))
        return vals


def ATMSession(bu):

    def Interface():
        #make sure that the bu varaible is nonlocal and amendable in this closure
        nonlocal bu

        #prompt user for the option they want
        print('Enter Option: \n')
        print('1)Exit\n')
        print('2)Create Account\n')
        print('3)Check Balance\n')
        print('4)Deposit\n')
        print('5)Withdraw \n')
        opt1 = input('')

        #make sure the selection is valid
        while(opt1 not in ['1','2','3','4','5']):
            print('This selection is invalid, try again.')
            print('Enter Option: \n')
            print('1)Exit\n')
            print('2)Create Account\n')
            print('3)Check Balance\n')
            print('4)Deposit\n')
            print('5)Withdraw \n')
            opt1 = input('')

        #if exit selection, make sure to exit
        if opt1 == '1':
            return 
        
        #if not exit, query the user for which account type they want to try next
        print('Enter Option: \n')
        print('1)Checking\n')
        print('2)Saving\n')
        opt2 = input('')

        #make sure the selection is valid
        while(opt2 not in ['1','2']):
            print('This account type is invalid, try again.')
            print('Enter Option: \n')
            print('1)Checking\n')
            print('2)Saving\n')
            opt2 = input('')

        #store the account type in internal variable based on selection
        if opt2 == '1':
            at=AccountType.CHECKING
        else:
            at=AccountType.SAVINGS


        #if creating an account, create an account
        if opt1 == '2':
            try:
                bu.getBalance(at)
                print('{} account already exists!'.format(at.name))

            except:
                bu.addAccount(at)
                print('{} account Created'.format(at.name))

        try:
            #check if account exists
            bu.getBalance(at)
            #if checking balance, provide balance
            if opt1 =='3':
                try:
                    print('Owner: {} \nAccount: {}\nBalance: {}'.format(bu.owner,at.name,bu.getBalance(at)))
                except:
                    print('{} account does not exist!'.format(at.name))
            
            #if making a deposit or withdawal, query user for the amount
            if opt1 in ['4','5']:
                while True:
                    opt3 = input('Enter a non-negative amount: ')
                    #see if the amount is valid for the user
                    try:
                        if opt1 =='4':
                            bu.deposit(at,float(opt3))
                            print('Owner: {} \nAccount: {}\nNew Balance: {}'.format(bu.owner,at.name,bu.getBalance(at)))
                            break
                    except:
                        print('Invalid amount,try again')

                    try:
                        if opt1 =='5':
                            bu.withdraw(at,float(opt3))
                            print('Owner: {} \nAccount: {}\nNew Balance: {}'.format(bu.owner,at.name,bu.getBalance(at)))
                            break
                    #if amount is not valid for the user, let them know and let them try again
                    except:
                        if (bu.getBalance(at)-int(opt3))<0:
                            print("Insufficient Funds, {} account has Balance of {}".format(at.name,bu.getBalance(at)))
                        else:
                            print('Invalid amount, try again')

                        
        # if account does not exist flag user
        except:
                print('{} account does not exist'.format(at.name))

        Interface()

    return Interface

        

user=BankUser('Matheus')
sess=ATMSession(user)
sess()
