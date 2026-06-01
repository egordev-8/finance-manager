import sqlite3

def init_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()


def add_transaction(transaction_type, category, amount):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions(type, category, amount) VALUES (?, ?, ?)",
        (transaction_type, category, amount)
    )

    conn.commit()
    conn.close()


def get_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT type, category, amount FROM transactions"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def get_balance():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        SUM(
            CASE
                WHEN type='income' THEN amount
                ELSE -amount
            END
        )
        FROM transactions
    """)

    balance = cursor.fetchone()[0]

    conn.close()

    return balance if balance else 0