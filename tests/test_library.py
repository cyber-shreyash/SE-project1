# tests/test_library.py

import unittest
from src.library import (
    Library,
    DuplicateBookIDError,
    BookAlreadyBorrowedError
)

class TestLibrarySprint1(unittest.TestCase):
    def test_successful_book_addition(self):
        lib = Library()
        lib.add_book("B1", "Python Basics", "Guido")

        self.assertIn("B1", lib.books)
        self.assertEqual(lib.books["B1"]["title"], "Python Basics")
        self.assertEqual(lib.books["B1"]["author"], "Guido")
        self.assertFalse(lib.books["B1"]["borrowed"])

    def test_duplicate_book_addition_raises_error(self):
        lib = Library()
        lib.add_book("B1", "Python Basics", "Guido")
        with self.assertRaises(DuplicateBookIDError):
            lib.add_book("B1", "DSA", "Someone")


class TestLibrarySprint2(unittest.TestCase):
    def test_borrowing_available_book(self):
        lib = Library()
        lib.add_book("B2", "C++", "Bjarne")
        lib.borrow_book("B2")

        self.assertTrue(lib.books["B2"]["borrowed"])

    def test_borrowing_unavailable_book_raises_error(self):
        lib = Library()
        lib.add_book("B3", "Java", "James")
        lib.borrow_book("B3")

        with self.assertRaises(BookAlreadyBorrowedError):
            lib.borrow_book("B3")

    def test_returning_book_updates_status_correctly(self):
        lib = Library()
        lib.add_book("B4", "OS", "Silberschatz")
        lib.borrow_book("B4")
        lib.return_book("B4")

        self.assertFalse(lib.books["B4"]["borrowed"])

if __name__ == "__main__":
    unittest.main()
