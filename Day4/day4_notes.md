# 🗓️ Day 04 – Prime Number Checker

## 🧩 Challenge:
Take a number as input from the user and check if it is a **prime number**.

---

## 🔢 What is a Prime Number?

A **prime number** is a natural number greater than 1 that is only divisible by:
- 1 and itself

👉 Examples of prime numbers: `2, 3, 5, 7, 11, 13...`  
👉 Numbers like `4, 6, 8, 9, 10` are **not prime** because they have additional divisors.

---

## 🧠 Concepts Used in This Challenge

### 🔹 1. User Input and Type Conversion
- I used the `input()` function to take a number from the user.
- Converted it to an integer using `int()` so I could perform arithmetic checks.

### 🔹 2. Conditional Statements
- First, I checked if the number is **less than 2** — because any number below 2 is not prime.
- This filters out negative numbers, 0, and 1.

### 🔹 3. Loops and the `range()` Function
- If the number is 2 or more, I checked if it is divisible by any number between `2` and `user_input - 1` using a `for` loop with `range()`.

### 🔹 4. Modulus Operator (`%`)
- I used `%` to check if the number has a remainder when divided by another number.
- If `user_input % i == 0`, that means `user_input` is divisible by `i` and **not prime**.

### 🔹 5. `break` and `else` with Loop
- If the number was divisible (not prime), I used `break` to stop the loop early.
- The `else` attached to the `for` loop runs **only if the loop wasn’t broken**, meaning no divisor was found — so the number is prime.

### 🔹 6. f-Strings for Output
- I used formatted strings (`f""`) to dynamically display whether the number is prime or not, making output more readable.

---

## 🧮 Logic Flow Recap

1. User enters a number.
2. If it's less than 2 → Not prime.
3. Else → Loop through numbers from 2 up to (but not including) the number.
   - If any divisor is found → Not prime.
   - If no divisors are found → Prime.

---

## ✅ What I Learned

- The definition and logic behind identifying prime numbers.
- How to use loops and conditions together to implement real-world logic.
- The difference between `for-else` vs `if-else`.
- How `break` and `else` on a loop can work as a smart way to check conditions efficiently.

This challenge helped me understand number theory basics and apply logical thinking using Python’s control flow tools.
