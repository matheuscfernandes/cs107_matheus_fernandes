#closure function initiating the balance in the bank
def bank(balance):
    #inner function that decreases the nonlocal variable by the amount of the withdrawal
    def withdraw(amount):
        balance-=amount
        #print the latest balance
        print(balance) 
    #return the withdraw function
    return withdraw


print('Did not work because the identifier balance refers to a previously bound variable that was defined outside of this frame -- therefore you can read, but you cannot alter the variable.')

#initiate the bank account with a certain amount
wd=bank(100)
#withdraw 50 from the balance
wd(50)
#withdraw 30 from the new current balance
wd(30)