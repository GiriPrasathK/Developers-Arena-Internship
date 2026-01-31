from datetime import datetime, timedelta

MAX_BORROW_LIMIT = 5

class Member:
    def __init__(self, name, member_id):
        self.name = name.strip().title()
        self.member_id = member_id
        self.borrowed_books = {}  # isbn -> due_date

    def can_borrow(self):
        return len(self.borrowed_books) < MAX_BORROW_LIMIT

    def borrow_book(self, isbn):
        due_date = datetime.now() + timedelta(days=14)
        self.borrowed_books[isbn] = due_date.strftime("%Y-%m-%d")

    def return_book(self, isbn):
        return self.borrowed_books.pop(isbn, None)

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)}"
