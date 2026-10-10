import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading expenses file.")
    return []


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error saving expenses.")


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter expense category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['category']} "
            f"- ₹{expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ₹{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
    