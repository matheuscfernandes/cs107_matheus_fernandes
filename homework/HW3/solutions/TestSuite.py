# tests to run given module, return score
def testSuite (m, repo):
    print ("--- TESTING: ", repo)
    
    points = 0;
    comments = []; #list to hold the comments as autograders got through
    
    SAVINGS = m.AccountType.SAVINGS
    CHECKING = m.AccountType.CHECKING
    # create a bank account and bank user- worth 1 point. Just check no errors thrown
    try:
        acc = m.BankAccount('Charles Liu', m.AccountType.SAVINGS);
        user = m.BankUser('Charles Liu');
        points += 1;
    except:
        # if this doesn't work, then it's a 0
        comments.append('Class instantiation didnt work.');
        return (points, comments);
    
    ####### test BankAccount class- worth 8 points #######################################
    #test len method for BankAccount
    try:
        assert(len(acc) == 0);
        points += 1;
    except:
        comments.append('-1 point: __len__ method is not defined correctly for BankAccount class.');
    
    #test withdraw method of BankAccount
    try:
        acc.withdraw(100); #should return some Exception because no balance
    except:
        points += 2; #raised proper Exception
        pass;
    else:
        comments.append('-2 point: withdraw method for BankAccount class does not raise Exception for over-withdrawal when balance=0.');
    
    #test that we can deposit money
    try:
        acc.deposit(100);
        points += 1;
    except:
        comments.append('-1 point: deposit method for BankAccount class raised some Exception when used.');
    
    #test withdraw method of BankAccount after we deposited money
    try:
        acc.withdraw(10);
        assert(len(acc) == 90);
        points += 1;
    except:
        comments.append('-1 point: withdraw method for BankAccount class did not work properly.');
    
    #test that deposit throws Exception when negative integer is used
    try:
        acc.deposit(-10);
        comments.append('-2 point: deposit method for BankAccount class did not raise an Exception when a negative number was used.');
    except:
        points += 2;
        
    try: #test that __str__ method is implement properly
        if('<Bank.BankAccount' in str(acc)):
            raise Exception();
        points += 1;
    except:
        comments.append('-1 point: __str__ not implemented for BankAccount class.');
    
    ####### test BankUser class- worth 15 pts #######################################
    try: #test that Exception is thrown when getBalance is called on non-existent account
        user.getBalance(SAVINGS);
        comments.append('-2 point: Savings account hasnt been created yet but getbalance() does not raise Exception');
    except:
        points += 2;
        
    try: #test that Exception is thrown when withdraw is called on non-existent account
        user.withdraw(SAVINGS, 10);
        comments.append('-1 point: Savings account hasnt been created yet but withdraw does not raise an Exception.');
    except:
        points += 1;
        
    try: #test that Exception is thrown when deposit is called on non-existent account
        user.deposit(SAVINGS, 10);
        comments.append('-1 point: Savings account hasnt been created yet but deposit does not raise an Exception.');
    except:
        points += 1;
    
    #try adding SAVINGS account
    try:
        user.addAccount(SAVINGS);
        points += 1;
    except:
        comments.append('-1 points: Could not add SAVINGS account for user.');
        return (points, comments); #if addAccount throws error, then we can't test the rest of the methods
    
    #try adding second SAVINGS account. Should throw exception
    try:
        user.addAccount(SAVINGS);
        comments.append('-1 points: We were able to add a second SAVINGS account for user but this should have thrown an Exception.');
    except:
        points += 1;    
    
    #try adding CHECKING account
    try:
        user.addAccount(CHECKING);
        points += 1;
    except:
        comments.append('-1 points: Could not add Checking account for user.');
        return (points, comments); #if addAccount throws error, then we can't test the rest of the methods
    
    #try getBalance() of CHECKING
    try:
        assert(user.getBalance(CHECKING) == 0);
        points += 1;
    except:
        comments.append('-1 points: CHECKING account balance was not 0 at initialization.');
    
    #try depositing negative amount into checking account. (2pts)
    try:
        user.deposit(CHECKING, -10); #this may raise an Exception
    except:
        points += 2; #student gets 1 point for properly raising an Exception
    else: #possible that student caught Exception in deposit method, but balance of CHECKING does not change
        try:
            assert(user.getBalance(CHECKING) == 0);
            points += 2;
        except:
            comments.append('-2 points: We could deposit -10 into CHECKING account.');
            # Try to recover by adding 10 back in
            try:
                user.deposit(CHECKING, 10)
            except:
                print("Couldn't recover from depositing negative balance")
    
    #try depositing 100 into CHECKING
    try:
        user.deposit(CHECKING, 100);
        assert(user.getBalance(CHECKING)==100);
        points += 2;
    except:
        comments.append('-2 points: Could not properly deposit 100 into CHECKING account.');
    
    #try withdrawing 10 from CHECKING
    try:
        user.withdraw(CHECKING, 10);
        assert(user.getBalance(CHECKING)==90);
        points += 2;
    except:
        comments.append('-2 points: Could not properly withdraw 10 from CHECKING account.');
    
    #test that __str__ method is implement properly for Bank User
    try:
        if('<Bank.BankUser' in str(user)):
            raise Exception();
        points += 1;
    except:
        comments.append('-1 point: __str__ not implemented for BankUser class.');
        
    
    ####### test Interface class- worth 6 pts #######################################
    try:  
        # Choose Deposit
        print ("RUNNING TEST: #####################")
        with contextlib.redirect_stdout(None):
            user = m.BankUser('Charles Liu');
            user.addAccount(CHECKING)
#         TypewriteThread(['4', '\n'], sleep=5.0).start()
#         # Choose CHECKING
#         TypewriteThread(['1', '\n'], sleep=10.0).start()
#         # Deposit 1 into CHECKING so total is 91
#         TypewriteThread(['1', '\n'], sleep=15.0).start()
#         # Exit prompt
#         TypewriteThread(['1', '\n'], sleep=20.0).start()
        interface = m.ATMSession(user)
        interface()
    except:
        pass
    if user.getBalance(CHECKING) != 1:
        comments.append('-6 points: ATMSession did not update CHECKING account properly.');
    else:
        points += 6;
    
    
    if(len(comments) == 0): #no issues with code
        comments.append('SUCCESSFUL')
    
    return (points, comments);
