class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author}[{status}]"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed!")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
            return
        
        print(f"\n--- Borrowed Books by {self.name} ---")
        for book in self.borrowed_books:
            print(book)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"New member: {member.name}")

    def show_all_books(self):
        print(f"\n--- {self.name} - All Books ---")
        for book in self.books:
            print(book)
        print("-----------------------------\n")


my_library = Library("SLIIT Library")
book1 = Book("python Basics", "John Smith", "12345")
book2 = Book("OOP in Python", "Jane Doe", "67890")
book3 = Book("Data Structure", "Alan Turing", "11123")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

member1 = Member("Suresh", "M001")
my_library.add_member(member1)

my_library.show_all_books()
member1.borrow_book(book1)
my_library.show_all_books()
member1.return_book(book1)
my_library.show_all_books()