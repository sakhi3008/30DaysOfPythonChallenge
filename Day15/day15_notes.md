# 🗓️ Day 15 – Function Decorators and Execution Time Challenge

In today’s challenge, I explored **function decorators** — a powerful and elegant feature in Python that allows you to **modify the behavior of a function without changing its actual code**. They're widely used in logging, authentication, performance measurement, and more.

---

## 🔹 What is a Decorator?

A **decorator** is a special function in Python that takes another function as input, adds some functionality to it, and returns the modified function.

It’s written using the `@decorator_name` syntax just above the function definition. Think of it like “wrapping” a function to give it additional powers.

---
## 🔹 Syntax Structure

A basic decorator includes:

- A main decorator function that takes another function as its argument  
- A nested wrapper function that adds extra behavior  
- A return of the wrapper function to replace the original  

Example structure:

```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@decorator_name
def my_function():
    pass
```
---

## 🔹 Role of *args and **kwargs

Decorators are often written using `*args` and `**kwargs` to make them flexible. This ensures the wrapper can accept any number and type of arguments, making the decorator reusable across many functions.

---

## 🔹 Why Use Decorators?

Decorators make it easy to:

- Log execution details  
- Measure performance (timing functions)  
- Check user authentication  
- Cache results  
- Validate inputs and more  

---

## 🎯 Challenge – Create a Decorator to Log Execution Time

In this challenge, I:

- Created a decorator `log_execution_time` to measure how long a function takes to run  
- Used `time.time()` to capture start and end times  
- Calculated the execution duration and printed it  
- Applied the decorator to a function `process_large_dataset()` that simulates a heavy computation  

This challenge helped me understand how decorators work behind the scenes, how to write reusable and powerful wrapper functions, and how decorators can simplify performance logging in Python applications.
