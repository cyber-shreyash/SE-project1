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

    # ------------------ Sprint 2 ------------------
    def borrow_book(self, book_id: str):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")

        if self.books[book_id]["borrowed"]:
            raise BookAlreadyBorrowedError(f"Book ID {book_id} is already borrowed")

        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id: str):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")

        if not self.books[book_id]["borrowed"]:
            raise BookNotBorrowedError(f"Book ID {book_id} is not borrowed")

        self.books[book_id]["borrowed"] = False

    # ------------------ Sprint 3 ------------------
    def generate_report(self) -> str:
        header = "Book ID | Title | Author | Status"
        lines = [header]

        for book_id, info in self.books.items():
            status = "Borrowed" if info["borrowed"] else "Available"
            lines.append(f"{book_id} | {info['title']} | {info['author']} | {status}")

        return "\n".join(lines)
