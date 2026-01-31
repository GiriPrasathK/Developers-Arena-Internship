from library_system.member import Member, MAX_BORROW_LIMIT

def test_member_creation():
    m = Member("john doe", "M001")
    assert m.name == "John Doe"
    assert m.member_id == "M001"
    assert m.borrowed_books == {}

def test_member_borrow_book():
    m = Member("Alice", "M002")
    m.borrow_book("ISBN123")

    assert "ISBN123" in m.borrowed_books
    assert len(m.borrowed_books) == 1

def test_member_return_book():
    m = Member("Bob", "M003")
    m.borrow_book("ISBN999")

    returned = m.return_book("ISBN999")
    assert returned is not None
    assert "ISBN999" not in m.borrowed_books

def test_borrow_limit():
    m = Member("Charlie", "M004")

    for i in range(MAX_BORROW_LIMIT):
        m.borrow_book(f"ISBN{i}")

    assert m.can_borrow() is False
