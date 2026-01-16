# TRACEABILITY MATRIX

Traceability connects requirements (user stories) → code → unit tests → releases(tags).

| User Story ID | Requirement / Feature | Code Location | Test Case(s) | Sprint | Release Tag |
|-------------|------------------------|--------------|--------------|--------|-------------|
| US1 | Add new book (ID, title, author) | src/library.py : Library.add_book() | test_successful_book_addition | 1 | v0.1 |
| US2 | Reject duplicate book ID | src/library.py : Library.add_book() | test_duplicate_book_addition_raises_error | 1 | v0.1 |
| US3 | Borrow a book | src/library.py : Library.borrow_book() | test_borrowing_available_book | 2 | v0.2 |
| US5 | Prevent borrowing borrowed book | src/library.py : Library.borrow_book() | test_borrowing_unavailable_book_raises_error | 2 | v0.2 |
| US4 | Return a book | src/library.py : Library.return_book() | test_returning_book_updates_status_correctly | 2 | v0.2 |
| US6 | Generate library report | src/library.py : Library.generate_report() | test_report_contains_header, test_report_contains_at_least_one_book_entry | 3 | v0.3 |
