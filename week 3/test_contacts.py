
---

## 🧪 `test_contacts.py` (Basic Testing Script)


from contact_manager import validate_phone, validate_email

assert validate_phone("9876543210") == True
assert validate_phone("12345") == False

assert validate_email("test@email.com") == True
assert validate_email("invalidemail") == False

print("All tests passed!")
