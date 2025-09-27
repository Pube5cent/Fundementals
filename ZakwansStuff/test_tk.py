import customtkinter as ctk

# ------------------------------ Functions ----------------------------------

def create_button(parent, text, command):  # button creation function
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

def create_quote(parent, text):  # quote creation function
    return ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 15),
        text_color="#cce0ff",
    )

def create_title(parent, text):  # title creation function
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

# ---------------------------- Pages (Frames) ---------------------------------

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#007acc")

        label = create_title(self, "Financial Buddy")
        label.pack(padx=20, pady=30)

        button1 = create_button(self, "Interest & Compound Interest",
                                lambda: controller.show_frame("SimpleCompoundPage"))
        button1.pack(padx=20, pady=30)

        button2 = create_button(self, "Loan & Mortgage", None)
        button2.pack(padx=20, pady=30)

        button3 = create_button(self, "Savings and Investment", None)
        button3.pack(padx=20, pady=30)

        quote = create_quote(self, "“Little drops of water make a\n mighty ocean”")
        quote.pack(padx=20, pady=40)


class SimpleCompoundPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#007acc")

        label = create_title(self, "Simple & Compound\nInterest")
        label.pack(padx=20, pady=30)

        button1 = create_button(self, "Simple Interest",
                                lambda: controller.show_frame("SimpleInterestPage"))
        button1.pack(padx=20, pady=30)

        button2 = create_button(self, "Compound Interest", None)
        button2.pack(padx=20, pady=30)

        quote = create_quote(self, "“Do not save what is left after spending,\n but spend what is left after saving”")
        quote.pack(padx=20, pady=40)

        back_btn = create_button(self, "← Back", lambda: controller.show_frame("HomePage"))
        back_btn.pack(pady=10)


class SimpleInterestPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#007acc")

        label = create_title(self, "Simple Interest")
        label.pack(padx=20, pady=30)

        self.Principal = create_input(self, "Principal")
        self.Principal.pack(padx=20, pady=15)

        self.Interest = create_input(self, "Annual Interest (decimal)")
        self.Interest.pack(padx=20, pady=15)

        self.Time = create_input(self, "Time (years)")
        self.Time.pack(padx=20, pady=15)

        equals = create_title(self, "=")
        equals.pack(padx=20, pady=15)

        back_btn = create_button(self, "← Back", lambda: controller.show_frame("SimpleCompoundPage"))
        back_btn.pack(pady=10)


# ---------------------------- Main App ---------------------------------

class FinancialBuddyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x650")
        self.title("Financial Buddy")
        self.configure(fg_color="#007acc")

        # container for frames
        container = ctk.CTkFrame(self, fg_color="#007acc")
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Add all pages
        for F in (HomePage, SimpleCompoundPage, SimpleInterestPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = FinancialBuddyApp()
    app.mainloop()
