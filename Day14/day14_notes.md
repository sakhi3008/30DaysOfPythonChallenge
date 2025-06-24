# 🗓️ Day 14 – Recursive Functions, Base Cases and Factorial Challenge

In today’s challenge, I explored one of the most important concepts in programming — **recursion**. It is widely used in problems involving repetitive patterns, breaking problems down into subproblems, and solving them elegantly with cleaner code.

---

## 🔄 What is Recursion?

**Recursion** is a programming technique where a function calls itself to solve smaller instances of a problem. Each recursive call reduces the size of the problem until it reaches a stopping condition known as the **base case**.

Think of recursion like looking into a mirror placed in front of another mirror — the function keeps calling itself until it hits the simplest version of the problem.

---

## 🔹 Key Components of a Recursive Function

1. **Base Case**  
   The stopping condition. It tells the function when to stop calling itself.  
   Example: `if n == 0 or n == 1: return 1`

2. **Recursive Case**  
   The part where the function calls itself with a smaller value.  
   Example: `return n * factorial(n-1)`

Without a base case, the function would run infinitely, eventually causing a stack overflow.

---

## 🔹 Real-life Use Cases of Recursion

- Calculating factorials  
- Computing Fibonacci numbers  
- Solving mazes or tree structures  
- File system traversal (folders inside folders)  
- Divide-and-conquer algorithms (Merge Sort, Quick Sort)

---

## 🎯 Challenge – Calculate Factorial Recursively

In this challenge, I implemented a **recursive function** to calculate the factorial of a number:

- Added a **base case** to stop recursion when `n` is 0 or 1.
- Used the recursive formula: `factorial(n) = n * factorial(n-1)`
- Handled **invalid inputs** using `try-except` blocks.
- Displayed the result only for valid non-negative integers.

---

This challenge strengthened my understanding of how recursion works, how base and recursive cases interact, and why it’s important to include stopping conditions in any recursive logic.
