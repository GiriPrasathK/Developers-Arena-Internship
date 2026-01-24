def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for i, e in enumerate(expenses):
        print(f"{i}. {e['date']} | ₹{e['amount']} | {e['category']} | {e['description']}")
