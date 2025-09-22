import os

#clean debug screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#makes sure its a number
def get_number(prompt="Enter a number: "):
    while True:  
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

#define the functions of the calculator: add, sub, mul, div, pow
def add(a, b):
    answer = float(a) + float(b)
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")
def sub(a, b):
    answer = float(a) - float(b)
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")
def mul(a, b):
    answer = float(a) * float(b)
    print(str(a) + "x" + str(b) + "=" + str(answer) + "\n")
def div(a, b):
    answer = float(a) / float(b)
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")
def pow(a, b):
    answer = float(a) ** float(b)
    print(str(a) + "^" + str(b) + "=" + str(answer) + "\n")
def per(a, b):
        answer = (float(a) / float(b)) * 100
        print(str(a) + "^" + str(b) + " x 100" + "=" + str(answer) + "%" + "\n")

clear_console()

 #print options for the user
while True:
    print("Semi Functional Calculator")
    print("Features: ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Power")
    print("F. Percentage Converter")
    print("G. Simple Interest")
    print("H. Exit")
 #ask user which feature they wanna use
    choice = input("Which would you like to proceed with? : ")
 #ask user for values in life
    if choice.upper() == "A":
        clear_console()
        print("Addition")
        a = get_number("First number: ")
        b = get_number("Second number: ")
        add(a, b)
    elif choice.upper() == "B":
        clear_console()
        print("Subtraction")
        a = get_number("First number: ")
        b = get_number("Second number: ")
        sub(a, b)
    elif choice.upper() == "C":
        clear_console()
        print("Multiplication")
        a = get_number("First number: ")
        b = get_number("Second number: ")
        mul(a, b)
    elif choice.upper() == "D":
        clear_console()
        print("Division")
        a = get_number("First number: ")
        b = get_number("Second number: ")
         # add a math/syntax error
        if b == "0":
            print("Math Error" + "\n")
        if b != "0":
            div(a, b)
    elif choice.upper() == "E":
        clear_console()
        print("Power")
        a = get_number("First number: ")
        b = get_number("Second number: ")
        pow(a, b)
    elif choice.upper() == "F":
        clear_console()
        print("Percentage Converter")
        a = get_number("First number: ")
        b = get_number("Second number: ")
        # add a math/syntax error
        if b == "0":
            print("WARNING: Math Error" + "\n")
        if b != "0":
            per(a, b)
    elif choice.upper() == "G":
        clear_console()
        print("Simple Interest")
        P = get_number("Loan amount: ")
        b = get_number("Annual interest rate [decimal]: ")
        r = float(b) / 100
        t = get_number("Loan term[Year]: ")
        e = get_number("Number of months: ")
        n = float(e) * 12
        TotalInterest = str(float(P) * float(r) * float(t))
        TotalRepayment = str(float(P) + float(TotalInterest))
        MonthlyPayment = str(float(TotalRepayment) / float(n))
        print("Your Total Interest is: " + str(TotalInterest))
        print("Your Total Repayment is: " + str(TotalRepayment))
        print("And Your Monthly Repayment is: " + str(MonthlyPayment))

    # quitters module
    elif choice.upper() == "H":
            print("Have a nice day")
            quit()
    # if the user choses something out of bound, dis prompt {not a valid command or something idk}d
    else:
        print("Not an Option" + "\n")

