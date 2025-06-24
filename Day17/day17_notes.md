# 🗓️ Day 17 – `with` Statement and Custom Context Managers

Today’s challenge focused on **context managers**, a very elegant way to manage resources in Python — especially for tasks like file handling, where cleanup is crucial.

---

## 🔹 What is a Context Manager?

A **context manager** is an object that defines runtime behavior to be used in a `with` statement. It’s used to **set up and tear down resources automatically** (like opening and closing files, database connections, etc.).

The `with` block ensures that resources are **automatically cleaned up**, even if errors occur.

---

## 🔹 Built-in `with` Statement

The `with` keyword is used with objects that support context management, like file objects.

### 🔸 Example:
```python
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed after the block
```
---
## 🔹 Under the Hood: __enter__ and __exit__
To create your own context manager, you define a class with:

__enter__() → what happens when entering the with block

__exit__() → what happens when exiting the block (handles closing, cleanup, and error control)

### 🔸 Example:
```python
class MyManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return True  # suppresses exceptions
```
---

## 🔹 Why Use Context Managers?

- Ensures proper cleanup of resources

- Improves code readability

- Reduces chances of bugs and memory leaks

- Used widely in file I/O, networking, threading, database connections, etc.

---

## 🎯 Challenge – Build a Context Manager for Safe File Handling
In this challenge, I:

- Created a custom class FileManager with __enter__ and __exit__ methods

- Ensured the file is opened when entering the with block and automatically closed afterward

- Handled potential exceptions gracefully using the __exit__ method

- Tested the context manager with both writing and reading a text file

This challenge helped me truly understand what happens behind the scenes of the with statement and how to build powerful, reusable resource managers in Python.

