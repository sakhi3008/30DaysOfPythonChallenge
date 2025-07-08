# Challenge - Develop a FastAPI application with endpoints to manage a library of books, including creating, reading, updating, and deleting books

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Book model
class Book(BaseModel):
    title: str
    author: str
    year: int

# In-memory database
books = []

# Welcome route
@app.get("/")
def welcome():
    return {"message":  "Welcome to the Library API"}

# Add a book
@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added!", "book": book}

# Get all books
@app.get("/books")
def get_books():
    return books

# Update a book
@app.put("/books/{index}")
def update_book(index: int, book: Book):
    if index < len(books):
        books[index] = book
        return {"message": "Book updated!", "book": book}
    return {"error": "Book not found"}

# Delete a book
@app.delete("/books/{index}")
def delete_book(index: int):
    if index < len(books):
        removed = books.pop(index)
        return {"message": "Book deleted", "book": removed}
    return {"error": "Book not found"}

