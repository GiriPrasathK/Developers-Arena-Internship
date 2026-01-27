from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.due_date = None

    def check_out(self, days=14):
        if not self.available:
            return False
        self.available = False
        self.due_date = datetime.now() + timedelta(days=days)
        return True

    def return_book(self):
        self.available = True
        self.due_date = None

    def is_overdue(self):
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["title"], data["author"], data["isbn"], data["year"])
        book.available = data["available"]
        book.due_date = (
            datetime.fromisoformat(data["due_date"])
            if data["due_date"] else None
        )
        return book

    def __str__(self):
        status = "Available" if self.available else f"Due: {self.due_date.date()}"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"
