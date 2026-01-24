from finance_tracker.expense import Expense

def test_validation():
    e = Expense("2026-01-01", 100, "Food", "Lunch")
    e.validate()
    try:
        e_invalid = Expense("2026-13-01", -50, "", "")
        e_invalid.validate()
        assert False, "Validation should have failed"
    except ValueError:
        pass
def test_to_from_dict():
    e = Expense("2026-01-01", 100, "Food", "Lunch", True)
    d = e.to_dict()
    e2 = Expense.from_dict(d)
    assert e == e2
def test_str():
    e = Expense("2026-01-01", 100, "Food", "Lunch", True)
    s = str(e)
    assert "Expense(date=2026-01-01, amount=100, category=Food, description=Lunch, recurring=True)" == s
