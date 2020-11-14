import Bank as bank

#test that user can make savings account, deposit into it, and withdraw from it
user1 = bank.BankUser("Joe");
user1.addAccount(bank.AccountType.SAVINGS); # 1 point for adding account to user
user1.deposit(bank.AccountType.SAVINGS, 100); # 1 point for depositing correctly into account
print("Savings:",user1.getBalance(bank.AccountType.SAVINGS));
user1.withdraw(bank.AccountType.SAVINGS, 51); # 1 point for withdrawing correctly into account
print("Savings:",user1.getBalance(bank.AccountType.SAVINGS));
print(user1);
print()

#test that user can't withdraw more than balance in account
try:
    user1.withdraw(bank.AccountType.SAVINGS, 10000);
except Exception as e:
    print(e);
    
#test that user can't withdraw a negative balance in account
try:
    user1.withdraw(bank.AccountType.SAVINGS, -10);
except Exception as e:
    print(e);
    
#test that user can't deposit a negative balance in savings account
try:
    user1.deposit(bank.AccountType.SAVINGS, -10);
except Exception as e:
    print(e);
print()
    
##############################################################

#test that user can't have more than one savings/checking account
try:
    user1.addAccount(bank.AccountType.SAVINGS);
except Exception as e:
    print(e);

#test that user can't deposit into non-existent account
try:
    user1.deposit(bank.AccountType.CHECKING, 10);
except Exception as e:
    print(e);
    
#test that user can't withdraw from non-existent account
try:
    user1.withdraw(bank.AccountType.CHECKING, 10);
except Exception as e:
    print(e);
    
#test that user can't get balance from non-existent account
try:
    user1.getBalance(bank.AccountType.CHECKING);
except Exception as e:
    print(e);
print();

###############################################################

#test that user can make checking account, deposit into it, and withdraw from it
user1.addAccount(bank.AccountType.CHECKING);
user1.deposit(bank.AccountType.CHECKING, 50);
print("Checking:",user1.getBalance(bank.AccountType.CHECKING));
user1.withdraw(bank.AccountType.CHECKING, 20);
print("Checking:",user1.getBalance(bank.AccountType.CHECKING));
print(user1);