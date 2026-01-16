# src/library.py

class DuplicateBookIDError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class BookAlreadyBorrowedError(Exception):
    pass


class BookNotBorrowedError(Exception):
    pass


class Library:
    """
    In-memory Library Book Management System.
    Data structure: dictionary {book_id: {title, author, borrowed}}
    """

    def __init__(self):
        self.books = {}  # {book_id: {"title": str, "author": str, "borrowed": bool}}

    # ------------------ Sprint 1 ------------------
    def add_book(self, book_id: str, title: str, author: str):
        if book_id in self.books:
            raise DuplicateBookIDError(f"Book ID {book_id} already exists")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }
