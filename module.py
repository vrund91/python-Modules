''' 1. Create a module to create following functions
 • simple interest
 • deposit
 • withdrawl 
Create a main file and set current balance= 50000 and perform following.
 • Withdraw some amount and print remaining amount
 • deposit 5000
 • If balance is greater than 50000,give a interest of  5% and print updated amount'''


def simple_interest(p,r,n):
    si = (p * r * n) / 100
    print("simple Interest:",si)

def withdrawal(withdraw,curr_balance):
    curr_balance -= withdraw
    return curr_balance

def deposit(deposite,curr_balance):
    curr_balance += deposite
    if curr_balance > 50000:
        interest = curr_balance * 0.5
        print("Interest on current balance:", interest)
    else:
        print("Current Balance is:",curr_balance)

    return curr_balance