def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance:
            return "You cannot withdraw more than you have in your current balance."
        else:
            return balance - amount
    return withdraw

init_bal = 1000.00
wd = make_withdraw(init_bal)
wd_amount = 50.00
print("New balance is: ${0:6.2f}".format(wd(wd_amount)))
new_wd_amount = 100.00
print("Updated balance is: ${0:6.2f}".format(wd(new_wd_amount)))