loan = eval(input("enter the loan -->"))
loan_period = eval(input("enter something -->" ))
loan_period *= 12
balance = loan
principal = loan / loan_period 
print("YOUR SUMMRY")
print("|MONTH\t|MONTLY\t|INTEREST\t|PRICIPAl\t|REAMINING BALANCE\t|")
print("_____________________________________________________________________________________________")
for i in range(1,loan_period+1,1):
    balance -= principal 
    interest = balance * 0.003
    monthly = principal + interest
    print(f"{i}\t|{round(monthly,2)}\t\t|{round(interest,2)}\t\t|{round(principal,2)}\t\t|{round(balance,2)}\t\t|")
