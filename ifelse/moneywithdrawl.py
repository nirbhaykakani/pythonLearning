balance = 20000
withdrawl=300

if withdrawl<balance and withdrawl%5==0:
    print("Withdrawl: ",withdrawl)
    balance=balance-withdrawl
    print("Amount left: ",balance)
else:
    print("Withdrawl not possible")