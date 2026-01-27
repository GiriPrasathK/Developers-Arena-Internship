import json
import os
from datetime import datetime
from .book import Book
from .member import Member

BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"
BACKUP_DIR = "data/backup/"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    # ---------- Book Management ----------
    def add_book(self, book):
        self.books[book.isbn] = book

    def find_book(self, keyword):
        return [
            book for book in self.books.values()
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
            or keyword == book.isbn
        ]

    # ---------- Member Management ----------
    def register_member(self, member):
        self.members[member.member_id] = member

    def find_member(self, member_id):
        return self.members.get(member_id)

    # ---------- Borrow / Return ----------
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)

        if not member or not book:
            return "Invalid member or book"

        if not book.check_out():
            return "Book not available"

        if not member.borrow_book(isbn):
            book.return_book()
            return "Borrow limit reached"

        return "Book borrowed successfully"

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)

        if not member or not book:
            return "Invalid return"

        member.return_book(isbn)
        overdue_days = 0

        if book.is_overdue():
            overdue_days = (datetime.now() - book.due_date).days

        book.return_book()
        return f"Returned successfully. Overdue days: {overdue_days}"

    # ---------- Persistence ----------
    def save_data(self):
        os.makedirs(BACKUP_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"{BACKUP_DIR}/backup_{timestamp}.json", "w") as f:
            json.dump({
                "books": {k: v.to_dict() for k, v in self.books.items()},
                "members": {k: v.to_dict() for k, v in self.members.items()}
            }, f, indent=4)

        with open(BOOKS_FILE, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open(MEMBERS_FILE, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE) as f:
                for k, v in json.load(f).items():
                    self.books[k] = Book.from_dict(v)

        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE) as f:
                for k, v in json.load(f).items():
                    self.members[k] = Member.from_dict(v)
    def get_book_by_isbn(self, isbn):
        return self.books.get(isbn)
    # ---------- Reporting ----------
    def overdue_report(self):
        report = []
        for member in self.members.values():
            if member.has_overdue_books(self):
                report.append(member)
        return report
    def inventory_report(self):
        return list(self.books.values())
    def member_report(self):
        return list(self.members.values())