# 🗓️ Day 13 – Data Structures: Stacks and Queues

In today’s challenge, I explored two fundamental linear data structures in Python — **stacks** and **queues**. These are the building blocks of many real-world applications like web browsing history, task scheduling, undo-redo operations, and more.

---

## 🧱 What are Data Structures?

A **data structure** is a way to store and organize data efficiently so that it can be used effectively. Linear data structures like stacks and queues manage elements in a sequence, with clear rules about how items are added or removed.

---

## 🔹 Stack (LIFO – Last In, First Out)

A **stack** works like a stack of plates — the last item added is the first to be removed. It follows the **LIFO** principle.

### Core Operations:
- `push(item)` → Add item to the top
- `pop()` → Remove item from the top
- `peek()` → View top item without removing
- `is_empty()` → Check if the stack is empty
- `display()` → Show all items in stack

### Real-life Examples:
- Browser history (back button)
- Undo feature in text editors
- Function call stack in programming

---

## 🔹 Queue (FIFO – First In, First Out)

A **queue** works like a line at a ticket counter — the first person in line is served first. It follows the **FIFO** principle.

### Core Operations:
- `enqueue(item)` → Add item to the end of the queue
- `dequeue()` → Remove item from the front
- `peek()` → View the front item
- `is_empty()` → Check if the queue is empty
- `display()` → Show all items in queue

### Real-life Examples:
- Print job scheduling
- Task queues in operating systems
- Customer support call center systems

In Python, a queue can be implemented using:
- `list` (less efficient)
- `collections.deque` (recommended)
- `queue.Queue` (for multi-threaded programs)

---

## 🎯 Challenge – Implement a Stack with Push, Pop, and Peek

In this challenge, I implemented a simple **stack** using a Python list.

- Created a `Stack` class with core methods: `push()`, `pop()`, `peek()`, `is_empty()`, and `display()`
- Simulated a browser history use case with multiple URLs
- Practiced how LIFO logic works in everyday applications

---

By doing this, I not only understood how stacks behave but also how data structures help organize and control program flow — a must-have foundation for problem solving, competitive coding, and system design.
