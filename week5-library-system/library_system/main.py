from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Save & Exit")

def main():
    library = Library()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book(Book(
                input("Title: "),
                input("Author: "),
                input("ISBN: "),
                input("Year: ")
            ))

        elif choice == "2":
            library.register_member(Member(
                input("Name: "),
                input("Member ID: ")
            ))

        elif choice == "3":
            print(library.borrow_book(
                input("Member ID: "),
                input("ISBN: ")
            ))

        elif choice == "4":
            print(library.return_book(
                input("Member ID: "),
                input("ISBN: ")
            ))

        elif choice == "5":
            for book in library.find_book(input("Search keyword: ")):
                print(book)

        elif choice == "6":
            library.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()