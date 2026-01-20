# Traceability Matrix

| User Story | Feature | Method | Unit Test |
|------------|---------|--------|-----------|
| Sprint 1 | Add Book | `add_book` | `test_successful_book_addition` |
| Sprint 1 | Duplicate ID | `add_book` | `test_duplicate_book_addition_raises_error` |
| Sprint 2 | Borrow Book | `borrow_book` | `test_borrow_book_success` |
| Sprint 2 | Borrow Not Found | `borrow_book` | `test_borrow_book_not_found` |
| Sprint 2 | Borrow Already Borrowed | `borrow_book` | `test_borrow_already_borrowed` |
| Sprint 2 | Return Book | `return_book` | `test_return_book_success` |
| Sprint 2 | Return Not Found | `return_book` | `test_return_book_not_found` |
| Sprint 2 | Return Not Borrowed | `return_book` | `test_return_book_not_borrowed` |
| Sprint 3 | Report Header | `generate_report` | `test_generate_report_header` |
| Sprint 3 | Report Order/Content | `generate_report` | `test_generate_report_content_and_sorting` |
