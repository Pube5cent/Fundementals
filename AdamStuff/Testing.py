print("Simple Interest")
P = input("Loan amount: ")
b = input("Annual interest rate [decimal]: ")
r = b / 100
t = input("Loan term[Year]: ")
e = input("Number of months: ")
n = e * 12
TotalInterest = P * r * t
TotalRepayment = P + TotalInterest
MonthlyPayment = TotalRepayment / n
print("Your Total Interest is:" + TotalInterest)