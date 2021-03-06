#closure function initiating the balance in the bank
def bank(balance):
    #inner function that decreases the balance variable by the amount of the withdrawal
    def withdraw(amount):
        try:
            new_bal=new_bal-amount
            print('updating balance')
        except:
            new_bal=balance-amount
        #print the latest balance
        print(new_bal) 
    #return the withdraw function
    return withdraw

#printing discussion on what is going on in this problem
print('This does not behave correctly because there is no way to keep the information stored in the new_bal variable (as this variable is maintained in the local frame and is reset whenever the function is over) as this variable is not a global variable unlike the balance variable. Therefore, every time the closure is re-called, the new_bal variable is re-uptaded with the balance that we started with.')

#initiate the bank account with a certain amount
wd=bank(100)

#withdraw 50 from the balance
wd(50)
#withdraw 30 from the new current balance
wd(30)

#checking for basic exceptions
wd(150)
wd(-50)