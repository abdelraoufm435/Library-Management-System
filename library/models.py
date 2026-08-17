class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrow_count = 0

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f'"{self.title}" by {self.author} (ISBN: {self.isbn}) — {status}'


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_isbns = []

    def __str__(self):
        return (
            f"{self.name} (ID: {self.member_id}) — "
            f"{len(self.borrowed_isbns)} book(s) borrowed"
        )
