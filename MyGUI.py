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

def create_home_button(parent, text, command): #home button function
    return ctk.CTkButton(
        parent,
        text=text,
        font=('Poppins', 20),
        text_color="#cce0ff",
        height=50,
        width=50,
        fg_color='#00509e',
        command=command
    )

def create_quote(parent, text): #quote creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 15),
        text_color="#cce0ff",
    )

def create_title(parent, text): #title creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 40, 'bold'),
        text_color="#cce0ff",
    )

def create_input(parent, placeholder):
    return ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        font=('Poppins', 20),
        text_color='black', 
        fg_color='white', 
        width=300,
        justify="center"
    )

# ---------------------------- Pages ---------------------------------

"""
def open_simple_compound(app): #Simple and Compound Interest page
    app.withdraw()

    simple_compound_window = ctk.CTkToplevel()
    simple_compound_window.configure(fg_color="#007acc")

    simple_compound_window.title("Financial Buddy")
    simple_compound_window.geometry("500x650")

    label = create_title(simple_compound_window, "Simple & Compound\n Interest")
    label.pack(padx=20, pady=30)

    button1 = create_button(simple_compound_window, "Simple Interest", lambda: open_calc_simple(simple_compound_window, app))
    button1.pack(padx=20, pady=30,)

    button2 = create_button(simple_compound_window, "Compound Interest", None)
    button2.pack(padx=20, pady=30,)

    quote = create_quote(simple_compound_window, "“Do not save what is left after spending,\n but spend what is left after saving”")
    quote.pack(padx=20, pady=40)

    simple_compound_window.protocol("WM_DELETE_WINDOW", lambda: (app.destroy(), simple_compound_window.destroy()))

def open_calc_simple(simple_compound_window, app): #Simple Interest calculation page
    simple_compound_window.withdraw()

    calc_simple = ctk.CTkToplevel()
    calc_simple.configure(fg_color="#007acc")

    calc_simple.title("Simple Interest")
    calc_simple.geometry("500x650")

    label = create_title(calc_simple, "Simple Interest")
    label.pack(padx=20, pady=30)

    Principal = create_input(calc_simple, "Principal")
    Principal.pack(padx=20, pady=15)

    Interest = create_input(calc_simple, "Annual Interest (decimal)")
    Interest.pack(padx=20, pady=15)

    Time = create_input(calc_simple, "Time (years)")
    Time.pack(padx=20, pady=15)

    label = create_title(calc_simple, "=")
    label.pack(padx=20, pady=15)

    calc_simple.protocol("WM_DELETE_WINDOW", lambda: (app.destroy(), calc_simple.destroy()))
"""

#--------------------------Main App-----------------------
def main_app():

    app = ctk.CTk()
    app.resizable(False, False)
    app.geometry("500x650")
    app.title("Financial Buddy")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

#-------------------------Pages---------------------------
    homepage = CTkFrame(app)
    option1 = CTkFrame(app)
    option2 = CTkFrame(app)
    option3 = CTkFrame(app)

    for frame in (homepage, option1, option2, option3):
        frame.configure(fg_color="#007acc")

    for frame in (homepage, option1, option2, option3):
        frame.grid(row=0, column=0, sticky="nsew")

#-----------------------Home page--------------------------
    label = create_title(homepage, "Financial Buddy")
    label.pack(padx=20, pady=30)

    button1 = create_button(homepage, "Interest & Compound Interest", lambda: option1.tkraise())
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

    button1 = create_button(option1, "Simple Interest", None)
    button1.pack(padx=20, pady=30)

    button2 = create_button(option1, "Compound Interest", None)
    button2.pack(padx=20, pady=30)

    quote = create_quote(option1, "“Do not save what is left after spending,\n but spend what is left after saving”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_home_button(option1, "🏠", lambda: homepage.tkraise())
    home_button.place(x=20, y=20)

#----------------------Loan--------------------------
    label = create_title(option2, "Loan &\n Mortgage")
    label.pack(padx=20, pady=30)

    button1 = create_button(option2, "Flat Interest", None)
    button1.pack(padx=20, pady=30)

    button2 = create_button(option2, "Amortization", None)
    button2.pack(padx=20, pady=30)

    quote = create_quote(option2, "“Small amounts saved daily add up to\n huge investments in the end”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_home_button(option2, "🏠", lambda: homepage.tkraise())
    home_button.place(x=20, y=20)

#---------------------Savings-------------------------
    label = create_title(option3, "Savings &\n Investment")
    label.pack(padx=20, pady=30)

    button1 = create_button(option3, "Lump Sum Investment", None)
    button1.pack(padx=20, pady=30)

    button2 = create_button(option3, "Systematic Investment\n Plan", None)
    button2.pack(padx=20, pady=30)

    quote = create_quote(option3, "“An investment in knowledge pays the\n best interest”")
    quote.place(x=250, y=550, anchor="center")

    home_button = create_home_button(option3, "🏠", lambda: homepage.tkraise())
    home_button.place(x=20, y=20)

#---------------------App Running------------------------
    homepage.tkraise()
    app.mainloop()

if __name__ == "__main__":
    main_app()

    #myentry = ctk.CTkEntry(self.root, font=('Poppins', 20), text_color="#cce0ff", fg_color='white')
    #myentry.pack()