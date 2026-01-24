import os

structure = {
    "week4-finance-tracker": {
        "finance_tracker": [
            "__init__.py",
            "main.py",
            "expense.py",
            "expense_manager.py",
            "file_handler.py",
            "reports.py",
            "utils.py"
        ],
        "data": {
            "files": ["expenses.json"],
            "backup": {},
            "exports": {}
        },
        "tests": [
            "test_expense.py",
            "test_file_handler.py",
            "test_reports.py"
        ],
        "requirements.txt": None
    }
}

def create(base, tree):
    for name, content in tree.items():
        path = os.path.join(base, name)
        if content is None:
            open(path, "w").close()
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                open(os.path.join(path, file), "w").close()
        elif isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create(path, content)

create(".", structure)
print("✅ Project structure created successfully!")
