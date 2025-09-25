import customtkinter as ctk
from customtkinter import CTkFrame


# ------------------------------ Functions ----------------------------------

def create_button(parent, text, command): #button creation function
    return ctk.CTkButton(
        parent,
        text=text,
        font=('Poppins', 20),
        text_color="#cce0ff",
        height=60,
        width=300,
        fg_color='#00509e',
        command=command
    )

def create_back_button(parent, text, page, inputs=None): #home button function
    def go_back():
        if inputs:
            for input in inputs:
                placeholder = input._placeholder_text
                input.delete(0, "end")
                input.configure(placeholder_text=placeholder)
        page.tkraise()

    button = ctk.CTkButton(
        parent,
        text=text,
        font=('Poppins', 20),
        text_color="#cce0ff",
        height=50,
        width=50,
        fg_color='#00509e',
        command= go_back
    )
    button.place(x=20, y=20)
    return button

def create_quote(parent, text): #quote creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 15),
        text_color="#cce0ff",
    )

def create_title(parent, text, font=40): #title creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', font, 'bold'),
        text_color="#cce0ff",
    )

def create_text(parent, text): #text creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 20, 'bold'),
        text_color="#cce0ff",
    )

def create_input(parent, placeholder, font=20):
    return ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        font=('Poppins', font),
        text_color='black', 
        fg_color='white', 
        width=300,
        justify="center"
    )

#--------------------------Main App-----------------------
def main_app():

    app = ctk.CTk()
    app.resizable(False, False)
    app.geometry("500x650")
    app.title("Financial Buddy💸")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

#-------------------------Pages---------------------------
    homepage = CTkFrame(app)
    option1 = CTkFrame(app)
    option2 = CTkFrame(app)
    option3 = CTkFrame(app)
    simple_interest = CTkFrame(app)
    compound_interest = CTkFrame(app)
    flat_interest = CTkFrame(app)
    amortization = CTkFrame(app)
    lump_sum = CTkFrame(app)
    SIP_investment = CTkFrame(app)

    for frame in (homepage, option1, option2, option3, simple_interest, compound_interest, flat_interest, amortization, lump_sum, SIP_investment):
        frame.configure(fg_color="#007acc")

    for frame in (homepage, option1, option2, option3, simple_interest, compound_interest, flat_interest, amortization, lump_sum, SIP_investment):
        frame.grid(row=0, column=0, sticky="nsew")

#-----------------------Home page--------------------------
    label = create_title(homepage, "Financial Buddy💸")
    label.pack(padx=20, pady=30)

    button1 = create_button(homepage, "Simple & Compound Interest", lambda: option1.tkraise())
    button1.pack(padx=20, pady=30)

    button2 = create_button(homepage, "Loan & Mortgage", lambda: option2.tkraise())
    button2.pack(padx=20, pady=30)

    button3 = create_button(homepage, "Savings and Investment", lambda: option3.tkraise())
    button3.pack(padx=20, pady=30)

    quote = create_quote(homepage, "“Little drops of water make a\n mighty ocean”")
    quote.place(x=250, y=550, anchor="center")

#-----------------------Interest----------------------------
    label = create_title(option1, "Simple &\n Compound Interest")
    label.pack(padx=20, pady=30)

    button1 = create_button(option1, "Simple Interest", lambda: simple_interest.tkraise())
    button1.pack(padx=20, pady=30)

    button2 = create_button(option1, "Compound Interest", lambda: compound_interest.tkraise())
    button2.pack(padx=20, pady=30)

    quote = create_quote(option1, "“Do not save what is left after spending,\n but spend what is left after saving”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_back_button(option1, "🏠", homepage)

#----------------------Loan--------------------------
    label = create_title(option2, "Loan &\n Mortgage")
    label.pack(padx=20, pady=30)

    button1 = create_button(option2, "Flat Interest", lambda: flat_interest.tkraise())
    button1.pack(padx=20, pady=30)

    button2 = create_button(option2, "Amortization", lambda: amortization.tkraise())
    button2.pack(padx=20, pady=30)

    quote = create_quote(option2, "“Small amounts saved daily add up to\n huge investments in the end”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_back_button(option2, "🏠", homepage)

#---------------------Savings-------------------------
    label = create_title(option3, "Savings &\n Investment")
    label.pack(padx=20, pady=30)

    button1 = create_button(option3, "Lump Sum Investment", lambda: lump_sum.tkraise())
    button1.pack(padx=20, pady=30)

    button2 = create_button(option3, "Systematic Investment\n Plan", lambda: SIP_investment.tkraise())
    button2.pack(padx=20, pady=30)

    quote = create_quote(option3, "“An investment in knowledge pays the\n best interest”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_back_button(option3, "🏠", homepage)

#---------------------Simple Interest Calculation--------------
    label = create_title(simple_interest, "Simple Interest")
    label.pack(padx=20, pady=30)

    Principal_SI = create_input(simple_interest, "Principal")
    Principal_SI.pack(padx=20, pady=15)

    Interest_SI = create_input(simple_interest, "Annual Interest (decimal)")
    Interest_SI.pack(padx=20, pady=15)

    Time_SI = create_input(simple_interest, "Time (years)")
    Time_SI.pack(padx=20, pady=15)

    def calculate_simple_interest():
        try:
            P = float(Principal_SI.get())
            R = float(Interest_SI.get())
            T = float(Time_SI.get())
            SI = P * R * T
            FV = SI + P
            result_SI.configure(text=f"Interest earned = {SI:.2f}\n Future Value = {FV:.2f}")
        except ValueError:
            result_SI.configure(text="⚠️Enter valid numbers⚠️")

    calc_button = create_button(simple_interest, "Calculate", calculate_simple_interest)
    calc_button.pack(padx=20, pady=20)

    result_SI = create_text(simple_interest, "Future Value =\n Interest earned =")
    result_SI.pack(padx=20, pady=30)

    back_button = create_back_button(simple_interest, "⬅️", option1, (Principal_SI, Interest_SI, Time_SI))

#----------------------Compound Interest Calculation-----------------
    label = create_title(compound_interest, "Compound Interest", 30)
    label.pack(padx=20, pady=30)

    Principal_CI = create_input(compound_interest, "Principal")
    Principal_CI.pack(padx=20, pady=15)

    Interest_CI = create_input(compound_interest, "Annual Interest (decimal)")
    Interest_CI.pack(padx=20, pady=15)

    Time_CI = create_input(compound_interest, "Time (years)")
    Time_CI.pack(padx=20, pady=15)

    Compound_CI = create_input(compound_interest, "Compound Frequency / year", 19)
    Compound_CI.pack(padx=20, pady=15)

    def calculate_compound_interest():
        try:
            P = float(Principal_CI.get())
            R = float(Interest_CI.get())
            T = float(Time_CI.get())
            N = float(Compound_CI.get())
            FV = P * ( 1 + (R / N)) ** (N * T)
            CI = FV - P
            result_CI.configure(text=f"Interest earned = {CI:.2f}\n Future Value = {FV:.2f}")
        except ValueError:
            result_CI.configure(text="⚠️Enter valid numbers⚠️")
        except ZeroDivisionError:
            result_CI.configure(text="Cannot divide by 0")

    calc_button = create_button(compound_interest, "Calculate", calculate_compound_interest)
    calc_button.pack(padx=20, pady=20)

    result_CI = create_text(compound_interest, "Future Value =\n Interest earned =")
    result_CI.pack(padx=20, pady=30)

    back_button = create_back_button(compound_interest, "⬅️", option1, (Principal_CI, Interest_CI, Time_CI, Compound_CI))

#-----------------------Loan Flat Interest Calculation---------------------
    label = create_title(flat_interest, "Flat Interest Loan", 35)
    label.pack(padx=20, pady=30)

    Principal_FI = create_input(flat_interest, "Principal")
    Principal_FI.pack(padx=20, pady=15)

    Interest_FI = create_input(flat_interest, "Annual Interest (decimal)")
    Interest_FI.pack(padx=20, pady=15)

    Time_FI = create_input(flat_interest, "Time (years)")
    Time_FI.pack(padx=20, pady=15)

    def calculate_flat_interest_loan():
        try:
            P = float(Principal_FI.get())
            R = float(Interest_FI.get())
            T = float(Time_FI.get())
            FI = P * R * T
            Total_repayment = FI + P
            Monthly_installment = Total_repayment / (12 * T)
            result_FI.configure(text=f"Monthly Installment = {Monthly_installment:.2f}\n Interest Paid = {FI:.2f}")
        except ValueError:
            result_FI.configure(text="⚠️Enter valid numbers⚠️")

    calc_button = create_button(flat_interest, "Calculate", calculate_flat_interest_loan)
    calc_button.pack(padx=20, pady=20)

    result_FI = create_text(flat_interest, "Monthly Installment =\n Interest Paid =")
    result_FI.pack(padx=20, pady=30)

    back_button = create_back_button(flat_interest, "⬅️", option2, (Principal_FI, Interest_FI, Time_FI))

#-----------------------Amortization Calculation---------------------
    label = create_title(amortization, "Amortization", 40)
    label.pack(padx=20, pady=30)

    Principal_A = create_input(amortization, "Principal")
    Principal_A.pack(padx=20, pady=15)

    Interest_A = create_input(amortization, "Annual Interest (decimal)")
    Interest_A.pack(padx=20, pady=15)

    Time_A = create_input(amortization, "Time (years)")
    Time_A.pack(padx=20, pady=15)

    def calculate_amortization():
        try:
            P = float(Principal_A.get())
            R = float(Interest_A.get())
            r = R / 12
            T = float(Time_A.get())
            n = T*12
            EMI = (P * r * (1 + r)**(n)) / ((1 + r)**n - 1)
            Total_repayment = EMI * n
            Interest_paid = Total_repayment - P
            result_A.configure(text=f"Monthly Installment = {EMI:.2f}\n Interest Paid = {Interest_paid:.2f}")
        except ValueError:
            result_A.configure(text="⚠️Enter valid numbers⚠️")

    calc_button = create_button(amortization, "Calculate", calculate_amortization)
    calc_button.pack(padx=20, pady=20)

    result_A = create_text(amortization, "Monthly Installment =\n Interest Paid =")
    result_A.pack(padx=20, pady=30)

    back_button = create_back_button(amortization, "⬅️", option2, (Principal_A, Interest_A, Time_A))

#-----------------------Lump Sum Investment---------------------
    label = create_title(lump_sum, "Lump Sum Investment", 30)
    label.pack(padx=20, pady=30)

    Principal_LS = create_input(lump_sum, "Principal")
    Principal_LS.pack(padx=20, pady=15)

    Interest_LS = create_input(lump_sum, "Annual Interest (decimal)")
    Interest_LS.pack(padx=20, pady=15)

    Time_LS = create_input(lump_sum, "Time (years)")
    Time_LS.pack(padx=20, pady=15)

    Compound_LS = create_input(lump_sum, "Compound Frequency / year", 19)
    Compound_LS.pack(padx=20, pady=15)

    def calculate_lump_sum():
        try:
            P = float(Principal_LS.get())
            R = float(Interest_LS.get())
            T = float(Time_LS.get())
            n = float(Compound_LS.get())
            FV = P * (1 + R/n)**(n*T)
            Interest_earned = FV - P
            result_LS.configure(text=f"Future Value = {FV:.2f}\n Interest Earned = {Interest_earned:.2f}")
        except ValueError:
            result_LS.configure(text="⚠️Enter valid numbers⚠️")

    calc_button = create_button(lump_sum, "Calculate", calculate_lump_sum)
    calc_button.pack(padx=20, pady=20)

    result_LS = create_text(lump_sum, "Future Value =\n Interest Earned =")
    result_LS.pack(padx=20, pady=30)

    back_button = create_back_button(lump_sum, "⬅️", option3, (Principal_LS, Interest_LS, Time_LS, Compound_LS))

#-----------------------SIP Investment---------------------
    label = create_title(SIP_investment, "Systematic Investment", 28)
    label.pack(padx=20, pady=(40, 0))
    label = create_title(SIP_investment, "Plan", 28)
    label.pack(padx=20, pady=0)

    Monthly_Investment_SIP = create_input(SIP_investment, "Monthly Investment")
    Monthly_Investment_SIP.pack(padx=20, pady=15)

    Interest_SIP = create_input(SIP_investment, "Annual Interest (decimal)")
    Interest_SIP.pack(padx=20, pady=15)

    Time_SIP = create_input(SIP_investment, "Time (years)")
    Time_SIP.pack(padx=20, pady=15)

    Compound_SIP = create_input(SIP_investment, "Compound Frequency / year", 19)
    Compound_SIP.pack(padx=20, pady=15)

    def calculate_SIP():
        try:
            P = float(Monthly_Investment_SIP.get())
            R = float(Interest_SIP.get())
            T = float(Time_SIP.get())
            n = float(Compound_SIP.get())
            FV = P * (( (1 + R/n)**(n * T) - 1 ) / (R / n)) * (1 + R/n)
            Interest_earned = FV - (P * T * 12)
            result_SIP.configure(text=f"Future Value = {FV:.2f}\n Interest Earned = {Interest_earned:.2f}")
        except ValueError:
            result_SIP.configure(text="⚠️Enter valid numbers⚠️")

    calc_button = create_button(SIP_investment, "Calculate", calculate_SIP)
    calc_button.pack(padx=20, pady=20)

    result_SIP = create_text(SIP_investment, "Future Value =\n Interest Earned =")
    result_SIP.pack(padx=20, pady=30)

    back_button = create_back_button(SIP_investment, "⬅️", option3, (Monthly_Investment_SIP, Interest_SIP, Time_SIP, Compound_SIP))

#---------------------App Running------------------------
    homepage.tkraise()
    app.mainloop()

if __name__ == "__main__":
    main_app()