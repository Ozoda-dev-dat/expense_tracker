from models import add_transaction, view_balance, view_transactions

def main():
    while True:
        print("\n=== Expense Tracker CLI ===")
        print("1️⃣ Xarajat qo'shish")
        print("2️⃣ Daromad qo'shish")
        print("3️⃣ Balansni ko'rish")
        print("4️⃣ Oxirgi xarajatlarni ko'rish")
        print("0️⃣ Chiqish")
        
        choice = input("Tanlang: ")
        
        if choice == "1":
            category = input("Xarajat kategoriyasi: ")
            amount = float(input("Miqdori: "))
            add_transaction("expense", category, amount)
        elif choice == "2":
            category = input("Daromad manbasi: ")
            amount = float(input("Miqdori: "))
            add_transaction("income", category, amount)
        elif choice == "3":
            view_balance()
        elif choice == "4":
            view_transactions()
        elif choice == "0":
            print("👋 Chiqish...")
            break
        else:
            print("🚫 Noto'g'ri tanlov! Qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
