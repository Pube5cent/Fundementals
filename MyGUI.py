import customtkinter as ctk

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

def main_app(): #Home page

    app = ctk.CTk()
    app.resizable(False, False)
    app.configure(fg_color="#007acc")

    app.geometry("500x650")
    app.title("Financial Buddy")

    label = create_title(app, "Financial Buddy")
    label.pack(padx=20, pady=30)

    button1 = create_button(app, "Interest & Compound Interest", lambda: open_simple_compound(app))
    button1.pack(padx=20, pady=30,)

    button2 = create_button(app, "Loan & Mortgage", None)
    button2.pack(padx=20, pady=30,)

    button3 = create_button(app, "Savings and Investment", None)
    button3.pack(padx=20, pady=30,)

    quote = create_quote(app, "“Little drops of water make a\n mighty ocean”")
    quote.pack(padx=20, pady=40)

    app.mainloop()

if __name__ == "__main__":
    main_app()

    #myentry = ctk.CTkEntry(self.root, font=('Poppins', 20), text_color="#cce0ff", fg_color='white')
    #myentry.pack()