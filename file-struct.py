import os

structure = {
    "week5-library-system": [
        "requirements.txt",
        "README.md",
        ".gitignore",
        {
            "library_system": [
                "__init__.py",
                "book.py",
                "member.py",
                "library.py",
                "main.py"
            ]
        },
        {
            "data": [
                "books.json",
                "members.json",
                {"backup": []}
            ]
        },
        {
            "tests": [
                "test_book.py",
                "test_member.py",
                "test_library.py"
            ]
        }
    ]
}

def create_structure(base_path, items):
    for item in items:
        if isinstance(item, dict):
            for folder, contents in item.items():
                path = os.path.join(base_path, folder)
                os.makedirs(path, exist_ok=True)
                create_structure(path, contents)
        else:
            open(os.path.join(base_path, item), "a").close()

for root, contents in structure.items():
    os.makedirs(root, exist_ok=True)
    create_structure(root, contents)

print("✅ Library Management System file structure created successfully!")
