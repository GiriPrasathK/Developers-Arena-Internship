from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import Reports
from finance_tracker.utils import print_expenses
from finance_tracker.file_handler import FileHandler

def main():
    manager = ExpenseManager()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Category Report")
        print("5. Monthly Report")
        print("6. Export CSV")
        print("7. Predict Next Month")
        print("8. Exit")

        choice = input("Choice: ")

        try:
            if choice == "1":
                e = Expense(
                    input("Date (YYYY-MM-DD): "),
                    float(input("Amount: ")),
                    input("Category: "),
                    input("Description: ")
                )
                manager.add(e)
                print("Expense added ✅")

            elif choice == "2":
                print_expenses(manager.all())

            elif choice == "3":
                key = input("Keyword: ")
                print_expenses(manager.search(key))

            elif choice == "4":
                Reports.visualize(Reports.category(manager.all()))

            elif choice == "5":
                Reports.visualize(Reports.monthly(manager.all()))

            elif choice == "6":
                FileHandler.export_csv(manager.all())
                print("Exported to CSV 📁")

            elif choice == "7":
                print("Predicted next month expense: ₹",
                      Reports.predict_next_month(manager.all()))

            elif choice == "8":
                break

            else:
                print("Invalid option")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
