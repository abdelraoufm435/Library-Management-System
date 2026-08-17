from library import (
    Book,
    BookNotAvailableError,
    BookNotFoundError,
    DuplicateEntryError,
    Library,
    Member,
    MemberNotFoundError,
    load_library,
    save_library,
)



DATA_FILE = "library.json"


def print_menu():
    print(
        """
1. Add book
2. Remove book
3. Add member
4. Remove member
5. Search books
6. List all books
7. List available books
8. Borrow book
9. Return book
10. List borrowed books
11. Most borrowed book
12. Save library
13. Exit
"""
    )


def main():
    library = Library()
    load_library(library, DATA_FILE)

    while True:
        print_menu()
        choice = input("Choose an option: ")

        try:

            if choice == "1":
                    try:
                        title = input("Title: ").strip() 
                    except ValueError:
                        print("Title cannot be empty")
                    try:
                        author = input("Author: ").strip()
                    except ValueError:
                        print("Author cannot be empty")
                    try:
                        isbn = input("ISBN: ").strip()
                    except ValueError:
                        print("ISBN cannot be empty")
                    library.add_book(Book(title, author, isbn))

            elif choice == "2":
                isbn = input("ISBN to remove: ").strip()
                library.remove_book(isbn)

            elif choice == "3":
                name = input("Member name: ").strip()
                member_id = input("Member ID: ").strip()
                library.add_member(Member(name, member_id))

            elif choice == "4":
                name = input("Member name: ").strip()
                member_id = input("Member ID: ").strip()
                library.remove_member(Member(name, member_id))

            elif choice == "5":
                keyword = input("Search keyword: ").strip()
                results = library.search_books(keyword)
                for book in results:
                    print("-", book)

            elif choice == "6":
                for book in library.list_books():
                    print("-", book)

            elif choice == "7":
                library.available_books

            elif choice == "8":
                member_id = input("Member ID: ").strip()
                isbn = input("ISBN: ").strip()
                library.borrow_book(member_id, isbn)

            elif choice == "9":
                member_id = input("Member ID: ").strip()
                isbn = input("ISBN: ").strip()
                library.return_book(member_id, isbn)

            elif choice == "10":
                member_id = input("Member ID: ").strip()
                library.list_borrowed_books(member_id)

            elif choice == "11":
                library.most_borrowed_book

            elif choice == "12":
                save_library(library, DATA_FILE)
                print("Library saved.")

            elif choice == "13":
                save_library(library, DATA_FILE)
                print("Goodbye!")
                break

            else:
                print ("Invalid Options please select from 1 to 13")


        except (
            BookNotFoundError,
            MemberNotFoundError,
            BookNotAvailableError,
            DuplicateEntryError,

        ) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
