from finance_tracker.file_handler import FileHandler
from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = FileHandler.load()

    def add(self, expense: Expense):
        expense.validate()
        self.expenses.append(expense.__dict__)
        FileHandler.save(self.expenses)

    def remove(self, index):
        self.expenses.pop(index)
        FileHandler.save(self.expenses)

    def search(self, keyword):
        return [
            e for e in self.expenses
            if keyword.lower() in e["description"].lower()
            or keyword.lower() in e["category"].lower()
        ]

    def filter_by_category(self, category):
        return [e for e in self.expenses if e["category"] == category]

    def all(self):
        return self.expenses
