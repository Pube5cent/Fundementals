import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("history.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS simple_interest (
    simple_interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    principal DECIMAL NOT NULL,
    interest_rate DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    earned DECIMAL NOT NULL,
    AMOUNT DECIMAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS compound_interest (
    compound_interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    principal DECIMAL NOT NULL,
    interest_rate DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    compound_frequency INTEGER NOT NULL,
    earned DECIMAL NOT NULL,
    AMOUNT DECIMAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flat_interest (
    flat_interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    principal DECIMAL NOT NULL,
    annual_interest DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    monthly_installment DECIMAL NOT NULL,
    paid DECIMAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS amortization (
    amortization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    principal DECIMAL NOT NULL,
    annual_interest DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    monthly_installment DECIMAL NOT NULL,
    paid DECIMAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lump_investment (
    lump_investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    principal INTEGER NOT NULL,
    annual_interest DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    compound_frequency INTEGER NOT NULL,
    earned DECIMAL NOT NULL,
    future_amount DECIMAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS systematic_investment (
    systematic_investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    monthly_investment DECIMAL NOT NULL,
    annual_interest DECIMAL NOT NULL,
    time INTEGER NOT NULL,
    compound_frequency INTEGER NOT NULL,
    earned DECIMAL NOT NULL,
    future_amount DECIMAL NOT NULL
);
""")

# Insert sample values

# Simple Interest: principal=1000, rate=5%, time=2 years
cursor.execute("""
INSERT INTO simple_interest (principal, interest_rate, time, earned, amount) 
VALUES (?, ?, ?, ?, ?)
""", (1000, 5.0, 2, 100, 1100))

# Compound Interest: principal=2000, rate=6%, time=3 years, quarterly compounding
cursor.execute("""
INSERT INTO compound_interest (principal, interest_rate, time, compound_frequency, earned, amount) 
VALUES (?, ?, ?, ?, ?, ?)
""", (2000, 6.0, 3, 4, 382.03, 2382.03))

# Flat Interest Loan: principal=5000, 10% annual, 2 years, monthly installment=229.17, total paid=5500
cursor.execute("""
INSERT INTO flat_interest (principal, annual_interest, time, monthly_installment, paid) 
VALUES (?, ?, ?, ?, ?)
""", (5000, 10.0, 2, 229.17, 5500))

# Amortization Loan: principal=8000, 7% annual, 3 years, monthly installment=246.60, total paid=8877.60
cursor.execute("""
INSERT INTO amortization (principal, annual_interest, time, monthly_installment, paid) 
VALUES (?, ?, ?, ?, ?)
""", (8000, 7.0, 3, 246.60, 8877.60))

# Lump Sum Investment: 10000 at 5% for 5 years, yearly compounding
cursor.execute("""
INSERT INTO lump_investment (principal, annual_interest, time, compound_frequency, earned, future_amount) 
VALUES (?, ?, ?, ?, ?, ?)
""", (10000, 5.0, 5, 1, 2762.82, 12762.82))

# Systematic Investment (SIP): 500 monthly, 12% annual, 10 years, monthly compounding
cursor.execute("""
INSERT INTO systematic_investment (monthly_investment, annual_interest, time, compound_frequency, earned, future_amount) 
VALUES (?, ?, ?, ?, ?, ?)
""", (500, 12.0, 10, 12, 43233.38, 113233.38))

# Save changes and close
conn.commit()
conn.close()