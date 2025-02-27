import sqlite3

def create_database():
    conn = sqlite3.connect("financial_app.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Accounts (
        account_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        balance REAL NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        account_id INTEGER,
        amount REAL NOT NULL,
        category_id INTEGER,
        transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
    );
    """)

    users_data = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com"),
        ("Diana White", "diana@example.com"),
        ("Evan Green", "evan@example.com")
    ]
    cursor.executemany("INSERT INTO Users (name, email) VALUES (?, ?);", users_data)

    accounts_data = [
        (1, 5000.00),
        (2, 3000.00),
        (3, 7000.00),
        (4, 4500.00),
        (5, 6000.00)
    ]
    cursor.executemany("INSERT INTO Accounts (user_id, balance) VALUES (?, ?);", accounts_data)

    categories_data = [
        ("Groceries",),
        ("Entertainment",),
        ("Utilities",),
        ("Rent",),
        ("Transport",)
    ]
    cursor.executemany("INSERT INTO Categories (category_name) VALUES (?);", categories_data)

    transactions_data = [
        (1, 1, 150.75, 1),
        (2, 2, 200.50, 2),
        (3, 3, 300.00, 3),
        (4, 4, 1200.00, 4),
        (5, 5, 50.25, 5)
    ]
    cursor.executemany("INSERT INTO Transactions (user_id, account_id, amount, category_id) VALUES (?, ?, ?, ?);", transactions_data)

    conn.commit()
    conn.close()
    print("Database, tables, and initial data created successfully.")

def query_users_with_transactions():
    conn = sqlite3.connect("financial_app.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users JOIN Transactions ON Users.user_id = Transactions.user_id;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_with_transactions AS 
    SELECT * FROM Users JOIN Transactions ON Users.user_id = Transactions.user_id;
    """)

    conn.commit()
    conn.close()
    print("Query executed: users with transactions saved in 'users_with_transactions'.")

def query_highest_transactions():
    conn = sqlite3.connect("financial_app.db")
    cursor = conn.cursor()

    cursor.execute("SELECT category_id, MAX(amount) FROM Transactions GROUP BY category_id;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS highest_transactions AS 
    SELECT category_id, MAX(amount) FROM Transactions GROUP BY category_id;
    """)

    conn.commit()
    conn.close()
    print("Query executed: highest transactions per category saved in 'highest_transactions'.")

if __name__ == "__main__":
    create_database()
    query_users_with_transactions()
    query_highest_transactions()
