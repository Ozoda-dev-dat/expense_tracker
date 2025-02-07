from datetime import datetime
from database import connect_db, close_db

def add_transaction(transaction_type, category, amount):
    """ Xarajat yoki daromad qo'shish """
    conn, cursor = connect_db()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)", 
                   (transaction_type, category, amount, date))
    conn.commit()
    close_db(conn)
    print("✅ Ma'lumot muvaffaqiyatli qo'shildi!")

def view_balance():
    """ Jami balansni ko'rish """
    conn, cursor = connect_db()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0
    close_db(conn)
    print(f"💰 Jami daromad: {income} so'm")
    print(f"💸 Jami xarajat: {expense} so'm")
    print(f"💵 Qolgan balans: {income - expense} so'm")

def view_transactions():
    """ Oxirgi 10 ta tranzaksiyani ko'rish """
    conn, cursor = connect_db()
    cursor.execute("SELECT type, category, amount, date FROM transactions ORDER BY date DESC LIMIT 10")
    transactions = cursor.fetchall()
    close_db(conn)
    
    if not transactions:
        print("🚫 Hozircha hech qanday ma'lumot yo'q!")
    else:
        print("\n📝 Oxirgi 10 tranzaksiya:")
        for t in transactions:
            print(f"[{t[3]}] {t[0].capitalize()} - {t[1]}: {t[2]} so'm")
