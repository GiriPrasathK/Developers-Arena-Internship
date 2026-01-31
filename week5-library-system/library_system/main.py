from .library import Library

def main():
    lib = Library()

    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Library Statistics")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            lib.add_book(
                input("Title: "),
                input("Author: "),
                input("ISBN: "),
                input("Year: ")
            )
            print("Book added.")

        elif choice == "2":
            lib.register_member(
                input("Member Name: "),
                input("Member ID: ")
            )
            print("Member registered.")

        elif choice == "3":
            print(lib.borrow_book(
                input("Member ID: "),
                input("ISBN: ")
            ))

        elif choice == "4":
            print(lib.return_book(
                input("Member ID: "),
                input("ISBN: ")
            ))

        elif choice == "5":
            results = lib.find_book(input("Search keyword: "))
            for b in results:
                print(b)

        elif choice == "6":
            total, available = lib.stats()
            print(f"Total Books: {total}, Available: {available}")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
