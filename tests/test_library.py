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

if __name__ == "__main__":
    unittest.main()
