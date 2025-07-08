# 🗓️ Day 26 – Intro to APIs with FastAPI

Today’s challenge introduced me to **building RESTful APIs using FastAPI**, one of the fastest modern frameworks for web development in Python. I built a simple book library API where users can add, view, update, and delete books.

---

## 🔹 Topics Covered

### 🔹 What is an API?

An **API (Application Programming Interface)** allows software applications to communicate with each other. In web development, **REST APIs** expose endpoints that allow data exchange using HTTP methods like GET, POST, PUT, and DELETE.

### 🔹 What is FastAPI?

**FastAPI** is a high-performance Python web framework for building APIs with automatic data validation and documentation (using Swagger UI). It is built on top of Starlette and Pydantic.

#### ✅ Key Benefits:

* Fast to run and write
* Built-in data validation with Pydantic
* Interactive API documentation at `/docs`
* Easy to learn and use

---

## 🔹 HTTP Methods Used in REST APIs

| Method | Purpose              | Example Description |
| ------ | -------------------- | ------------------- |
| GET    | Read/Retrieve data   | Fetch all books     |
| POST   | Create new data      | Add a new book      |
| PUT    | Update existing data | Edit book info      |
| DELETE | Remove existing data | Delete a book       |

---

## 🔹 FastAPI App Structure

1. **Import FastAPI & Pydantic**: FastAPI for creating routes, Pydantic for data validation.
2. **Create an App**: `app = FastAPI()`
3. **Define a Model**: Use `BaseModel` to define the schema (e.g., title, author, year).
4. **Create Endpoints**:

   * `@app.get()` for reading data
   * `@app.post()` for creating data
   * `@app.put()` for updating
   * `@app.delete()` for deleting

---

## 🔹 Routes I Created

* `GET /` — Welcome message
* `POST /books` — Add a new book (takes `title`, `author`, `year`)
* `GET /books` — Get the full list of books
* `PUT /books/{index}` — Update book by index
* `DELETE /books/{index}` — Delete book by index

Each route works with an in-memory list (`books[]`), simulating a database.

---

## 🏠 Book Model with Pydantic

```python
class Book(BaseModel):
    title: str
    author: str
    year: int
```

Pydantic automatically:

* Validates input types
* Returns clear error messages if types don’t match

---

## 🔹 Interactive API Docs

FastAPI provides an auto-generated Swagger UI at:

```
http://localhost:8000/docs
``` 

You can test all routes directly from the browser, without Postman or writing extra frontend code.

---

## 🎓 What I Learned

* How to define and test API endpoints using FastAPI
* Difference between HTTP methods like GET/POST/PUT/DELETE
* How to use Pydantic models to ensure clean and valid input
* Built a functional and tested API with only a few lines of code

---

## 📅 Challenge Summary

**🎯 Challenge**: Build a FastAPI application with endpoints to manage a library of books.

**📆 What I Built**:

* A RESTful API with FastAPI
* Used endpoints to perform CRUD operations on a book collection
* Validated data using Pydantic
* Ran and tested it using Swagger UI

---

FastAPI is incredibly powerful for backend developers. It makes creating production-ready APIs a breeze and integrates cleanly with frontend apps or other services!
