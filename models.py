import sqlite3
from database import db_path

DB_NAME = "history.db"

def connect():
    return sqlite3.connect(db_path)

def add_simple_interest(principal, interest_rate, time, earned, amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO simple_interest (principal, interest_rate, time, earned, amount)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ROUND(?, 2), ROUND(?, 2))
    """, (principal, interest_rate, time, earned, amount))
    conn.commit()
    conn.close()

def get_all_simple_interest():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM simple_interest")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_compound_interest(principal, interest_rate, time, compound_frequency, earned, amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO compound_interest (principal, interest_rate, time, compound_frequency, earned, amount)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ?, ROUND(?, 2), ROUND(?, 2))
    """, (principal, interest_rate, time, compound_frequency, earned, amount))
    conn.commit()
    conn.close()

def get_all_compound_interest():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compound_interest")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_flat_interest(principal, annual_interest, time, monthly_installment, paid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO flat_interest (principal, annual_interest, time, monthly_installment, paid)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ROUND(?, 2), ROUND(?, 2))
    """, (principal, annual_interest, time, monthly_installment, paid))
    conn.commit()
    conn.close()

def get_all_flat_interest():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flat_interest")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_amortization(principal, annual_interest, time, monthly_installment, paid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO amortization (principal, annual_interest, time, monthly_installment, paid)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ROUND(?, 2), ROUND(?, 2))
    """, (principal, annual_interest, time, monthly_installment, paid))
    conn.commit()
    conn.close()

def get_all_amortization():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM amortization")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_lump_investment(principal, annual_interest, time, compound_frequency, earned, future_amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO lump_investment (principal, annual_interest, time, compound_frequency, earned, future_amount)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ?, ROUND(?, 2), ROUND(?, 2))
    """, (principal, annual_interest, time, compound_frequency, earned, future_amount))
    conn.commit()
    conn.close()

def get_all_lump_investment():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lump_investment")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_systematic_investment(monthly_investment, annual_interest, time, earned, future_amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO systematic_investment (monthly_investment, annual_interest, time, earned, future_amount)
        VALUES (ROUND(?, 2), ROUND(?, 2), ?, ROUND(?, 2), ROUND(?, 2))
    """, (monthly_investment, annual_interest, time, earned, future_amount))
    conn.commit()
    conn.close()

def get_all_systematic_investment():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM systematic_investment")
    rows = cursor.fetchall()
    conn.close()
    return rows
