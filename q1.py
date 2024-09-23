from module import simple_interest,withdrawal,deposit

print("1. Simple Interest")
print("2. Deposit and Withdrawal")

choice = int(input("Enter a choice: "))

if choice == 1:
    p = float(input("Enter principal amount: "))
    r = float(input("Enter interest rate: "))
    n = float(input("Enter number of years: "))
    
    simple_interest(p, r, n)
    
elif choice == 2:
    curr_balance = 50000
    print("Current balance:", curr_balance)
    
    withdraw = float(input("Enter amount to withdraw: "))
    curr_balance = withdrawal(withdraw, curr_balance)
    print("After withdraw current balance:",curr_balance)
    
    deposite = float(input("Enter amount to deposit: "))
    curr_balance = deposit(deposite, curr_balance)
    
else:
    print("Invalid operation")
