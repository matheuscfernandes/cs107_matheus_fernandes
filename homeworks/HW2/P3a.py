#closure function initiating the balance in the bank
def bank(balance):
    #inner function that decreases the nonlocal variable by the amount of the withdrawal
    def withdraw(amount):
        nonlocal balance
        balance-=amount
        #print the latest balance
        print(balance) 
    #return the withdraw function
    return withdraw

#initiate the bank account with a certain amount
bal=bank(100)
#withdraw 50 from the balance
bal(50)
#withdraw 30 from the new current balance
bal(30)