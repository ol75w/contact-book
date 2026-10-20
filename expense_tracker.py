expenses = []


def add_expense():
    name = input("Expense name: ")

    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    category = input("Category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - "
            f"{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spending: {total:.2f}")


def category_summary():
    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n--- Category Summary ---")

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"{removed['name']} deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Show category spending")
    print("5. Delete expense")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")