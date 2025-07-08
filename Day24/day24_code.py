# Challenge - -  Create a dataclass to represent a library book with fields for title, author, ISBN, and publication year, including a method to display book details

from dataclasses import dataclass

@dataclass
class LibraryBook:
    title: str
    author: str
    isbn: str
    publication_year: int

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Published: {self.publication_year}")

# Example usage:
book = LibraryBook("Atomic Habits", "James Clear", "9780735211292", 2018)
book.display()
