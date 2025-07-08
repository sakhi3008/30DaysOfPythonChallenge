# 🗓️ Day 25 – Validating Data with Pydantic

Today’s challenge focused on building data models using **Pydantic**, a powerful library for **data validation and settings management** using Python type hints.

---

## 🔹 Topics Covered

### 🔸 What is Pydantic?

**Pydantic** is a data validation library that uses Python's type annotations to enforce data types and validate input data automatically. It's widely used with **FastAPI**, config files, and more.

### 🔸 Why Use Pydantic?

* Ensures input data is valid and clean
* Helps catch bugs early
* Makes your code more robust and readable
* Supports nested models and complex data types

---

## 🔸 Defining a Pydantic Model

A model is defined by subclassing `BaseModel` and using type hints for fields.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Once defined, you can create instances with automatic validation:

```python
user = User(name="Sakhi", age=24)
```

---

## 🔸 Built-in Data Types

Pydantic supports many Python types, including:

* `str`, `int`, `float`, `bool`
* `EmailStr`, `HttpUrl`, `conint`, `constr` (from `pydantic` validators)
* `List`, `Dict`, `Optional`, `datetime`, and nested models

### 🔸 Email Validation

Use `EmailStr` to validate email format:

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
```

---

## 🔸 Field Validation using `@validator`

You can define custom validation logic using `@validator` decorators:

```python
from pydantic import validator

class User(BaseModel):
    age: int

    @validator('age')
    def check_age(cls, value):
        if not 18 <= value <= 100:
            raise ValueError("Age must be between 18 and 100")
        return value
```

---

## 🔸 Displaying Data

You can define custom methods (like `display()`) in your model to format or print data as needed.

```python
    def display(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"
```

---

## 🌟 Additional Features of Pydantic

* `Config` class for setting global model behavior (e.g., `orm_mode`, `allow_mutation=False`)
* Automatic data conversion (e.g., str to int if possible)
* Nested Models: Pydantic models can be used inside other models
* JSON export with `.json()`

---

## 🎯 Challenge – User Profile Validator

### 🔫 Task:

Create a Pydantic model for a **user profile** with the following fields:

* `name` (string)
* `email` (must be a valid Gmail)
* `age` (must be between 18 and 100)

### 📓 What I Did:

* Defined a model `UserProfile` using `BaseModel`
* Used `EmailStr` for automatic email format checking
* Used `@validator` to ensure age is in the valid range
* Added a method `.display()` to return a formatted string

### 🧠 Key Learnings:

* Pydantic simplifies data validation with minimal code
* Email and numerical range validation can be enforced easily
* Custom validators add flexibility
* Useful for APIs, config parsing, and reliable input handling

---

Pydantic turns raw input into clean, validated objects—a game-changer for modern Python development.
