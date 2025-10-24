# tests.py
from operations import LibrarySystem

lib = LibrarySystem()
lib.add_book("1001", "World Wars", "J. Clarke", "History", 2)
lib.add_member("001", "John Doe", "john@gmail.com")

# Tests
assert lib.add_book("1001", "Another", "X", "History", 1) == "ISBN already exists."
assert lib.borrow_book("001", "1001") == "Book borrowed successfully."
assert lib.borrow_book("001", "1001") == "No copies available."
assert lib.return_book("001", "1001") == "Book returned successfully."
assert lib.update_member("001", name="Johnny Doe") == "Member updated successfully."

print("✅ All tests passed!")
