from library_system.book import Book

def test_book():
    b = Book("Python", "Guido", "123", 2020)
    assert b.available is True
