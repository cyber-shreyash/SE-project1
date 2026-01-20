from src.library import Library, DuplicateBookIDError, BookNotFoundError, BookAlreadyBorrowedError, BookNotBorrowedError

def main():
    library = Library()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Enter choices (1-5): ").strip()
        
        try:
            if choice == "1":
                b_id = input("Enter Book ID: ").strip()
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                library.add_book(b_id, title, author)
                print(f"Book '{title}' added successfully!")
                
            elif choice == "2":
                b_id = input("Enter Book ID to borrow: ").strip()
                library.borrow_book(b_id)
                print(f"Book {b_id} borrowed successfully!")
                
            elif choice == "3":
                b_id = input("Enter Book ID to return: ").strip()
                library.return_book(b_id)
                print(f"Book {b_id} returned successfully!")
                
            elif choice == "4":
                print("\n--- Library Report ---")
                print(library.generate_report())
                
            elif choice == "5":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except (DuplicateBookIDError, BookNotFoundError, BookAlreadyBorrowedError, BookNotBorrowedError, ValueError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
