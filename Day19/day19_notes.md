# 🗓️ Day 19 – Threading, Multiprocessing & Concurrency

Today's focus was on understanding how Python handles **concurrent execution** using **threading** and **multiprocessing**, which are crucial for improving performance in I/O-bound and CPU-bound tasks respectively.

---

## 🧠 Topics Covered

### 🔹 Threading
Threading allows **multiple tasks to run "at the same time"** within a single program. It's perfect for **I/O-bound** operations like downloading files, user input, and file reading.

- Runs in the **same process**
- Shares memory space
- Lightweight, less overhead

🔧 Threading Example

```python
import threading

def task():
    print("Thread running...")

t = threading.Thread(target=task)
t.start()
t.join()
```
`start()` – Starts the thread

`join()` – Waits for the thread to finish


### 🔹 Multiprocessing
Multiprocessing creates **separate processes** that run in **true parallel** using multiple CPU cores. It’s best for **CPU-bound** tasks like number crunching or heavy data processing.

- Each process has **its own memory**
- Bypasses the **GIL (Global Interpreter Lock)**
- Suitable for performance-heavy computations

🔧 Basic Multiprocessing Example

```python
from multiprocessing import Process

def compute():
    print("Heavy computation running...")

p = Process(target=compute)
p.start()
p.join()
```

### 🔹 Concurrency
Concurrency means **handling multiple tasks during the same period**. Tasks may not literally run at the exact same time but are managed efficiently (like context switching) so no time is wasted.

---

## 🎯 Challenge – Download Files Using Threads

## Objective: Download multiple text files from URLs concurrently using Python threads.

✅ What I Did:

- Created a `download_file()` function that:

  - Downloads content using `requests.get()`

  - Writes it to a `.txt` file

- Created a thread for each file download

- Used `start()` to initiate and `join()` to synchronize threads

## 🧠 Key Learnings:

- How to manage multiple threads

- How to pass arguments to threads

- The importance of using `join()` to ensure all threads complete before moving on

- Efficient handling of I/O operations without blocking the main program

#3 🛠️ Summary

- Concurrency helps make programs responsive and efficient.

- Use threading when your task waits for external resources (like downloading or file access).

- Use multiprocessing when your task is computationally intensive.

Today’s challenge made me confident in writing concurrent programs using threads in Python.
 
