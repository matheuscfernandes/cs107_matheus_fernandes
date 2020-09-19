def bank(balance):
    def withdraw(amount):
        balance-=amount
        print(balance) 
    return withdraw

bal=bank(100)
bal(30)
bal(30)