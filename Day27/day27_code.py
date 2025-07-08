# Challenge - Use SQLAlchemy in the book management APIs from the previous challenge and store the data in a SQLite database

# Import libraries
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()

# SQLAlchemy book model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

# Create the table
Base.metadata.create_all(bind = engine)   

# Pydantic model (Data Validation and Schemas)
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True

# FastAPI initialisation
app = FastAPI()


# Welcome route
@app.get("/")
def welcome():
    return {"message":  "Welcome to the Library API"}

# Create book endpoint(POST)
@app.post("/books/", response_model = BookResponse)
def create_book(book: BookCreate):
    db = SessionLocal()
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()
    return new_book

# Read all books (GET)
@app.get("/books/", response_model = List[BookResponse])
def get_books():
    db = SessionLocal()
    books = db.query(Book).all()
    db.close()
    return books

# Update book (PUT)
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookCreate):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book_data.dict().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    db.close()
    return book

# Delete book (DELETE)
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    db.close()
    return {"message": "Book deleted successfully"}

# View books (GET)
@app.get("/debug-view-books/")
def view_books():
    import sqlite3
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return {"data": rows}

