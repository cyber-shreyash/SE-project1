# tests/test_library.py

import unittest
from src.library import (
    Library,
    DuplicateBookIDError,
    BookNotFoundError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError
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

    def test_add_book_empty_fields_raises_error(self):
        lib = Library()
        with self.assertRaises(ValueError):
            lib.add_book("", "Title", "Author")
        with self.assertRaises(ValueError):
            lib.add_book("ID", "  ", "Author")
        with self.assertRaises(ValueError):
            lib.add_book("ID", "Title", "")

class TestLibrarySprint2(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B1", "Python Basics", "Guido")

    def test_borrow_book_success(self):
        self.lib.borrow_book("B1")
        self.assertTrue(self.lib.books["B1"]["borrowed"])

    def test_borrow_book_not_found(self):
        with self.assertRaises(BookNotFoundError):
            self.lib.borrow_book("B99")

    def test_borrow_already_borrowed(self):
        self.lib.borrow_book("B1")
        with self.assertRaises(BookAlreadyBorrowedError):
            self.lib.borrow_book("B1")

    def test_return_book_success(self):
        self.lib.borrow_book("B1")
        self.lib.return_book("B1")
        self.assertFalse(self.lib.books["B1"]["borrowed"])

    def test_return_book_not_found(self):
        with self.assertRaises(BookNotFoundError):
            self.lib.return_book("B99")

    def test_return_book_not_borrowed(self):
        with self.assertRaises(BookNotBorrowedError):
            self.lib.return_book("B1")

class TestLibrarySprint3(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B2", "Advanced Python", "Raymond")
        self.lib.add_book("B1", "Python Basics", "Guido")

    def test_generate_report_header(self):
        report = self.lib.generate_report()
        header = "BookID | Title | Author | Status"
        self.assertTrue(report.startswith(header))

    def test_generate_report_content_and_sorting(self):
        self.lib.borrow_book("B1")
        report = self.lib.generate_report()
        lines = report.split("\n")
        
        # Check sorting: B1 should come before B2
        self.assertIn("B1 | Python Basics | Guido | Borrowed", lines[1])
        self.assertIn("B2 | Advanced Python | Raymond | Available", lines[2])

if __name__ == "__main__":
    unittest.main()
