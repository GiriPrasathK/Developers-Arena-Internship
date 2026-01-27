from library_system.book import Book

def test_book_checkout():
    book = Book("Test", "Author", "123", 2023)
    assert book.check_out() is True
    assert book.available is False
    assert book.due_date is not None
    assert book.check_out() is False  # Cannot check out again
def test_book_return():
    book = Book("Test", "Author", "123", 2023)
    book.check_out()
    book.return_book()
    assert book.available is True
    assert book.due_date is None
def test_book_overdue():
    book = Book("Test", "Author", "123", 2023)
    book.check_out(days=-1)  # Set due date in the past
    assert book.is_overdue() is True
    book.return_book()
    assert book.is_overdue() is False
def test_book_to_from_dict():
    book = Book("Test", "Author", "123", 2023)
    book.check_out()
    data = book.to_dict()
    new_book = Book.from_dict(data)
    assert new_book.title == book.title
    assert new_book.author == book.author
    assert new_book.isbn == book.isbn
    assert new_book.year == book.year
    assert new_book.available == book.available
    assert new_book.due_date == book.due_date
def test_book_str():
    book = Book("Test", "Author", "123", 2023)
    assert str(book) == "Test by Author (123) - Available"
    book.check_out()
    assert "Due:" in str(book)
    assert str(book).startswith("Test by Author (123) - Due:")