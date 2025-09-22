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

 #add a cheeky little tittle
print("Semi Functional Calculator")

 #print options for the user
while True:
    print("Features: ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Power")
    print("F. Percentage Converter")
    print("G. Exit")
 #ask user which feature they wanna use
    choice = input("Which would you like to proceed with? : ")
 #ask user for values in life
    if choice.upper() == "A":
        print("Addition")
        a = input("First number: ")
        b = input("Second number: ")
        add(a, b)
    elif choice.upper() == "B":
        print("Subtraction")
        a = input("First number: ")
        b = input("Second number: ")
        sub(a, b)
    elif choice.upper() == "C":
        print("Multiplication")
        a = input("First number: ")
        b = input("Second number: ")
        mul(a, b)
    elif choice.upper() == "D":
        print("Division")
        a = input("First number: ")
        b = input("Second number: ")
         # add a math/syntax error
        if b == "0":
            print("Math Error" + "\n")
        if b != "0":
            div(a, b)
    elif choice.upper() == "E":
        print("Power")
        a = input("First number: ")
        b = input("Second number: ")
        pow(a, b)
    elif choice.upper() == "F":
        print("Percentage Converter")
        a = input("First number: ")
        b = input("Second number: ")
        # add a math/syntax error
        if b == "0":
            print("WARNING: Math Error" + "\n")
        if b != "0":
            per(a, b)
            # quitters module
    elif choice.upper() == "G":
            print("Have a nice day")
            quit()
    # if the user choses something out of bound, dis prompt {not a valid command or something idk}d
    else:
        print("Not an Option" + "\n")

