class Member:
    MAX_BORROW_LIMIT = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            return False
        self.borrowed_books.append(isbn)
        return True

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        member = Member(data["name"], data["member_id"])
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)}"
    def has_overdue_books(self, library):
        for isbn in self.borrowed_books:
            book = library.get_book_by_isbn(isbn)
            if book and book.is_overdue():
                return True
        return False