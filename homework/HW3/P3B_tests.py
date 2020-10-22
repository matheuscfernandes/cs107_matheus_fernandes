from Bank import AccountType,BankAccount,BankUser


def test_over_withdrawal(): #this test function should throw an Exception or Error 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    user.withdraw(AccountType.SAVINGS, 1);
    print(user.getBalance(AccountType.SAVINGS));
    print(user);

    
    #CHECK WITHDRAWAL LARGER THAN BALANCE
    try:
        user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

    #CHECK NEGATIVE WITHDRAWAL 
    try:
        user.withdraw(AccountType.SAVINGS, -10); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

    #CHECK NEGATIVE DEPOSIT 
    try:
        user.deposit(AccountType.SAVINGS, -10); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

    #CHECK ACCOUNT TYPE WORKS FOR GETBALACE
    try:
        user.getBalance(AccountType.CHECKING); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

    #CHECK ACCOUNT TYPE WORKS FOR DEPOSIT
    try:
        user.deposit(AccountType.CHECKING,1); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

    #CHECK ACCOUNT TYPE WORKS FOR WITHDRAWAL
    try:
        user.withdraw(AccountType.CHECKING,1); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

test_over_withdrawal();