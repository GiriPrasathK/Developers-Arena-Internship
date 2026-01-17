# 📇 Contact Management System

## Project Overview

A Python-based Contact Management System developed using **functions and dictionaries**. This application allows users to efficiently store, search, update, and manage contact details through a console-based interface.

---

## Features

* Add new contacts with phone and email validation
* Update existing contact information
* Search contacts using partial name matching
* Display contacts in a formatted manner
* Group contacts (Friends, Work, Family, Other)
* Timestamp tracking for creation and updates

---

## Technologies Used

* **Programming Language:** Python 3
* **Libraries:**

  * `re` – input validation
  * `datetime` – timestamp handling
  * `json` – data persistence (optional)
  * `csv` – export functionality (optional)

---

## How to Run

```bash
# Navigate to project directory
cd Dev Arena Intern > week 3 

# Run the program
python contacts_manager.py
```

---

## Data Structure

```python
contacts = {
    "Name": {
        "phone": "9876543210",
        "email": "example@gmail.com",
        "address": "City",
        "group": "Friends",
        "created_at": "timestamp",
        "updated_at": "timestamp"
    }
}
```

---

## Future Scope

* JSON-based persistent storage
* CSV export
* Menu-driven UI
* GUI/Web-based extension

---

**Author:** GiriPrasath K – Week 3 Practical
