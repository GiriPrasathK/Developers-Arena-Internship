class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = isbn
        self.year = year
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available
        }

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} ({self.year}) | {status}"
