import sqlite3

def connect_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    # Jadval yaratish
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type TEXT CHECK( type IN ('income','expense') ) NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL
                    )''')
    conn.commit()
    return conn, cursor

def close_db(conn):
    conn.close()
