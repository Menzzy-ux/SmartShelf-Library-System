# demo.py
from operations import LibrarySystem

library = LibrarySystem()

print("=== SmartShelf Library System Demo ===")

# Add books
print(library.add_book("101", "The Lost Island", "Jules Verne", "Adventure", 4))
print(library.add_book("102", "Love Beyond Time", "A. Green", "Romance", 3))

# Add members
print(library.add_member("M001", "Mary Brown", "mary@gmail.com"))
print(library.add_member("M002", "James Smith", "james@gmail.com"))

# Search
results = library.search_books("love")
for b in results:
    print(f"Found: {b.title} by {b.author}")

# Borrow & return
print(library.borrow_book("M001", "101"))
print(library.borrow_book("M001", "102"))
print(library.return_book("M001", "102"))

# Update & delete
print(library.update_book("101", title="The Hidden Island"))
print(library.delete_book("102"))
print(library.delete_member("M002"))
