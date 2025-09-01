class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added to library')

    def display_books(self):
        if not self.books:
            print("No books in library")
        else:
            print("Books in library:")
            for b in self.books:
                print("-", b)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You borrowed "{book}"')
        else:
            print(f'Sorry, "{book}" is not available')

    def return_book(self, book):
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