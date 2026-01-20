# User Stories

## Sprint 1: Add Books
**User Story:** As a librarian, I want to add new books to the system so that they can be tracked.
**Acceptance Criteria:**
- Successfully add a book with unique ID, title, and author.
- Raise `DuplicateBookIDError` if ID already exists.
- Default status is "Available".

## Sprint 2: Borrow and Return Books
**User Story:** As a library member, I want to borrow and return books so that the library can track availability.
**Acceptance Criteria:**
- `borrow_book(id)` sets status to "Borrowed".
- Raise `BookNotFoundError` if ID doesn't exist.
- Raise `BookAlreadyBorrowedError` if already borrowed.
- `return_book(id)` sets status to "Available".
- Raise `BookNotBorrowedError` if book was not borrowed.

## Sprint 3: Reporting
**User Story:** As a librarian, I want to generate a report of all books so that I can see the entire inventory at once.
**Acceptance Criteria:**
- Output string with header: `BookID | Title | Author | Status`.
- Each book on a new line.
- Sorted by `BookID`.
- Status shows "Available" or "Borrowed".
