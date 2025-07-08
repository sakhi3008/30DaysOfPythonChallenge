# 🗓️ Day 27 – SQLAlchemy with FastAPI (ORM + SQLite Integration)

Today’s challenge was all about learning how to use an **ORM (Object Relational Mapper)** with **FastAPI**, and more specifically, how to integrate **SQLAlchemy** to store and manage data using a **SQLite database**.

---

## 🔹 Topics Covered

### 🔸 What is an ORM?

An **ORM (Object Relational Mapper)** is a tool that lets you interact with a database using Python classes and objects instead of writing raw SQL queries.

### 🔸 Why SQLAlchemy?

SQLAlchemy is a powerful and popular ORM in Python that:

* Maps Python classes to database tables
* Provides tools to query, insert, update, and delete records
* Supports multiple databases like SQLite, PostgreSQL, MySQL, etc.

### 🔸 Key SQLAlchemy Concepts:

✅ **Engine** – Connects to the database

```python
engine = create_engine("sqlite:///./books.db")
```

✅ **Session** – Handles all interactions with the DB

```python
SessionLocal = sessionmaker(bind=engine)
```

✅ **Base** – Used to declare models (tables)

```python
Base = declarative_base()
```

✅ **Model (Table)** – Represents a table as a Python class

```python
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
```

✅ **Creating Tables**

```python
Base.metadata.create_all(bind=engine)
```

✅ **CRUD Operations**

* **Create:** `db.add()` + `db.commit()`
* **Read:** `db.query().all()` or `.filter()`
* **Update:** Use `setattr()`
* **Delete:** `db.delete()`

---

## 🎯 Challenge – Book Management API with SQLite DB

### ✅ What I Built:

* Defined a SQLAlchemy model for `Book`
* Used a SQLite database to store book data
* Created a FastAPI app with CRUD endpoints:

  * `GET /books/` to read all books
  * `POST /books/` to create a new book
  * `PUT /books/{id}` to update a book
  * `DELETE /books/{id}` to delete a book
* Added a `/debug-view-books/` endpoint to inspect all records directly from the database

---

## 🚀 How to Run This Project

1. **Run the FastAPI App:**

```bash
uvicorn main:app --reload
```

2. **Open the Swagger UI:**
   Visit `http://127.0.0.1:8000/docs` in browser.

3. **Interact with the API** using available endpoints:

* `GET /books/`
* `POST /books/`
* `PUT /books/{book_id}`
* `DELETE /books/{book_id}`

---

## 🧠 Key Takeaways

* ORMs make it easy to interact with databases using Python objects
* SQLAlchemy supports advanced features like joins, filters, and transactions
* FastAPI + Pydantic + SQLAlchemy = powerful combo for building modern APIs
* SQLite is great for lightweight local storage

---
