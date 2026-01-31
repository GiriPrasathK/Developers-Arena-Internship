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

    # ---------------- FILE HANDLING ----------------

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as f:
                for b in json.load(f):
                    book = Book(**b)
                    book.available = b["available"]
                    self.books[book.isbn] = book

        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE, "r") as f:
                for m in json.load(f):
                    member = Member(m["name"], m["member_id"])
                    member.borrowed_books = m["borrowed_books"]
                    self.members[member.member_id] = member

    def save_data(self):
        os.makedirs(BACKUP_DIR, exist_ok=True)

        with open(BOOKS_FILE, "w") as f:
            json.dump([b.to_dict() for b in self.books.values()], f, indent=4)

        with open(MEMBERS_FILE, "w") as f:
            json.dump([m.to_dict() for m in self.members.values()], f, indent=4)

    # ---------------- BOOK METHODS ----------------

    def add_book(self, title, author, isbn, year):
        if isbn not in self.books:
            self.books[isbn] = Book(title, author, isbn, year)

    def find_book(self, keyword):
        return [
            b for b in self.books.values()
            if keyword.lower() in b.title.lower()
            or keyword.lower() in b.author.lower()
            or keyword == b.isbn
        ]

    # ---------------- MEMBER METHODS ----------------

    def register_member(self, name, member_id):
        if member_id not in self.members:
            self.members[member_id] = Member(name, member_id)

    # ---------------- BORROW / RETURN ----------------

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member or not book or not book.available:
            return "Borrow failed."

        if not member.can_borrow():
            return "Borrow limit reached."

        book.check_out()
        member.borrow_book(isbn)
        self.save_data()
        return "Book borrowed successfully."

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member or not book:
            return "Invalid return."

        due = member.return_book(isbn)
        book.return_book()
        self.save_data()

        if due:
            due_date = datetime.strptime(due, "%Y-%m-%d")
            if datetime.now() > due_date:
                return "Returned late (Overdue)."
        return "Book returned successfully."

    # ---------------- STATISTICS ----------------

    def stats(self):
        total = len(self.books)
        available = sum(1 for b in self.books.values() if b.available)
        return total, available
