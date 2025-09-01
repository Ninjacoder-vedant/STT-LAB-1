"""Basic Library Management System (LMS).
This script allows adding, displaying, borrowing, and returning books.
"""

class Library:
    """A simple Library class to manage books."""

    def __init__(self):
        """Initialize the library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f'"{book}" added to library')

    def display_books(self):
        """Display all books currently in the library."""
        if not self.books:
            print("No books in library")
        else:
            print("Books in library:")
            for b in self.books:
                print("-", b)

    def borrow_book(self, book):
        """Borrow a book if available."""
        if book in self.books:
            self.books.remove(book)
            print(f'You borrowed "{book}"')
        else:
            print(f'Sorry, "{book}" is not available')

    def return_book(self, book):
        """Return a borrowed book to the library."""
        self.books.append(book)
        print(f'You returned "{book}"')

# -------- Main Program --------
lib = Library()
lib.add_book("Python Programming")
lib.add_book("Data Structures")
lib.add_book("Machine Learning")

lib.display_books()
lib.borrow_book("Python Programming")
lib.display_books()
lib.return_book("Python Programming")
lib.display_books()
