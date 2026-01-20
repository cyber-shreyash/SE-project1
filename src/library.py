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
        """Initialize the library with an empty set of books."""
        self.books = {}  # {book_id: {"title": str, "author": str, "borrowed": bool}}

    # ------------------ Sprint 1 ------------------
    def add_book(self, book_id: str, title: str, author: str):
        """
        Adds a new book to the library inventory.
        
        Args:
            book_id (str): Unique identifier for the book.
            title (str): The book's title.
            author (str): The book's author.
            
        Raises:
            ValueError: If any identifier is empty or whitespace.
            DuplicateBookIDError: If the book_ID already exists in inventory.
        """
        if not all(field.strip() for field in [book_id, title, author]):
            raise ValueError("All fields (ID, title, author) are required and cannot be empty.")

        if book_id in self.books:
            raise DuplicateBookIDError(f"Book ID {book_id} already exists")

        self.books[book_id] = {
            "title": title.strip(),
            "author": author.strip(),
            "borrowed": False
        }

    # ------------------ Sprint 2 ------------------
    def borrow_book(self, book_id: str):
        """
        Marks a book as borrowed.
        
        Args:
            book_id (str): The identifier of the book to borrow.
            
        Raises:
            BookNotFoundError: If the book does not exist.
            BookAlreadyBorrowedError: If the book is already out on loan.
        """
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")

        if self.books[book_id]["borrowed"]:
            raise BookAlreadyBorrowedError(f"Book ID {book_id} is already borrowed")

        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id: str):
        """
        Marks a borrowed book as returned.
        
        Args:
            book_id (str): The identifier of the book to return.
            
        Raises:
            BookNotFoundError: If the book does not exist.
            BookNotBorrowedError: If the book was not currently borrowed.
        """
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")

        if not self.books[book_id]["borrowed"]:
            raise BookNotBorrowedError(f"Book ID {book_id} was not borrowed")

        self.books[book_id]["borrowed"] = False

    # ------------------ Sprint 3 ------------------
    def generate_report(self) -> str:
        """
        Generates a summary report of all books in the library.
        
        Returns:
            str: A formatted string containing the inventory summary.
        """
        header = "BookID | Title | Author | Status"
        lines = [header]

        # Sort by book_id for deterministic output
        sorted_ids = sorted(self.books.keys())

        for b_id in sorted_ids:
            book = self.books[b_id]
            status = "Borrowed" if book["borrowed"] else "Available"
            line = f"{b_id} | {book['title']} | {book['author']} | {status}"
            lines.append(line)

        return "\n".join(lines)
