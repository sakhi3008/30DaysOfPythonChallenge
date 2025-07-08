# 🗓️ Day 24 – Dataclasses in Python

In today’s challenge, I explored the power and simplicity of **dataclasses** in Python. Dataclasses reduce boilerplate code and make it easier to represent structured data with minimal code.

---

## 🔹 Topics Covered

### 🔸 What is a Dataclass?

A **dataclass** is a Python class specifically designed to store data. Introduced in Python 3.7 via the `dataclasses` module, it automatically generates special methods like `__init__`, `__repr__`, `__eq__`, etc.

### ✅ Why Use Dataclasses?

* Simplifies class creation
* Automatically generates constructors and other methods
* Built-in support for type annotations

To use a dataclass, simply use the `@dataclass` decorator above a class definition.

---

### 🔸 Type Hints in Dataclasses

**Type hints** are used to indicate what kind of value each attribute should hold. They make the code more readable and are especially useful in larger projects or when using static type checkers.

#### Example:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    pages: int
```

Here, `title` is expected to be a `str`, and `pages` an `int`.

---

### 🔸 Default Values in Dataclasses

You can assign **default values** to fields in a dataclass just like in regular Python classes. These defaults are used if no value is provided during instantiation.

#### Example:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str = "Untitled"
    author: str = "Unknown"
    pages: int = 0
```

This allows flexible object creation:

```python
book = Book()  # Uses all default values
```

---

### 🔸 More Features of Dataclasses

#### 🔹 `field()` Function:

Use `field()` to customize the behavior of individual fields.

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    options: list = field(default_factory=list)
```

Here, `default_factory` ensures a new list is created for each instance.

#### 🔹 `frozen=True`:

Make the dataclass immutable.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

You cannot modify the attributes after object creation.

#### 🔹 `init=False`:

Exclude a field from the generated `__init__()` method.

```python
@dataclass
class Counter:
    count: int = 0
    status: str = field(init=False, default="idle")
```

#### 🔹 `repr=False`, `compare=False`:

Prevent fields from appearing in `__repr__()` or being used in comparisons.

```python
@dataclass
class Secret:
    public_info: str
    secret_info: str = field(repr=False, compare=False)
```

---

## 🎯 Challenge – LibraryBook Dataclass

### Problem Statement:

Create a dataclass to represent a **library book** with fields for:

* `title`
* `author`
* `isbn`
* `publication_year`

Also, include a method to display the book details.

### 👨‍💻 What I Built:

* Defined a `LibraryBook` dataclass with the required fields
* Used type hints for all attributes
* Added a method `.display()` to print book details in a user-friendly way

### 🧠 What I Learned:

* How to define and use dataclasses in Python
* The importance of type hints and default values
* How to enhance a simple class with built-in functionality using `@dataclass`
* Useful features like `frozen`, `default_factory`, and field customization with `field()`

Dataclasses are perfect when working with structured data like configurations, records, or any object that mainly stores attributes.

---
