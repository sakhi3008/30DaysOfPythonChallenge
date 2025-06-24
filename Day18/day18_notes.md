# 🧠 Understanding Python Metaclasses – A Beginner-Friendly Guide

---

## 🔹 What is a Metaclass?

In Python, **everything is an object** — even classes. Just like objects are created from classes, **classes themselves are created by metaclasses**.

> Simply put:  
> - Objects are instances of classes  
> - Classes are instances of metaclasses  

The **default metaclass in Python is `type`**. So when you write:

```python
class MyClass:
    pass
```
Behind the scenes, Python is actually doing something like this:
```python
MyClass = type('MyClass', (), {})
```
This means that `type` creates the class `MyClass`, just like `MyClass()` would create an instance of `MyClass`.
---

## 🔹 Why Use a Metaclass?
Metaclasses give you control over how classes are created, not how they behave (that’s what methods and inheritance are for).

You use metaclasses when you want to:

- Enforce coding standards (e.g., all class names must be uppercase)

- Add or modify attributes or methods automatically to a class

- Track or register classes (like plugins)

- Perform custom validation during class creation

## 🔹 They are most useful in:

- Frameworks (like Django, SQLAlchemy)

- APIs

- Large codebases with strict structure

---
## 🔹 Creating a Metaclass – Step-by-Step
✅ Step 1: Subclass `type`

```python
class MyMeta(type):
    def __new__(cls, name, bases, class_dict):
        # Custom logic before class is created
        return super().__new__(cls, name, bases, class_dict)
```
🔹 `cls`: the metaclass itself

🔹 `name`: name of the class being created

🔹 `bases`: parent classes (tuple)

🔹 `class_dict`: attributes/methods defined in the class

✅ Step 2: Use the metaclass in a class

```python
class MyClass(metaclass=MyMeta):
    pass
```
---
## 🔹 Metaclass vs Class vs Object — Summary
| Term      | Creates | Is Instance of |
| --------- | ------- | -------------- |
| Object    | Nothing | Class          |
| Class     | Object  | Metaclass      |
| Metaclass | Class   | type           |

---

## 🎯 Challenge – Enforce a Naming Convention

Goal: Ensure that all class names start with an uppercase letter.

What I did:

Created a metaclass `NamingConventionMeta`

Used `__new__()` to check if the class name starts with a capital letter

Raised a `ValueError` if the rule was broken

Successfully created a class `MyClass` that follows the rule.

✅ This challenge helped me understand how Python lets us control class creation and how metaclasses can enforce standards automatically — a powerful concept for advanced Python projects.
