"""Task 4: Track borrowing popularity.

Changes:
1. Add self.borrow_count = 0 to Book.__init__ in library/models.py.
2. Increment book.borrow_count in Library.borrow_book().
3. Add Library.most_borrowed_book().
4. Use max(..., key=lambda book: book.borrow_count).
5. Update storage so borrow_count is saved and loaded.
"""
# done