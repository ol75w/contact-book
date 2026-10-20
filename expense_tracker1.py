import json

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
        print("No expenses found!")
        return

    print("---Expenses---")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']}-"
              f"{expense['amount']:.2f}-"
              f"{expense['category']}"
              )

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total: {total:.2f}")

def category_summary():
    if not expenses:
        print("No expense found!")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("---Category Summary---")

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses to delete!")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"{removed['name']} has been removed")
        else:
            print("Invalid expense number!")
    except ValueError:
        print("Please enter a valid number!")

def search_expense():
    search = input("Enter expense name or category to search: ").lower()

    found = False

    for index, expense in enumerate(expenses, start=1):
        if (search in expense["name"].lower() or
                search in expense["category"].lower()):

            print(f"{index}. {expense['name']} - "
                  f"{expense['amount']:.2f} - "
                  f"{expense['category']}")

            found = True

    if not found:
        print("No matching expenses found!")

def edit_expense():
    if not expenses:
        print("No expenses to edit!")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to edit: "))

        if 1 <= choice <= len(expenses):
            expense = expenses[choice - 1]

            print("\nWhat do you want to edit?")
            print("1. Name")
            print("2. Amount")
            print("3. Category")

            edit_choice = input("Choose an option: ")

            if edit_choice == "1":
                expense["name"] = input("Enter new name: ")
                print("Name updated successfully!")

            elif edit_choice == "2":
                while True:
                    try:
                        amount = float(input("Enter new amount: "))

                        if amount <= 0:
                            print("Amount must be greater than 0.")
                        else:
                            expense["amount"] = amount
                            print("Amount updated successfully!")
                            break

                    except ValueError:
                        print("Please enter a valid number.")

            elif edit_choice == "3":
                expense["category"] = input("Enter new category: ")
                print("Category updated successfully!")

            else:
                print("Invalid option!")

        else:
            print("Invalid expense number!")

    except ValueError:
        print("Please enter a valid number!")

def save_file():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)

def load_file():
    try:
        with open("expenses.json", 'r') as f:
            data = json.load(f)
            expenses.extend(data)
    except FileNotFoundError:
        pass
    

load_file()
while True:


    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Show category spending")
    print("5. Delete expense")
    print("6. Search expense")
    print("7. Edit expense")
    print("8. Exit")

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
        search_expense()

    elif choice == "7":
        edit_expense()

    elif choice == "8":
        print("Goodbye!")
        save_file()
        break

    else:
        print("Invalid choice.")
