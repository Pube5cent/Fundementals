import sqlite3
import os

DB_NAME = "history.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "history.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

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
        earned DECIMAL NOT NULL,
        future_amount DECIMAL NOT NULL
    );
    """)

conn.commit()
conn.close()