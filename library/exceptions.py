class BookNotFoundError(Exception):
    """Raised when a requested book does not exist."""


class MemberNotFoundError(Exception):
    """Raised when a requested member does not exist."""


class BookNotAvailableError(Exception):
    """Raised when a book cannot be borrowed or returned."""


class DuplicateEntryError(Exception):
    """Raised when adding a duplicate book or member."""



