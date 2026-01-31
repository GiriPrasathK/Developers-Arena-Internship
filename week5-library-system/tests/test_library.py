from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

def test_add_and_find_book():
    lib = Library()
    lib.books = {}  # isolate test

    lib.add_book("Python Basics", "Guido", "ISBN001", 2021)
    results = lib.find_book("Python")

    assert len(results) == 1
    assert results[0].isbn == "ISBN001"

def test_register_member():
    lib = Library()
    lib.members = {}

    lib.register_member("Alice", "M100")
    assert "M100" in lib.members

def test_borrow_book_success():
    lib = Library()
    lib.books = {}
    lib.members = {}

    lib.add_book("ML Book", "Andrew", "ISBN777", 2020)
    lib.register_member("Rahul", "M200")

    msg = lib.borrow_book("M200", "ISBN777")
    assert msg == "Book borrowed successfully."
    assert lib.books["ISBN777"].available is False

def test_return_book():
    lib = Library()
    lib.books = {}
    lib.members = {}

    lib.add_book("AI Book", "Russell", "ISBN888", 2019)
    lib.register_member("Neha", "M300")

    lib.borrow_book("M300", "ISBN888")
    msg = lib.return_book("M300", "ISBN888")

    assert lib.books["ISBN888"].available is True
    assert "returned" in msg.lower()

def test_library_statistics():
    lib = Library()
    lib.books = {}

    lib.add_book("Book 1", "Author A", "1", 2020)
    lib.add_book("Book 2", "Author B", "2", 2021)

    total, available = lib.stats()
    assert total == 2
    assert available == 2
