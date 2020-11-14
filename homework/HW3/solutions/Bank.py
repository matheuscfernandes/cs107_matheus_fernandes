from enum import Enum

class AccountType(Enum):
    SAVINGS = 1;
    CHECKING = 2;

class BankAccount():
    '''Class for creating a bank account. Allows for deposits and withdrawals.
    '''
    def __init__(self, owner: str, accountType: AccountType):
        self.owner = owner;
        self.accountType = accountType;
        self.balance = 0.0;

    def withdraw(self, amount: float):
        '''This method adds "amount" to the account's current balance.
        '''
        #Do some logical checks
        assert self.balance >= amount, Exception("You cannot withdraw ${:.2f}. You will over-draw the account. Currently, your balance is ${:.2f}".format(amount, self.balance));
        assert amount >= 0, Exception("Your withdrawal must be greater than or equal to $0.");
        #if amount is ok
        self.balance = self.balance - amount;

    def deposit(self, amount: float):
        '''This method adds "amount" to the account's current balance.
        '''
        #Do some logical checks
        assert amount >= 0, Exception("Your deposit must be greater than or equal to $0.");
        
        self.balance = self.balance + amount;

    def __str__(self):
        return ("Owner: {0},\tAccount Type: {1}".format(self.owner, self.accountType.name));

    def __len__(self):
        return int(self.balance);

class BankUser():
    '''Class for a bank customer.
    '''
    def __init__(self, owner):
        self.owner = owner;
        self.savings_account = None;
        self.checking_account = None;
    
    def addAccount(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.savings_account == None:
                self.savings_account = BankAccount(self.owner, accountType);
            else:
                raise Exception("User already has a savings account. You cannot have more than one savings account.");
        elif accountType == AccountType.CHECKING:
            if self.checking_account == None:
                self.checking_account = BankAccount(self.owner,accountType);
            else:
                raise Exception("User already has a checking account. You cannot have more than one checking account.");

    def getBalance(self, accountType):
    	'''Returns the balance of the specified 'accountType.' Throws an error if the user does not have the specified 'account.'
    	'''
    	if accountType == AccountType.SAVINGS:
    		if self.savings_account != None:
    			return self.savings_account.balance;
    		else:
    			raise Exception("User does not have a savings account.");
    	if accountType == AccountType.CHECKING:
    		if self.checking_account != None:
    			return self.checking_account.balance;
    		else:
    			raise Exception("User does not have a checking account");

    def deposit(self, accountType, amount):
    	'''Adds 'amount' to the balance of the specified 'accountType.' Throws an error if the user does not have the specified 'account.'
    	'''
    	#check if account is SAVINGS
    	if accountType == AccountType.SAVINGS:
    		if self.savings_account != None:
    			self.savings_account.deposit(amount);
    		else:
    			raise Exception("User does not have a savings account.");
    	#check if account is CHECKING
    	if accountType == AccountType.CHECKING:
    		if self.checking_account != None:
    			self.checking_account.deposit(amount);
    		else:
    			raise Exception("User does not have a checking account");

    def withdraw(self, accountType, amount):
    	'''Substracts 'amount' to the balance of the specified 'accountType.' Throws an error if the user does not have the specified 'account' or if 'amount' is greater than the balance of the specified 'accountType.'
    	'''
    	#check if account is SAVINGS
    	if accountType == AccountType.SAVINGS:
    		if self.savings_account != None:
    			self.savings_account.withdraw(amount);
    		else:
    			raise Exception("User does not have a savings account.");
    	#check if account is CHECKING
    	if accountType == AccountType.CHECKING:
    		if self.checking_account != None:
    			self.checking_account.withdraw(amount);
    		else:
    			raise Exception("User does not have a checking account");

    def __str__(self):
    	
    	savings_str = "No savings account for {0}".format(self.owner);
    	checking_str = "No checking account for {0}".format(self.owner);
    	#check if there's a savings account
    	if self.savings_account != None:
    		savings_str = str(self.savings_account)+",\tBalance: ${:.2f}".format(self.savings_account.balance);
    	#check if there's a checking account
    	if self.checking_account != None:
    		checking_str = str(self.checking_account)+",\tBalance: ${:.2f}".format(self.checking_account.balance);
    	return (savings_str + "\n" + checking_str); 

def ATMSession(bankUser: BankUser):
    assert type(bankUser) == BankUser, Exception("ATMSession must take in a BankUser object.");

    def Interface():
        nonlocal bankUser; #make the bankUser that is passed in a nonlocal variable so it can be changed
        
        #internal method for getting user's input
        def get_option(input_message: str, poss_options: list): #gets the option from the user
            option = input(input_message);
            if option not in poss_options: #handle malformed case
                return -1;
            else:
                return option;

        #internal method to convert user's input to the correct account type
        def get_account_type(account_option):
            if account_option == "1":
                return AccountType.CHECKING;
            elif account_option == "2":
                return AccountType.SAVINGS;
            else:
                return -1;

        #internal method to check if user has the account selected
        def checkUserAccounts(bankUser: BankUser, atype: AccountType):
            if atype == AccountType.SAVINGS and bankUser.savings_account == None:
                raise Exception("You do not have a SAVINGS account.");
            if atype == AccountType.CHECKING and bankUser.checking_account == None:
                raise Exception("You do not have a CHECKING account.");

        #internal method to get the deposit or withdrawal amount from user. The method will keep looping until user puts in a valid number
        def get_amount(input_message: str):
            amount = input(input_message);
            try:
                amount = float(amount); #will raise Exception if amount is a float
                if amount < 0: #check input is positive
                    raise Exception();
                return amount;
            except: #catch exceptions for non-integers or negative numbers
                raise Exception("You must input a non-negative, integer amount.");
        

        while True: #endless while loop
            home_option = get_option(input_message="Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n", poss_options=["1","2","3","4","5"]);
            if home_option == -1: #check if user put in malformed entry
                print("Not a valid option.");
                continue; #go back to home screen
            elif home_option == "1": #exit since user put in 1
                return;
            #user wants to do something with accounts
            account_option = get_option(input_message="Enter Option:\n1)Checking\n2)Savings\n", poss_options=["1","2"]); #get account option
            if account_option == -1: #if input is malformed, return to home screen
                print("Not a valid account option. Returning to home screen.");
                continue; #go back to home screen
            
            atype = get_account_type(account_option); #convert option to AccountType
            try:
                if home_option == "2": #user wants to make new account
                    bankUser.addAccount(atype); #add account for user
                    print("Created a {0} account for {1}\n".format(atype.name, bankUser.owner));
                
                elif home_option == "3": #user wants to check balance
                    checkUserAccounts(bankUser, atype);
                    bal = bankUser.getBalance(atype);
                    print("{0} account balance: ${1:.2f}\n".format(atype.name, bal));
                
                elif home_option == "4": #user wants to make deposit
                    checkUserAccounts(bankUser, atype);
                    amount = get_amount("Enter Integer Amount, Cannot Be Negative:\n");
                    bankUser.deposit(atype, amount);
                    print("{0} account balance is now ${1:.2f}\n".format(atype.name, bankUser.getBalance(atype)) );

                elif home_option == "5": #user wants to make withdrawal
                    checkUserAccounts(bankUser, atype);
                    amount = get_amount("Enter Integer Amount, Cannot Be Negative:\n");
                    bankUser.withdraw(atype, amount);
                    print("{0} account balance is now ${1:.2f}\n".format(atype.name, bankUser.getBalance(atype)) );
            except Exception as e:
                    print(str(e)); #print message from Exception
                    continue; #return to home screen

    return Interface;


