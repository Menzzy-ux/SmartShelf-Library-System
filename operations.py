# operations.py
from typing import List, Dict, Tuple

GENRES: Tuple[str, ...] = ("Adventure", "Romance", "History", "Fantasy")

class Book:
    def __init__(self, isbn: str, title: str, author: str, genre: str, total_copies: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies

class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books: List[str] = []

class LibrarySystem:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}

    # ---------------- Add ----------------
    def add_book(self, isbn, title, author, genre, total_copies):
        if isbn in self.books:
            return "ISBN already exists."
        if genre not in GENRES:
            return "Invalid genre."
        self.books[isbn] = Book(isbn, title, author, genre, total_copies)
        return "Book added successfully."

    def add_member(self, member_id, name, email):
        if member_id in self.members:
            return "Member already exists."
        self.members[member_id] = Member(member_id, name, email)
        return "Member added successfully."

    # ---------------- Search ----------------
    def search_books(self, keyword):
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    # ---------------- Update ----------------
    def update_book(self, isbn, title=None, author=None, genre=None, total_copies=None):
        if isbn not in self.books:
            return "Book not found."
        book = self.books[isbn]
        if title: book.title = title
        if author: book.author = author
        if genre and genre in GENRES: book.genre = genre
        if total_copies:
            diff = total_copies - book.total_copies
            book.total_copies = total_copies
            book.available_copies += diff
        return "Book updated successfully."

    def update_member(self, member_id, name=None, email=None):
        if member_id not in self.members:
            return "Member not found."
        member = self.members[member_id]
        if name: member.name = name
        if email: member.email = email
        return "Member updated successfully."

    # ---------------- Delete ----------------
    def delete_book(self, isbn):
        if isbn not in self.books:
            return "Book not found."
        for m in self.members.values():
            if isbn in m.borrowed_books:
                return "Cannot delete; book currently borrowed."
        del self.books[isbn]
        return "Book deleted successfully."

    def delete_member(self, member_id):
        if member_id not in self.members:
            return "Member not found."
        if self.members[member_id].borrowed_books:
            return "Member has borrowed books; cannot delete."
        del self.members[member_id]
        return "Member deleted successfully."

    # ---------------- Borrow/Return ----------------
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not found."
        if isbn not in self.books:
            return "Book not found."
        member = self.members[member_id]
        book = self.books[isbn]
        if len(member.borrowed_books) >= 2:
            return "Borrow limit reached (max 2)."
        if book.available_copies <= 0:
            return "No copies available."
        member.borrowed_books.append(isbn)
        book.available_copies -= 1
        return "Book borrowed successfully."

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not found."
        member = self.members[member_id]
        if isbn not in member.borrowed_books:
            return "This book was not borrowed."
        member.borrowed_books.remove(isbn)
        self.books[isbn].available_copies += 1
        return "Book returned successfully."
