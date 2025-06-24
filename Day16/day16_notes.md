# 🗓️ Day 16 – `yield`, Iterators, and Lazy Evaluation

Today’s challenge deepened my understanding of how Python handles **iterators**, the use of the **`yield` keyword**, and the power of **lazy evaluation**. These are essential concepts for memory-efficient programming, especially when working with large data or infinite sequences.

---

## 🔹 What is an Iterator?

An **iterator** is any object in Python that implements two methods:
- `__iter__()` → returns the iterator object itself
- `__next__()` → returns the next value in the sequence

You typically use iterators when you want to loop through a sequence (like a list, tuple, or string), but Python also allows you to create your own custom iterators for more control.

### 🔸 Example:
```python
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
```
---

## 🔹 What is `yield`?

The `yield` keyword is used inside a function to make it a **generator**.

- A **generator** is a special type of iterator that **remembers its state** and **resumes execution** from where it left off.
- Unlike `return`, which ends a function, `yield` **pauses** it and sends a value back to the caller — then continues from the same place when called again.

This makes `yield` ideal for large or infinite sequences because it doesn't store all results in memory at once.

### 🔸 Example:
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)    # Output: 1,2,3
```
---

## 🔹 Lazy Evaluation

Lazy evaluation means values are **only calculated when needed**, not all at once. Generators achieve this by yielding one value at a time, which is very memory-efficient.

### 🔸 Example:
```python
def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_numbers()
for _ in range(5):
    print(next(gen))  # Output: 0,1,2,3,4
```
---

## 🔹 When to Use Generators?

Generators are useful when:

- You work with large datasets or streams
- You want memory-efficient looping
- You want to simplify iterator creation

Examples: reading huge files, streaming live data, or generating series like Fibonacci numbers.

---

## 🎯 Challenge – Generate the First n Fibonacci Numbers

In this challenge, I:

- Wrote a **generator function** `fibonacci_generator(n)` that uses `yield` to generate Fibonacci numbers one at a time.
- Used a **for loop** to yield the next Fibonacci number without storing the full list.
- Took user input `n` and printed the first `n` Fibonacci numbers.

This helped me understand the practical power of `yield`, how Python handles generator state, and how lazily-evaluated sequences work. It's a great technique for keeping memory usage low and code clean.
