import json

from .models import Book, Member


def save_library(library, path):
    data = {
        "books": [
            {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "is_borrowed": book.is_borrowed,
                "borrow_count": book.borrow_count,
            }
            for book in library.books
        ],
        "members": [
            {
                "name": member.name,
                "member_id": member.member_id,
                "borrowed_isbns": member.borrowed_isbns,
            }
            for member in library.members
        ],
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_library(library, path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return

    library.books = []
    for record in data.get("books", []):
        book = Book(
            record["title"],
            record["author"],
            record["isbn"],
            record["borrow_count"],
        )
        book.is_borrowed = record.get("is_borrowed", False)
        library.books.append(book)

    library.members = []
    for record in data.get("members", []):
        member = Member(
            record["name"],
            record["member_id"],
        )
        member.borrowed_isbns = record.get("borrowed_isbns", [])
        library.members.append(member)
