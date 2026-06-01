from database import (
    init_db,
    add_transaction,
    get_transactions,
    get_balance
)

init_db()

while True:
    print("\n=== Personal Finance Manager ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show transactions")
    print("4. Show balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Income source: ")
        amount = float(input("Amount: "))

        add_transaction(
            "income",
            category,
            amount
        )

        print("✅ Income added.")

    elif choice == "2":
        category = input("Expense category: ")
        amount = float(input("Amount: "))

        add_transaction(
            "expense",
            category,
            amount
        )

        print("✅ Expense added.")

    elif choice == "3":
        transactions = get_transactions()

        print("\n📋 Transactions:")

        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print(transaction)

    elif choice == "4":
        balance = get_balance()

        print(f"\n💰 Current balance: {balance}")

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option.")